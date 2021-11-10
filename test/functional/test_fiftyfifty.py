from source import create_app


def test_fifty_fifty_routes():
    flask_app = create_app()

    # Test fifty_fifty function is response or not
    with flask_app.test_client() as test_client:
        response = test_client.get('/game/fifty_fifty')
        assert response.status_code == 200
        assert b"first_option" in response.data
        assert b"second_option" in response.data
        assert b"attempt" in response.data 