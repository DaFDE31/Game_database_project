from flask import jsonify
from flask_cors import cross_origin
from . import db
from .models import Game, Platform, PlayedOn
from sqlalchemy.orm import joinedload

def register_routes(app):
    @app.route('/api/games')
    @cross_origin(origin='http://localhost:3000')  # explicitly allow this origin
    def get_games():
        games = Game.query.options(joinedload(Game.studio)).all()

        results = []
        for game in games:
            platforms = PlayedOn.query.filter_by(GameID=game.GameID).all()
            platform_names = [Platform.query.get(p.PlatID).Name for p in platforms]

            results.append({
                'id': game.GameID,
                'name': game.Name,
                'price': game.Price,
                'releaseDate': game.ReleaseDate.isoformat(),
                'rating': game.Rating,
                'studio': game.studio.Name if game.studio else 'Unknown',
                'platforms': platform_names
            })
        return jsonify(results)
