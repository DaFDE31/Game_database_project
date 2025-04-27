from flask import jsonify, request
from flask_cors import cross_origin
from . import db
from .models import Game, Platform, PlayedOn, GameStudio
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
    @app.route('/api/platforms')
    @cross_origin(origin='http://localhost:3000')
    def get_platforms():
        platforms = Platform.query.all()
        return jsonify([
            {'id': p.PlatID, 'name': p.Name}
            for p in platforms
        ])
    ### GET THE STUDIOS
    @app.route('/api/studios')
    @cross_origin(origin='http://localhost:3000')
    def get_studios():
        studios = GameStudio.query.all()
        return jsonify([
            {'id': s.StudioID, 'name': s.Name}
            for s in studios
        ])
    

    ### ADD GAMES TO THE DATABASE
    @app.route('/api/games', methods=['POST'])
    @cross_origin(origin='http://localhost:3000')
    def add_game():
        data = request.get_json()

        name = data.get('name')
        price = data.get('price')
        release_date = data.get('releaseDate')
        studio_name = data.get('studio')
        platforms = data.get('platforms', [])

        if not all([name, price, release_date, platforms]):
            return jsonify({'error': 'Missing fields'}), 400
        
        existing_game = Game.query.filter_by(Name = name).first()
        if existing_game:
            return jsonify({"This game already exists!"}), 400
        
        if studio_name:
            studio = GameStudio.query.filter_by(Name=studio_name).first()

            if not studio:
                studio = GameStudio(Name=studio_name, Location="N/A")
                db.session.add(studio)
                db.session.commit()
        
        new_game = Game(
            Name=name,
            Price=float(price),
            ReleaseDate=release_date,
            Rating=0,
            StudioID=studio.StudioID if studio else None
        )
        db.session.add(new_game)
        db.session.commit()


        for platform in platforms:
            p = Platform.query.filter_by(Name=platform).first()
            if p:
                played_on = PlayedOn(GameID=new_game.GameID, PlatID=p.PlatID)
                db.session.add(played_on)

        db.session.commit()

        return jsonify({'message': 'Game and Studio added successfully!', 'gameID': new_game.GameID, "gameName": new_game.Name}), 201