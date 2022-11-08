def test_get_all_breakfast_with_empty_db_returns_empty_list(client):
    #act
    response = client.get("/breakfast")
    response_body = response.get_json()

    #assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_breakfast_with_db_returns_404(client):
    #act
    response = client.get("/breakfast/1")
    response_body  = response.get_json()
    #assert
    assert response.status_code == 404
    assert "message" in response_body

def test_get_breakfast_with_populated_db_returns_breakfast_json(client, two_breakfasts):
    #act
    response = client.get("/breakfast/1")
    response_body  = response.get_json()
    #assert
    assert response.status_code == 200
    assert response_body == {"id": 1,
                            "name": "Cereal",
                            "rating": 2.0,
                            "prep_time": 3}

def test_post_one_breakfast_in_db(client, two_breakfasts):
    #act
    response = client.post("/breakfast", json = {
                    "name": "lazy oats",
                    "rating": 5.0,
                    "prep_time": 6})
    response_body = response.get_json()

    #assert
    assert response.status_code == 201
    assert "message" in response_body
    assert response_body["message"] == "Successfuly created Breakfast with id 3"
