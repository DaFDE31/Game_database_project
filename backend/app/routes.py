from flask import jsonify, request
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from datetime import datetime
from .models import Game, Platform, PlayedOn, GameStudio, UserAccount,Plays
from sqlalchemy.orm import joinedload

def register_routes(app):
    @app.route("/api/games")
    @cross_origin(origin="http://localhost:3000")  # explicitly allow this origin
    def get_games():
        games = Game.query.options(joinedload(Game.studio)).all()

        results = []
        for game in games:
            platforms = PlayedOn.query.filter_by(GameID=game.GameID).all()
            platform_names = [Platform.query.get(p.PlatID).Name for p in platforms]

            results.append({
                "id": game.GameID,
                "name": game.Name,
                "price": game.Price,
                "releaseDate": game.ReleaseDate.isoformat(),
                "rating": game.Rating,
                "studio": game.studio.Name if game.studio else "Unknown",
                "platforms": platform_names
            })
        return jsonify(results)
    @app.route("/api/platforms")
    @cross_origin(origin="http://localhost:3000")
    def get_platforms():
        platforms = Platform.query.all()
        return jsonify([
            {"id": p.PlatID, "name": p.Name}
            for p in platforms
        ])
    ### GET THE STUDIOS
    @app.route("/api/studios")
    @cross_origin(origin="http://localhost:3000")
    def get_studios():
        studios = GameStudio.query.all()
        return jsonify([
            {"id": s.StudioID, "name": s.Name}
            for s in studios
        ])
    

    ### ADD GAMES TO THE DATABASE
    @app.route("/api/games", methods=["POST"])
    @cross_origin(origin="http://localhost:3000")
    def add_game():
        data = request.get_json()

        name = data.get("name")
        price = data.get("price")
        release_date = data.get("releaseDate")
        studio_name = data.get("studio")
        platforms = data.get("platforms", [])

        if not all([name, price, release_date, platforms]):
            return jsonify({"error": "Missing fields"}), 400
        
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

        return jsonify({"message": "Game and Studio added!"}), 201
    
    ### CREATING AND LOGGING IN AS A USER
    @app.route("/api/register", methods=["POST"])
    @cross_origin(origin='http://localhost:3000')
    def register_user():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")
        first_name = data.get("firstName")
        last_name = data.get("lastName")
        region = data.get("region")
        dob = data.get("dob")  #"YYYY-MM-DD"

        if not all([username, password, email]):
            return jsonify({"error": "Username, email, and password required"}), 400
        if not all([first_name, last_name, dob]):
            return jsonify({"error": "Missing fields"}), 400

        if UserAccount.query.filter_by(UserName=username).first():
            return jsonify({"error": "User already exists"}), 400

        hash = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = UserAccount(
            UserName=username,
            Password=hash,
            Email = email,
            FirstName=first_name,
            LastName=last_name,
            Region=region,
            DoB=dob,
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered!"})

    @app.route("/api/login", methods=["POST"])
    @cross_origin(origin='http://localhost:3000')
    def login_user():
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = UserAccount.query.filter_by(UserName=username).first()

        if not user or check_password_hash(user.Password, password) == False:
            return jsonify({"error": "Username or Password are incorrect"}), 401

        return jsonify({"message": "Login successful", "userName": user.UserName})
    
    ### SAVING A GAME
    @app.route('/api/save_play', methods=['POST'])
    @cross_origin(origin='http://localhost:3000')
    def save_play():
        data = request.get_json()

        username = data.get('userName')  
        game_id = data.get('gameId')
        purchase_date = data.get('purchaseDate')
        hours_played = data.get('hoursPlayed', 0)
        platforms = data.get('platforms', [])

        if not all([username,game_id,platforms]):
            return jsonify({'error': 'Missing required fields'}), 400

        try:
            purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'Invalid date format'}), 400

        for platform in platforms:
            p = Platform.query.filter_by(Name=platform).first()
            if p:

                existing_play = Plays.query.filter_by(
                    GameID=data['gameId'],
                    UserID=data['userName'],
                    PlatID=p.PlatID
                ).first()

                if existing_play:
                    continue
                new_play = Plays(
                    UserID=username,
                    GameID=game_id,
                    PlatID=p.PlatID,
                    PurchaseDate=purchase_date,
                    Hours=hours_played
                )
                db.session.add(new_play)
        db.session.commit()

        return jsonify({'message': 'Game saved successfully'})

    
    @app.route('/api/saved_games', methods=['POST'])
    @cross_origin(origin='http://localhost:3000')
    def get_saved_games():
        data = request.get_json()
        username = data.get('userName')

        if not username:
            return jsonify({'error': 'Missing userName'}), 400
        
        plays = Plays.query.options(
            joinedload(Plays.game),
            joinedload(Plays.platform)
        ).filter_by(UserID=username).all()

        saved_games = {}

        for play in plays:
            game_id = play.GameID
            if game_id not in saved_games:
                saved_games[game_id] = {
                    "id" : play.GameID,
                    'name': play.game.Name if play.game else 'Unknown Game',
                    'hours': play.Hours,
                    'purchaseDate': play.PurchaseDate.isoformat() if play.PurchaseDate else '',
                    'platforms': []
                }
            if play.platform:
                saved_games[game_id]['platforms'].append(play.platform.Name)

        return jsonify(list(saved_games.values()))
    
    @app.route('/api/delete_saved_game', methods=['POST'])
    @cross_origin(origin='http://localhost:3000') 
    def delete_saved_game():
        data = request.get_json()
        user_name = data.get('userName')
        game_id = data.get('gameId')
        if not user_name or not game_id:
            return jsonify({'error': 'Missing user or game information'}), 400

        Plays.query.filter_by(UserID=user_name, GameID=game_id).delete()
        db.session.commit()

        return jsonify({'message': 'Deleted successfully'}), 200

    @app.route('/api/user_info', methods=['POST'])
    @cross_origin(origin='http://localhost:3000')
    def user_info():
        data = request.get_json()
        user_name = data.get('userName')

        if not user_name:
            return jsonify({'error': 'Missing username'}), 400

        user = UserAccount.query.filter_by(UserName=user_name).first()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'userName': user.UserName,
            'firstName': user.FirstName,
            'lastName': user.LastName,
            'region': user.Region if user.Region else "N/A",
            'dob': user.DoB.isoformat() if user.DoB else None
        })

