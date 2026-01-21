import pandas as pd
from rdflib import Graph

from ontology_library.high_level_functions.high_level_observation_functions import (
    harmonise_oim_sosa_observation_sea_temperature_degree_celsius,
)
from utils import bind_namespaces


def main():
    # Load the JSON data into a DataFrame
    df = pd.read_json("data/sea_temp.json")

    g = Graph()

    # Iterate over the rows and extract each field into variables
    for _index, row in df.iterrows():
        observation_id = str(row["id"])
        sea_temperature = row["sea_temperature_celsius"]
        timestamp = row["timestamp"]
        lat = row["latitude"]
        lon = row["longitude"]

        # Call the wave forecast observation template
        g += harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
            sea_temperature=sea_temperature,
            observation_id=observation_id,
            result_time=timestamp,
            feature_of_interest_id=f"loc_{lat}_{lon}",
        )

    # Bind namespaces for better readability
    g = bind_namespaces(g)

    # Serialize the graph to a file
    g.serialize(destination="output/sea_temp_observations.ttl", format="turtle")


if __name__ == "__main__":
    main()
