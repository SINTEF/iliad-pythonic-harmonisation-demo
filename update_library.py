from __future__ import annotations

from string import Template as StringTemplate
from typing import Any

from jinja2 import Template as JinjaTemplate
from SPARQLWrapper import JSON, SPARQLWrapper

from jinja_automation.jinja_templates.jinja_templates import (
    QUDT_QUANTITY_KINDS_TEMPLATE,
    QUDT_UNITS_TEMPLATE,
)
from ontology_library.utils import sanitize_function_name


def fetch_qudt_units(
    endpoint_url: str = "https://www.qudt.org/fuseki/qudt/query",
    query_file: str = "queries/qudt_units.sparql",
    limit: int = 1000,
    offset: int = 0,
) -> list[dict[str, Any]]:
    # Read the SPARQL query template from file
    with open(query_file, encoding="utf-8") as f:
        query_template = f.read()

    # Use Python's string.Template — not Jinja2
    tmpl = StringTemplate(query_template)
    query = tmpl.substitute(limit=limit, offset=offset)

    sparql = SPARQLWrapper(endpoint_url)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)

    try:
        ret = sparql.queryAndConvert()
    except Exception as e:
        raise RuntimeError(f"Failed at offset {offset}: {e}") from e

    return ret["results"]["bindings"]


def fetch_qudt_quantity_kinds(
    endpoint_url: str = "https://www.qudt.org/fuseki/qudt/query",
    query_file: str = "./jinja_automation/sparql_queries/qudt_quantity_kind.sparql",
    limit: int = 1000,
    offset: int = 0,
) -> list[dict[str, Any]]:
    # Load SPARQL query from file
    with open(query_file, encoding="utf-8") as f:
        query_template = f.read()

    # Substitute $limit and $offset placeholders
    tmpl = StringTemplate(query_template)
    query = tmpl.substitute(limit=limit, offset=offset)

    sparql = SPARQLWrapper(endpoint_url)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)

    try:
        ret = sparql.queryAndConvert()
    except Exception as e:
        raise RuntimeError(f"Failed at offset {offset}: {e}") from e

    return ret["results"]["bindings"]


def write_functions_with_template(
    filename: str,
    functions: list[dict[str, str]],
    template_str: str,
    imports: list[str] | None = None,
    module_docstring: str | None = None,
) -> None:
    qudt_unit_template = JinjaTemplate(template_str.strip())

    rendered_body = qudt_unit_template.render(functions=functions)

    # Compose the final module content
    content_parts = []

    # Optional module-level docstring
    if module_docstring:
        content_parts.append(f'"""{module_docstring}"""\n')

    # Add imports if provided
    if imports:
        content_parts.extend(imports)
        content_parts.append("")  # blank line after imports

    # Add the rendered functions
    content_parts.append(rendered_body.strip())

    # Write the final output
    with open(filename, "w") as f:
        f.write("\n".join(content_parts).strip() + "\n")

    print(f"Functions written to '{filename}'")


def fetch_all_units(batch: int = 1000) -> list[dict[str, Any]]:
    units = []
    offset = 0
    while True:
        batch_results = fetch_qudt_units(
            query_file="./jinja_automation/sparql_queries/qudt_unit.sparql",
            offset=offset,
            limit=batch,
        )
        if not batch_results:
            break
        units.extend(batch_results)
        print(f"Fetched {len(batch_results)} units (offset {offset})")
        offset += batch
    return units


def fetch_all_quantity_kinds(batch: int = 1000) -> list[dict[str, Any]]:
    quantity_kinds = []
    offset = 0
    while True:
        batch_results = fetch_qudt_quantity_kinds(offset=offset, limit=batch)
        if not batch_results:
            break
        quantity_kinds.extend(batch_results)
        print(f"Fetched {len(batch_results)} quantity kinds (offset {offset})")
        offset += batch
    return quantity_kinds


def create_unit_functions() -> None:
    all_units = fetch_all_units()
    print(all_units["label"])

    # Collapse by URI first (avoid multiple labels per same unit)
    by_uri = {}
    for b in all_units:
        uri = b["unit"]["value"]
        label = b.get("label", {}).get("value", "")
        if not label:
            continue
        by_uri[uri] = label  # keep last or first; your choice

    units = [{"uri": uri, "label": label} for uri, label in by_uri.items()]
    print(f"Total unique units (by URI): {len(units)}\n")

    seen_names = set()
    qudt_unit_functions = []

    for u in units:
        func_name = f"get_qudt_unit_{sanitize_function_name(u['label'])}"

        if func_name in seen_names:
            # Optional: log collision info
            print(f"Skipping duplicate function name {func_name} for URI {u['uri']}")
            continue

        seen_names.add(func_name)

        qudt_unit_functions.append(
            {
                "name": func_name,
                "return_type": "URIRef",
                "namespace": "QUDT_UNIT",
                "docstring": (
                    f"Returns the URI for QUDT unit: {u['label']} ({u['uri']})"
                ),
                "constant": u["uri"].split("/")[-1].upper(),
            }
        )

    imports = [
        "from rdflib import URIRef",
        "from ontology_library.constants import QUDT_UNIT",
    ]

    write_functions_with_template(
        filename="ontology_library/low_level_functions/qudt_unit_functions.py",
        functions=qudt_unit_functions,
        template_str=QUDT_UNITS_TEMPLATE,
        imports=imports,
        module_docstring="This module contains functions for the units in QUDT.",
    )


def create_quantity_kind_functions() -> None:
    imports = [
        "from rdflib import URIRef",
        "from ontology_library.constants import QUDT_QUANTITY_KIND",
    ]

    all_quantity_kinds = fetch_all_quantity_kinds()

    quantity_kinds = [
        {
            "uri": b["quantityKind"]["value"],
            "label": b.get("label", {}).get("value", ""),
        }
        for b in all_quantity_kinds
    ]

    print(f"Total quantity kinds fetched: {len(quantity_kinds)}\n")
    dynamic_quantity_kind_functions = [
        {
            "name": f"get_qudt_quantity_kind_{sanitize_function_name(q['label'])}",
            "return_type": "URIRef",
            "namespace": "QUDT_QUANTITY_KIND",
            "docstring": (
                f"Returns the URI for QUDT quantity kind: {q['label']} ({q['uri']})"
            ),
            "constant": q["uri"].split("/")[-1].upper(),
        }
        for q in quantity_kinds
        if q["label"]
    ]

    write_functions_with_template(
        filename="ontology_library/low_level_functions/qudt_quantity_kind_functions.py",
        functions=dynamic_quantity_kind_functions,
        template_str=QUDT_QUANTITY_KINDS_TEMPLATE,
        imports=imports,
        module_docstring="This module contains functions for the quantity kinds "
        "in QUDT.",
    )


if __name__ == "__main__":
    create_unit_functions()
    create_quantity_kind_functions()
    print("Function modules created successfully.")
