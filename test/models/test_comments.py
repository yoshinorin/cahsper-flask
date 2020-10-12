import pytest

from test import cahsper
from cahsper.models.comments import Comments

class TestComments(object):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.comment = Comments()
        self.comment.id = 12345
        self.comment.user_name = "ExampleUser"
        self.comment.comment = "Hello!!"
        self.comment.created_at = 1234567890

    def test_serialize(self):
        result = self.comment.serialize()
        assert result == {
            'id': 12345,
            'user_name': 'ExampleUser',
            'comment': 'Hello!!',
            'created_at': 1234567890
        }
