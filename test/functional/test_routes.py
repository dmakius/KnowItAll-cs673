from source import create_app


def test_home_page():
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"KNOWITALL" in response.data
        assert b"START" in response.data
        assert b"LeaderBoard" in response.data