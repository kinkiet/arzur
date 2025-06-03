from app import create_app, db
from app.models import Team, Player

app = create_app()

@app.before_request
def setup():
    db.drop_all()
    db.create_all()

    t1 = Team(name="Planets United", points=38, matches_played=20, wins=12)
    t2 = Team(name="Galaxy FC", points=42, matches_played=20, wins=14)
    t3 = Team(name="Stellar Squad", points=29, matches_played=20, wins=9)

    db.session.add_all([t1, t2, t3])
    db.session.commit()

    p1 = Player(name="Zenon", position="Forward", rating=8.2, goals=10, assists=4, team=t1)
    p2 = Player(name="Luna", position="Midfielder", rating=9.0, goals=12, assists=7, team=t2)
    p3 = Player(name="Orion", position="Forward", rating=8.5, goals=9, assists=10, team=t3)

    db.session.add_all([p1, p2, p3])
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
