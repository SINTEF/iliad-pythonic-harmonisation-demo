from typing import Optional
from rdflib import Graph
from datetime import datetime

from ontology_library.mid_level_functions.mid_level_observation_functions import (
    create_oim_sosa_observation_sea_temperature,
    create_oim_sosa_result_sea_temperature_degree_celsius,
)


def harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
    sea_temperature: float,
    observation_id: Optional[str] = None,
    result_time: Optional[datetime] = None,
    feature_of_interest_id: Optional[str] = None,
    sensor_id: Optional[str] = None,
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

    # def harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
    #     sea_temperature: float,
    #     observation_id: Optional[str] = None,
    #     result_time: Optional[str] = None,
    #     feature_of_interest_id: Optional[str] = None,
    #     sensor_id: Optional[str] = None,
    # ) -> Graph:
    #     # Get observation uri and observation graph
    #     (
    #         oim_sosa_observation_sea_temperature_uri,
    #         oim_sosa_observation_sea_temperature_graph,
    #     ) = create_oim_sosa_observation_sea_temperature(
    #         observation_id,  # Optional
    #         result_time,  # Optional
    #         feature_of_interest_id,  # Optional
    #         sensor_id,  # Optional
    #     )
    #
    #     (
    #         oim_sosa_result_sea_temperature_degree_celsius_uri,
    #         oim_sosa_result_sea_temperature_degree_celsius_graph,
    #     ) = create_oim_sosa_result_temperature_degree_celsius(
    #         sea_temperature, oim_sosa_observation_sea_temperature_uri
    #     )
    #
    #     # Combine the graphs into one
    #     observation_graph = (
    #         oim_sosa_observation_sea_temperature_graph
    #         + oim_sosa_result_sea_temperature_degree_celsius_graph
    #     )
    #
    return observation_graph
