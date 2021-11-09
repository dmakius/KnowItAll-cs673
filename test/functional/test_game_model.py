from source.models import Game, Question, Player

def test_player_model():
    game = Game(type = 'TEST', lives = 3, score = 0, question_time = 30, 
                    num_skip_question = 3, questions_left = str(0),
                    answer_location =  0, max_questions = 0)
    
    assert game.lives == 3
    assert game.score == 0
    assert game.question_time == 30