import pytest
from app import app

#Sets up test client (runs before each test)
#Setup code for tests (general pytest, not just Flask)
#The fixture creates a fake HTTP client that talks to your Flask app
@pytest.fixture
def client():
    """Creates a test client for your Flask app"""
    app.config['TESTING'] = True
    #Creates fake client (simulates browser/curl)
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    """Test GET /tasks endpoint"""
    response = client.get('/api/tasks/')
    assert response.status_code == 200
    assert isinstance(response.json , list)

def test_post_task(client):
    response = client.post('/api/tasks/' , json = {'title' : 'Test task'})
    assert response.status_code == 201
    assert response.json['title'] == 'Test task'
    assert response.json['completed'] == False
    assert 'id' in response.json
    
def test_put_task(client):
    response = client.put('/api/tasks/1' , json = {'completed' : True})
    assert response.status_code == 200
    assert 'message' in response.json
    assert 'updated successfully' in response.json['message']
    
def test_del_task(client):
    response = client.delete('/api/tasks/444')
    assert response.status_code == 200
    
    assert 'message' in response.json
    assert 'deleted successfully' in response.json['message']
    