import unittest
import unittest.mock
from unittest.mock import Mock, patch

from project.url import url_exists, process_response

url = 'http://google.com'
class FakeResponse():
    status_code = 200
    content = "Some content"

class FetchTests(unittest.TestCase):

    @mock.patch('requests.get')
    def test_returns_true_if_url_found(self, mock_request):
        mock_request.return_value.status_code = 200
        self.assertTrue(url_exists(url))
        mock_request.assert_called_once_with(url)

    @mock.patch('requests.get')
    def test_returns_false_if_url_not_found(self, mock_request):
        mock_request.return_value.status_code = 404
        self.assertFalse(url_exists(url + "/nonexistingurl"))
        mock_request.assert_called_once_with(url + "/nonexistingurl")


class ProcessResponseTests(unittest.TestCase):

    @patch('requests.get')
    def test_content_is_not_empty(self, mock_get):
        mock_get.return_value.content = "Fake content"
        response = process_response(url)
        self.assertIsNotNone(response.content)

# fake_response = FakeResponse()
# mock_request.return_value = fake_response

# fake_response.status_code = 404
# fake_response.content = "Hello, world"




# TODO
# change content to json
# remove context manager and use patch as decorator