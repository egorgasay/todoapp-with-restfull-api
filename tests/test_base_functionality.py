import requests


def test_base_functionality():
    # CREATE new test record (POST)
    test_headers = {"title" : "a1", "description" : "a1", "date" : "2077-04-23"}
    response = requests.post("http://localhost:8000/create/", json=test_headers)
    assert response.ok, "Error when trying to create a new record"
    # GET all records (GET)
    response = requests.get("http://localhost:8000/tasks/all")
    assert response.ok, "Error while getting the todo list"
    # GET all records (ids only)
    response = requests.get("http://localhost:8000/id-info/")
    # GET id from last record
    last_id = str(response.json()[-1]['id'])
    # GET by id (GET)
    response = requests.get(f"http://localhost:8000/tasks/{last_id}")
    assert response.ok, "Error while getting the record by id"
    # CHANGE status of test record (PUT)
    response = requests.put(f"http://localhost:8000/change-status/{last_id}/", json={"done" : "true"})
    assert response.ok, "Error when trying to change status"
    # DELETE test record (DELETE)
    response = requests.delete("http://localhost:8000/delete/"+last_id)
    assert response.ok, "Error while deleting the record"
