import pytest

from test import cahsper
from cahsper.models.users import Users

class TestUsers(object):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.user = Users()
        self.user.name = 'ExampleUser'
        self.user.created_at = 1234567890

    def test_serialize(self):
        result = self.user.serialize()
        assert result == {'name': 'ExampleUser', 'created_at': 1234567890 }
