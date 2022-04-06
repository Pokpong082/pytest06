from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../Lab055')        
from main import app

client = TestClient(app)

def test_call_test_api():
    response = client.get("/courses/test")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

# def test_post_insert():
#     response = client.post(
#         "/students/",
#         json={
#             "name": "string",
#             "description": "string",
#             "completed": "true",
#             "date": "string"
#         }
#     )
#     assert response.status_code == 200
#     assert response.json()[0]["name"] == "string"