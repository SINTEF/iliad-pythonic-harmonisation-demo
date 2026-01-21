from rdflib import Graph

from utils import bind_namespaces, sanitize_function_name


def test_sanitize_function_name_simple_unit():
    """Test simple single-word QUDT labels."""
    assert sanitize_function_name("Kilogram") == "kilogram"
    assert sanitize_function_name("Metre") == "metre"
    assert sanitize_function_name("Joule") == "joule"


def test_sanitize_function_name_compound_unit():
    """Test QUDT labels with 'per' for derived units."""
    assert sanitize_function_name("Joule per Tesla") == "joule_per_tesla"
    assert sanitize_function_name("Henry per Metre") == "henry_per_metre"
    assert sanitize_function_name("Kilogram per Mole") == "kilogram_per_mole"
    assert sanitize_function_name("Farad per Metre") == "farad_per_metre"


def test_sanitize_function_name_complex_unit():
    """Test complex QUDT labels with multiple components."""
    assert (
        sanitize_function_name("Ampere Square Metre per Joule Second")
        == "ampere_square_metre_per_joule_second"
    )
    assert (
        sanitize_function_name("Newton Square Metre per Square Kilogram")
        == "newton_square_metre_per_square_kilogram"
    )


def test_sanitize_function_name_with_prefix():
    """Test QUDT labels with SI prefixes."""
    assert sanitize_function_name("Mega Electron Volt") == "mega_electron_volt"
    assert sanitize_function_name("Reciprocal Mole") == "reciprocal_mole"
    assert sanitize_function_name("Reciprocal Metre") == "reciprocal_metre"


def test_sanitize_function_name_special_units():
    """Test special QUDT unit labels."""
    assert sanitize_function_name("Unitless") == "unitless"
    assert (
        sanitize_function_name("Unified Atomic Mass Unit") == "unified_atomic_mass_unit"
    )


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
