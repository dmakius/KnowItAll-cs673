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

#   This test ensures that the 'questions_left' array is initialized correctly, containing every question but the first one.
def test_questions_left_initialization():
    flask_app = create_app()
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        #TODO We need to dynamically get the game associated with the user/game instance
        game = Game.query.get(1)
        game.category = '' #this line isn't properly setting the category so the test only works when no category is active
        db.session.commit
        response = test_client.get('/game')
        assert response.status_code == 200
        questions_left = game.questions_left.split(',')
        questions_left[0] = int(''.join(filter(str.isdigit, questions_left[0])))
        #this line only works is the category is properly empty
        assert len(questions_left) == game.max_questions - 1
        for i in range(len(questions_left)):
            assert game.question_id != questions_left[i]


        
        
