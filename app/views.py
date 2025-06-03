from flask import Blueprint
from app.controllers import get_best_team, get_best_player, get_best_player_against_team

bp = Blueprint('routes', __name__)

@bp.route('/best_team')
def best_team():
    return get_best_team()

@bp.route('/best_player')
def best_player():
    return get_best_player()

@bp.route('/best_player_vs_team/<int:team_id>')
def best_player_vs_team(team_id):
    return get_best_player_against_team(team_id)
