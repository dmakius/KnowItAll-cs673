from source import create_app
from source.models import Game
from source import db

def test_home_page():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"KNOWITALL" in response.data
        assert b"START" in response.data
        assert b"LeaderBoard" in response.data
        assert b"Player Profile" in response.data
        assert b"About" in response.data

def test_category_page():
    flask_app = create_app()
    
    with flask_app.test_client() as test_client:
        response = test_client.get('/category')
        assert response.status_code == 200
        assert b"START" in response.data
        assert b"GEOGRAPHY" in response.data
        assert b"ART" in response.data
        assert b"COMPUTER SCIENCE" in response.data
        assert b"SCIENCE" in response.data
        assert b"MYTHOLOGY" in response.data
        assert b"TV SHOWS" in response.data
        assert b"MOVIE" in response.data
        assert b"ALL" in response.data
        
def test_game_page():
    flask_app = create_app()
    
    with flask_app.test_client() as test_client:
        response = test_client.get('/game')
        assert response.status_code == 200
        assert b"LIVES" in response.data
        assert b"SCORE" in response.data
        assert b"TIME" in response.data
        assert b"Lifelines" in response.data
        assert b"Next Question" in response.data
        assert b"Submit" in response.data
        assert b"QUIT GAME" in response.data
        assert b"Skip Question" in response.data
        assert b"50/50" in response.data
        
            