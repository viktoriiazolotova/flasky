import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.breakfast import Breakfast


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app) # if request is not finished , go to line 16
    def expire_session(sender, response, **extra):
        #help us to make sure that we always check most updated data
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
#creating a mock client
def client(app):
    return app.test_client()


@pytest.fixture
def two_breakfasts(app):
    #arrange
    breakfast1 = Breakfast(name= "Cereal", rating = 2.0,
                                prep_time = 3)
    breakfast2 = Breakfast(name= "Coffee", rating = 3.0,
                                prep_time = 5)

    db.session.add_all([breakfast1, breakfast2])
    db.session.commit()


    #dont need to return anything                       

