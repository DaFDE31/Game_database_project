from flask import jsonify, request
from . import db
from .models import Company, Platform, GameStudio, Game, GameGenre, PlayedOn, Review, Achievements, OnlineService, UserAccount, Plays, DLC, Downloaded
from flask import current_app as app

@app.route('/api/games', methods=['GET'])
def get_games():
    platform = request.args.get('platform')
    if platform:
        games = Game.query.filter_by(platform=platform).all()
    else:
        games = Game.query.all()
    return jsonify([{'id': g.id, 'title': g.title, 'platform': g.platform} for g in games])
