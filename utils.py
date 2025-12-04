from rdflib import Graph, Namespace
import re

from constants import (
    OIM_OBS,
    OIM_FEATURE,
    OIM_PROPERTY,
    OIM_RESULT,
    SOSA,
    QUDT,
    QUDT_UNIT,
)


def bind_namespaces(g: Graph = None):
    g.bind("oim-obs", OIM_OBS)
    g.bind("oim-feat", OIM_FEATURE)
    g.bind("oim-property", OIM_PROPERTY)
    g.bind("oim-result", OIM_RESULT)
    g.bind("sosa", SOSA)
    g.bind("qudt", QUDT)
    g.bind("qudt_unit", QUDT_UNIT)

    return g


def sanitize_function_name(label: str) -> str:
    """
    Converts a label into a valid Python function name:
    - Lowercases the label
    - Replaces any non-alphanumeric character with underscores
    - Prepends an underscore if it starts with a digit
    - Strips trailing underscores
    """
    label = label.lower()
    label = re.sub(r"\W+", "_", label)
    if re.match(r"^\d", label):
        label = "_" + label
    return label.rstrip("_")
