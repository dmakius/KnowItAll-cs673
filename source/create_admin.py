from . import db
from .models import Player
from werkzeug.security import generate_password_hash

def create_admin_prod():
    print("CREATING AN ADMIN USER IN PROD")
    
    email = 'admin@test.com'
    player_name='admin'
    password1= "admin1234"
    new_admin = Player(email=email, player_name=player_name, password=generate_password_hash(password1, method='sha256'), admin=True)

    db.session.add(new_admin)
  
    db.session.commit()

    print("ADMIN USER SUCESSFULLY CREATED!")