from source.models import LeaderboardScore

def test_LeaderboardScore_model():
    leaderboard = LeaderboardScore(
        category = 'categoryTest',
        username = 'userNameTest',
        score = 1000
    )

    assert leaderboard.score == 1000;
    assert leaderboard.category == 'categoryTest'
    assert leaderboard.username == 'userNameTest'



