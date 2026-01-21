from datetime import datetime, timezone

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF

from constants import SOSA
from ontology_library.high_level_functions.high_level_observation_functions import (
    harmonise_oim_sosa_observation_sea_temperature_degree_celsius,
)
from ontology_library.low_level_functions.low_level_observation_functions import (
    create_oim_sosa_observation_uri,
    create_sosa_observation,
    get_oim_observation_namespace,
)


class TestLowLevelFunctions:
    def test_create_oim_sosa_observation_uri(self):
        uri = create_oim_sosa_observation_uri("test-obs-123")
        assert isinstance(uri, URIRef)
        assert "test-obs-123" in str(uri)

    def test_create_oim_sosa_observation_uri_with_namespace(self):
        uri = create_oim_sosa_observation_uri("my-observation")
        namespace = get_oim_observation_namespace()
        assert str(uri).startswith(str(namespace))

    def test_create_sosa_observation_basic(self):
        obs_uri = URIRef("http://example.org/obs/1")
        graph = create_sosa_observation(observation_uri=obs_uri)

        assert isinstance(graph, Graph)
        assert (obs_uri, RDF.type, SOSA.Observation) in graph

    def test_create_sosa_observation_with_result_time(self):
        obs_uri = URIRef("http://example.org/obs/1")
        result_time = datetime(2025, 6, 15, 12, 0, 0, tzinfo=timezone.utc)

        graph = create_sosa_observation(
            observation_uri=obs_uri,
            result_time=result_time,
        )

        # Check that result time triple exists
        result_times = list(graph.objects(obs_uri, SOSA.resultTime))
        assert len(result_times) == 1
        assert isinstance(result_times[0], Literal)


class TestHighLevelFunctions:
    def test_harmonise_returns_graph(self):
        result = harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
            sea_temperature=15.5,
            observation_id="test-123",
        )
        assert isinstance(result, Graph)

    def test_harmonise_creates_observation_triple(self):
        result = harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
            sea_temperature=15.5,
            observation_id="test-456",
        )

        # Check that at least one SOSA Observation exists
        observations = list(result.subjects(RDF.type, SOSA.Observation))
        assert len(observations) == 1

    def test_harmonise_creates_result_triple(self):
        result = harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
            sea_temperature=20.0,
            observation_id="test-789",
        )

        # Check that at least one SOSA Result exists
        results = list(result.subjects(RDF.type, SOSA.Result))
        assert len(results) == 1

    def test_harmonise_stores_temperature_value(self):
        temperature = 18.5
        result = harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
            sea_temperature=temperature,
            observation_id="test-temp",
        )

        # Find the result and check its value
        values = list(result.objects(predicate=SOSA.hasValue))
        assert len(values) == 1
        assert float(values[0]) == temperature

    def test_harmonise_with_feature_of_interest(self):
        result = harmonise_oim_sosa_observation_sea_temperature_degree_celsius(
            sea_temperature=12.0,
            observation_id="test-foi",
            feature_of_interest_id="location_123",
        )

        # Check that feature of interest is linked
        foi_links = list(result.subject_objects(SOSA.hasFeatureOfInterest))
        assert len(foi_links) == 1
