import os
import json
from enum import Enum
import pytest

from hyperon_das import DistributedAtomSpace


class ActionType(str, Enum):
    COUNT_ATOMS = "count_atoms"
    GET_ATOM = "get_atom"
    GET_NODE = "get_node"
    GET_LINK = "get_link"
    GET_LINKS = "get_links"
    GET_INCOMING_LINKS = "get_incoming_links"
    QUERY = "query"


class TestRemoteDistributedAtomSpace:
    """Integration tests with OpenFaas function on the server"""

    @pytest.fixture
    def remote_das(self):
        return DistributedAtomSpace(
            query_engine="remote",
            host=os.getenv("TEST_REMOTE_HOST"),
            port=os.getenv("TEST_REMOTE_PORT"),
        )

    def get_request(self, action: ActionType):
        request_file = f"{os.getenv('TEST_REMOTE_DATABASE')}.json"

        current_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_path, "fixtures", "request", request_file)

        with open(filepath, "r") as file:
            requests = json.loads(file.read())

            return requests.get(action.value)

    def get_response(self, action: ActionType):
        response_file = f"{os.getenv('TEST_REMOTE_DATABASE')}.json"

        current_path = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_path, "fixtures", "response", response_file)

        with open(filepath, "r") as file:
            requests = json.loads(file.read())

            return requests.get(action.value)

    def test_server_connection(self):
        host = os.getenv("TEST_REMOTE_HOST")
        port = os.getenv("TEST_REMOTE_PORT")
        try:
            das = DistributedAtomSpace(query_engine="remote", host=host, port=port)
        except Exception as e:
            pytest.fail(f"Connection with OpenFaaS server fail, Details: {str(e)}")
        if not das.query_engine.remote_das.url:
            pytest.fail("Connection with server fail")
        assert (
            das.query_engine.remote_das.url
            == f"http://{host}:{port}/function/query-engine"
        )

    def test_get_atom(self, remote_das: DistributedAtomSpace):
        payload = self.get_request(ActionType.GET_ATOM)
        expected_output = self.get_response(ActionType.GET_ATOM)

        result = remote_das.get_atom(**payload)
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"

    def test_get_node(self, remote_das: DistributedAtomSpace):
        payload = self.get_request(ActionType.GET_NODE)
        expected_output = self.get_response(ActionType.GET_NODE)

        result = remote_das.get_node(**payload)
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"

    def test_get_link(self, remote_das: DistributedAtomSpace):
        payload = self.get_request(ActionType.GET_LINK)
        expected_output = self.get_response(ActionType.GET_LINK)

        result = remote_das.get_link(**payload)
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"

    def test_get_links(self, remote_das: DistributedAtomSpace):
        payload = self.get_request(ActionType.GET_LINKS)
        expected_output = self.get_response(ActionType.GET_LINKS)

        result = remote_das.get_links(**payload)
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"

    def test_get_incoming_links(self, remote_das: DistributedAtomSpace):
        payload = self.get_request(ActionType.GET_INCOMING_LINKS)
        expected_output = self.get_response(ActionType.GET_INCOMING_LINKS)

        result = remote_das.get_incoming_links(**payload)
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"

    def test_count_atoms(self, remote_das: DistributedAtomSpace):
        expected_output = self.get_response(ActionType.COUNT_ATOMS)

        result = list(remote_das.count_atoms())
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"

    def test_query(self, remote_das: DistributedAtomSpace):
        payload = self.get_request(ActionType.QUERY)
        expected_output = self.get_response(ActionType.QUERY)

        result = remote_das.query(**payload)
        assert (
            result == expected_output
        ), f"Assertion failed:\nResponse Body: {result}\nExpected: {json.dumps(expected_output)}"
