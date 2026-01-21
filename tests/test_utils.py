from utils import sanitize_function_name


def test_sanitize_function_name_basic():
    assert sanitize_function_name("Degree Celsius") == "degree_celsius"


def test_sanitize_function_name_with_special_chars():
    assert sanitize_function_name("Metre per Second") == "metre_per_second"


def test_sanitize_function_name_starting_with_digit():
    assert sanitize_function_name("3D Printer") == "_3d_printer"
