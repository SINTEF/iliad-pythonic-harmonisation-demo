# Jinja2 template for generating QUDT unit definitions in Python

# Template for quantity kind functions
QUDT_UNITS_TEMPLATE = '''
{% for func in functions %}
def {{ func.name }}() -> {{ func.return_type }}:
    {% if func.docstring %}"""{{ func.docstring }}"""{% endif %}
    return {{ func.namespace }}["{{ func.constant }}"]

{% endfor %}
'''

# Template for quantity kind functions
QUDT_QUANTITY_KINDS_TEMPLATE = '''
{% for func in functions %}
def {{ func.name }}() -> {{ func.return_type }}:
    {% if func.docstring %}"""{{ func.docstring }}"""{% endif %}
    return {{ func.namespace }}["{{ func.constant }}"]

{% endfor %}
'''
