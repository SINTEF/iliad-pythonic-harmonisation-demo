from __future__ import annotations

from datetime import datetime

from rdflib import Graph

from ontology_library.mid_level_functions.mid_level_observation_functions import (
    create_oim_sosa_observation_sea_temperature,
    create_oim_sosa_result_sea_temperature_degree_celsius,
)


def harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
    sea_temperature: float,
    observation_id: str | None = None,
    result_time: datetime | None = None,
    feature_of_interest_id: str | None = None,
    sensor_id: str | None = None,
) -> Graph:
    obs_iri, obs_graph = create_oim_sosa_observation_sea_temperature(
        observation_id=observation_id,
        result_time=result_time,
        feature_of_interest_id=feature_of_interest_id,
    )

    result_iri, result_graph = create_oim_sosa_result_sea_temperature_degree_celsius(
        sea_temperature=sea_temperature, observation_iri=obs_iri
    )

    return obs_graph + result_graph
