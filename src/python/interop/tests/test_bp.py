import pytest
from unittest.mock import Mock, MagicMock

from bp import FilterPostRoutingRule
from message import PostMessage
from obj import PostClass

class TestFilterPostRoutingRule:

    def test_iris_to_python(self,mock_send_request_sync):
        # Create a mock iris.dc.Demo.PostMessage object
        iris_post = MagicMock()
        iris_post.Post.Title = "Test Title"
        iris_post.Post.Selftext = "Test Selftext"
        iris_post.Post.Author = "Test Author"
        iris_post.Post.Url = "https://www.example.com"
        iris_post.Post.CreatedUTC = 1234567890
        iris_post.Post.OriginalJSON = {"key": "value"}

        # Create a FilterPostRoutingRule object
        fpr = FilterPostRoutingRule()
        fpr.on_python_message = mock_send_request_sync

        # Call the iris_to_python method with the mock iris.dc.Demo.PostMessage object
        fpr.iris_to_python(iris_post)

        # Check that the result is a PostMessage object with the correct attributes
        assert mock_send_request_sync.called
        
        # Check that the result is a PostMessage object with the correct attributes
        assert mock_send_request_sync.call_args[0][0] == PostMessage(post=PostClass(title='Test Title', selftext='Test Selftext', author='Test Author', url='https://www.example.com', created_utc=1234567890, original_json={'key': 'value'}))


    @pytest.fixture
    def mock_send_request_sync(self):
        return Mock()

    def test_on_python_message(self,mock_send_request_sync):
        rule = FilterPostRoutingRule()
        # fix the target to avoid the error
        target = 'Python.FileOperation'
        rule.target = target
        rule.send_request_sync = mock_send_request_sync

        post = PostClass(title='Test Post', selftext='This is a test post about dogs.', author='Test Author', url='http://test.com', created_utc=1234567890, original_json='{}')
        message = PostMessage(post=post)

        rule.on_python_message(message)

        # assert that the send_request_sync has been called once
        excepted = message
        excepted.to_email_address = 'dog@company.com'
        excepted.found = 'Dog'

        mock_send_request_sync.assert_called_once_with(target, excepted)