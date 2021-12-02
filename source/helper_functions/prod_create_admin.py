from source import  db
from source.models import Player

print(db)

p = Player.query.all()

for x in p:
    print(x);