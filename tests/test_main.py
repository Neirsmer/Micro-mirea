import requests
api = 'http://localhost:7000'
def test_health():
    response =requests.get(f'{api}/health')
    assert response.status_code == 200
def test_bye():
    response =requests.get(f'{api}/1_nya')
    assert response.status_code == 200
#dsdssddd