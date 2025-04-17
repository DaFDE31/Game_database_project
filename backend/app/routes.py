from flask import jsonify, request, Flask, current_app as app
from . import db
from .models import Company, Platform, GameStudio, Game, GameGenre, PlayedOn, Review, Achievements, OnlineService, UserAccount, Plays, DLC, Downloaded
from sqlalchemy.orm import joinedload

'''
@app.route('/api/games', methods=['GET'])
def get_games():
    platform = request.args.get('platform')
    if platform:
        games = Game.query.filter_by(platform=platform).all()
    else:
        games = Game.query.all()
    return jsonify([{'id': g.id, 'title': g.title, 'platform': g.platform} for g in games])
'''

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

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
