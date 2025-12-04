from rdflib import URIRef, Namespace, Graph, Literal
from rdflib.namespace import RDF, XSD
from datetime import datetime
from typing import Optional
from constants import QUDT, QUDT_UNIT, SOSA

# Import automatically generated functions
from ontology_library.low_level_functions.qudt_unit_functions import (
    get_qudt_unit_degree_celsius,
)

from ontology_library.low_level_functions.qudt_quantity_kind_functions import (
    get_qudt_quantity_kind_temperature,
)


## NAMESPACE FUNCTIONS ##
def get_oim_observation_namespace() -> Namespace:
    return Namespace("https://w3id.org/iliad/oim/observations/")


def get_oim_result_namespace() -> Namespace:
    return Namespace("https://w3id.org/iliad/oim/results/")


def get_oim_sensor_namespace() -> Namespace:
    return Namespace("https://w3id.org/iliad/oim/sensors/")


def get_oim_feature_of_interest_namespace() -> Namespace:
    return Namespace("https://w3id.org/iliad/oim/features_of_interest/")


def get_oim_property_namespace() -> Namespace:
    return Namespace("https://w3id.org/iliad/oim/property/")


## UNITS AND QUANTITY KINDS FUNCTIONS ##
def get_oim_quantity_kind_sea_temperature() -> URIRef:
    OIM_PROPERTY = get_oim_property_namespace()

    return OIM_PROPERTY.seaTemperature


## OBSERVATION FUNCTIONS ##
def create_oim_sosa_observation_uri(observation_id: str = None) -> URIRef:
    OIM_OBS = get_oim_observation_namespace()

    # If no observation_id is provided, use the current datetime
    if observation_id is None:
        observation_id = str(datetime.now())

    return OIM_OBS[observation_id]


def create_sosa_observation(
    observation_uri: URIRef,
    result_time: Optional[datetime] = None,
    feature_of_interest_id: Optional[str] = None,
    sensor_id: Optional[str] = None,
    result_uri: Optional[str] = None,
    observable_property_uri: Optional[URIRef] = None,
) -> Graph:
    g = Graph()
    g.add((observation_uri, RDF.type, SOSA.Observation))

    # Add result time if provided
    if result_time:
        g.add(
            (
                observation_uri,
                SOSA.resultTime,
                Literal(result_time, datatype=XSD.dateTime),
            )
        )

    # Add feature of interest if provided
    if feature_of_interest_id:
        feature_of_interest_uri = create_oim_feature_of_interest_uri(
            feature_of_interest_id
        )
        g.add((observation_uri, SOSA.hasFeatureOfInterest, feature_of_interest_uri))

    # Add sensor if provided
    if sensor_id:
        sensor_uri = create_oim_sosa_sensor_uri(sensor_id)
        g.add((observation_uri, SOSA.madeBySensor, sensor_uri))

    # Add result if provided
    if result_uri:
        g.add((observation_uri, SOSA.hasResult, result_uri))

    # Add observable property if provided
    if observable_property_uri:
        g.add((observation_uri, SOSA.observedProperty, observable_property_uri))

    return g


### RESULT FUNCTIONS ###
def create_oim_sosa_result_uri() -> URIRef:
    OIM_RESULT = get_oim_result_namespace()

    id = str(datetime.now()).replace(" ", "_")

    return OIM_RESULT[id]


def create_sosa_result(
    measured_value: float,
    observation_uri: URIRef,
    unit: URIRef,
    result_uri: URIRef,
) -> Graph:
    g = Graph()

    # Add the result triples to the graph
    g.add((result_uri, RDF.type, SOSA.Result))
    g.add((result_uri, SOSA.hasValue, Literal(measured_value, datatype=XSD.float)))
    g.add((result_uri, SOSA.hasUnit, unit))

    # Add as a qudt quantity value
    g.add((result_uri, RDF.type, QUDT.QuantityValue))

    # Connect the result to the observation
    g.add((observation_uri, SOSA.hasResult, result_uri))

    return g


## SENSOR FUNCTIONS ##
def create_oim_sosa_sensor_uri(sensor_id: str = None) -> URIRef:
    # Create the URI of the new observation individual
    OIM_SENSORS = get_oim_sensor_namespace()

    return OIM_SENSORS[sensor_id]


## FEATURE OF INTEREST FUNCTIONS ##
def create_oim_feature_of_interest_uri(feature_of_interest_id: str) -> URIRef:
    OIM_FEATURE = get_oim_feature_of_interest_namespace()
    return OIM_FEATURE[feature_of_interest_id]
