from source.models import Game, Question, Player

#Test for the game session object
def test_game_model():
    game = Game(type = 'TEST', lives = 3, score = 0, question_time = 30, 
                    num_skip_question = 3, questions_left = str(0),
                    answer_location =  0, max_questions = 0)
    #This portion ensures that all of the functional aspects of the game table were actively updated.
    assert game.lives == 3
    assert game.score == 0
    assert game.question_time == 30
    assert game.num_skip_question == 3
    assert game.max_questions == 0
    assert game.answer_location == 0
    assert game.questions_left == '0'

    #Test for the player object
    
    #Test for the question object

    #Test for the ledaerboard object