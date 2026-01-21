from rdflib import Graph

from utils import bind_namespaces, sanitize_function_name


def test_sanitize_function_name_basic():
    assert sanitize_function_name("Degree Celsius") == "degree_celsius"


def test_sanitize_function_name_with_special_chars():
    assert sanitize_function_name("Metre per Second") == "metre_per_second"


def test_sanitize_function_name_starting_with_digit():
    assert sanitize_function_name("3D Printer") == "_3d_printer"


def test_bind_namespaces():
    g = Graph()
    result = bind_namespaces(g)

    # Check that namespaces are bound
    namespaces = dict(result.namespaces())
    assert "oim-obs" in namespaces
    assert "oim-feat" in namespaces
    assert "sosa" in namespaces
    assert "qudt" in namespaces


def test_bind_namespaces_returns_graph():
    g = Graph()
    result = bind_namespaces(g)
    assert isinstance(result, Graph)
    assert result is g  # Same graph object returned
