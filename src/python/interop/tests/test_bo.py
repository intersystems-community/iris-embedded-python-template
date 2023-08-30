from bo import FileOperation
import os
from unittest.mock import patch, mock_open, MagicMock

class TestFileOperation():

    def test_on_init(self):
        """
        This method is called when the operation is initialized.
        """
        # Create a FileOperation instance
        operation = FileOperation()

        # Set the path attribute
        operation.path = "/path/to/directory"

        # Use a context manager to temporarily change the current working directory
        with patch.object(os, "chdir") as mock_chdir:
            # Call the on_init method
            operation.on_init()

            # Assert that the chdir function was called with the correct argument
            mock_chdir.assert_called_once_with("/path/to/directory")

    @patch('bo.FileOperation.put_line')
    def test_on_post_message(self, mock_put_line):
        # Create a mock PostMessage object
        post_message = MagicMock()
        post_message.post.title = "Test Title"
        post_message.post.author = "Test Author"
        post_message.post.url = "http://test.com"
        post_message.post.selftext = "Test Text"
        post_message.found = "Test Company"

        # Create a FileOperation object and call the on_post_message method with the mock PostMessage object
        file_operation = FileOperation()
        file_operation.on_post_message(post_message)

        # assert that the put_line has been called 4 times
        assert mock_put_line.call_count == 4

        # assert that the put_line has been called with the correct arguments
        mock_put_line.call_args_list[0][0][0] == "Test Company.txt"
        mock_put_line.call_args_list[0][0][1] == '1970-01-01 01:00:01 : Test Title : Test Author : http://test.com'
        mock_put_line.call_args_list[1][0][0] == "Test Company.txt"
        mock_put_line.call_args_list[1][0][1] == ""
        mock_put_line.call_args_list[2][0][0] == "Test Company.txt"
        mock_put_line.call_args_list[2][0][1] == "Test Text"
        mock_put_line.call_args_list[3][0][0] == "Test Company.txt"
        mock_put_line.call_args_list[3][0][1] == ' * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'

    def test_put_line(self):
            # create a mock file object
            m = mock_open()
            
            # patch the built-in open function with the mock object
            with patch('builtins.open', m):
                # call the function with some test data
                filename = 'test.txt'
                string = 'hello world'
                FileOperation().put_line(filename, string)
                
                # check if the mock file object was called with the expected arguments
                m.assert_called_once_with(filename, 'a', encoding='utf-8')
                handle = m()
                handle.write.assert_called_once_with(string)