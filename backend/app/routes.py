from flask import jsonify, request
from . import db
from .models import Company, Platform, GameStudio, Game, GameGenre, PlayedOn, Review, Achievements, OnlineService, UserAccount, Plays, DLC, Downloaded
from sqlalchemy.orm import joinedload

def register_routes(app):
    @app.route('/api/games')
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
                'releaseDate': game.ReleaseDate.isoformat(),  # converts to 'YYYY-MM-DD'
                'rating': game.Rating,
                'studio': game.studio.Name if game.studio else 'Unknown',
                'platforms': platform_names
            })
        print(results)
        response = jsonify(results)
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
        return response