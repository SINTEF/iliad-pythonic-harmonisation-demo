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

# Template for sosa observations using qudt quantity kinds
QUDT_QUANTITY_KIND_OBSERVATION_TEMPLATE = ''' 
{% for func in functions %}
def {{ func.name }} -> {{ func.return_type }}:
    {% if func.docstring %}"""{{ func.docstring }}"""{% endif %}

    # Get/Create observation URI
    observation_uri = create_sosa_observation_uri(observation_id)

    # Create the observation graph
    observation_graph = create_sosa_observation(
        observation_uri=observation_uri,
        result_time=result_time,
        feature_of_interest_id=feature_of_interest_id,
        sensor_id=sensor_id,
        observable_property_uri={{ func.namespace }}["{{ func.constant }}"],
    )

    return (
        observation_uri,
        observation_graph,
    )

{% endfor %}
'''
