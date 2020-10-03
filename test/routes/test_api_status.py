from test import cahsper

def test_status_api():

    response = cahsper.test_client().get('/status')
    assert response.status_code == 200
    assert b'{"status":"operational"}\n' in response.data
