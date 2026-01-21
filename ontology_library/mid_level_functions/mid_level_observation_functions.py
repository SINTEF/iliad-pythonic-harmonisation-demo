from __future__ import annotations

from datetime import datetime

from rdflib import Graph, URIRef

from ontology_library.low_level_functions.low_level_observation_functions import (
    create_oim_sosa_observation_uri,
    create_oim_sosa_result_uri,
    create_sosa_observation,
    create_sosa_result,
    get_oim_quantity_kind_sea_temperature,
)
from ontology_library.low_level_functions.qudt_unit_functions import (
    get_qudt_unit_degree_celsius,
)


def create_oim_sosa_observation_sea_temperature(
    observation_id: str,
    result_time: datetime | None = None,
    feature_of_interest_id: str | None = None,
    sensor_id: str | None = None,
) -> Graph:
    # Get/Create observation URI
    observation_uri = create_oim_sosa_observation_uri(observation_id)

    # Create the observation graph
    observation_graph = create_sosa_observation(
        observation_uri=observation_uri,
        result_time=result_time,
        feature_of_interest_id=feature_of_interest_id,
        sensor_id=sensor_id,
        observable_property_uri=get_oim_quantity_kind_sea_temperature(),
    )

    return observation_uri, observation_graph


def create_oim_sosa_result_sea_temperature_degree_celsius(
    sea_temperature: float, observation_iri: URIRef
) -> Graph:
    unit = get_qudt_unit_degree_celsius()
    oim_sosa_result_iri = create_oim_sosa_result_uri()

    oim_sosa_result_graph = create_sosa_result(
        sea_temperature, observation_iri, unit, oim_sosa_result_iri
    )
    return oim_sosa_result_iri, oim_sosa_result_graph
