import unittest
import unittest.mock
from unittest.mock import Mock, patch
import requests

from project.services import get_todos, get_uncompleted_todos

class Testing(unittest.TestCase):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('project.services.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()


    @patch('project.services.requests.get')
    def test_request_response(self, mock_get):
        todos = [{
                'userid' : 1,
                'id' : 1,
                'title' : 'Make the bed',
                'completed' : False
        }]



        # Configure the mock to return a response with an OK status code.
        # Also, the mock should have a 'json()' method that returns a list of todos
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
        response = get_todos()

        # If the request is sent successfully, then I expect a response to be returned 
        self.assertEqual(response.json(), todos)

    @patch('project.services.requests.get')
    def testing_getting_todos_when_response_is_not_ok(self, mock_get):
        # Configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        response = get_todos()

        # If the response contains an error, I should get no todos.
        self.assertIsNone(response)

    @patch('project.services.get_todos')
    def test_getting_uncompleted_todos_when_todos_is_not_none(self, mock_get_todos):
        todo1 = {
            'userId' : 1,
            'id' : 1,
            'title' : 'Make the bed',
            'completed' : False
        }
        todo2 = {
            'userId' : 1,
            'id' : 2,
            'title' : 'Walk the dog',
            'completed' : True
        }
        
        # Configure mock to return a response with a JSON-serialized list of todos.
        mock_get_todos.return_value = Mock()
        mock_get_todos.return_value.json.return_value = [todo1, todo2]

        # Call the service, which will get a list of todos filtered on completed.
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called.
        self.assertTrue(mock_get_todos.called)

        # Confirm that the expected filtered list of todos was returned.
        self.assertEqual(uncompleted_todos, [todo1])

    @patch('project.services.get_todos')
    def test_getting_uncompleted_todos_when_todos_is_none(self, mock_get_todos):
        # Configure mock to return None
        mock_get_todos.return_value = None

        # Call the service, which will return an empty list.
        uncompleted_todos = get_uncompleted_todos()

        # Confirm that the mock was called.
        self.assertTrue(mock_get_todos.called)

        # Confirm that an empty list was returned.
        self.assertEqual(uncompleted_todos, [])

class Integration(unittest.TestCase):
    def test_integration_contract(self):
        # Call the service to hit the actual API.
        actual = get_todos()
        actual_keys = actual.json().pop().keys()

        # Call the service to hit the mocked API.
        with patch('project.services.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'userId': 1,
                'id': 1,
                'title': 'Make the bed',
                'completed': False
            }]

            mocked = get_todos()
            mocked_keys = mocked.json().pop().keys()

        # An object from the actual API and an object from the mocked API should
        # have the same data structure.
        self.assertEqual(list(actual_keys), list(mocked_keys))