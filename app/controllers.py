from app.models import Team, Player
from sqlalchemy import desc
from flask import jsonify

def get_best_team():
    best_team = Team.query.order_by(desc(Team.points)).first()
    return jsonify({'best_team': best_team.name, 'points': best_team.points})

def get_best_player():
    best_player = Player.query.order_by(desc(Player.goals + Player.assists)).first()
    return jsonify({'best_player': best_player.name, 'goals': best_player.goals, 'assists': best_player.assists})

def get_best_player_against_team(team_id):
    team = Team.query.get(team_id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    best_player = Player.query.order_by(desc(Player.goals + Player.assists)).first()
    return jsonify({
        'team_to_beat': team.name,
        'recommended_player': best_player.name,
        'goals': best_player.goals,
        'assists': best_player.assists
    })
