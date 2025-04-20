from . import db


class Company(db.Model):
    __tablename__ = 'company'
    CompID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))


class Platform(db.Model):
    __tablename__ = 'platform'
    PlatID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Generation = db.Column(db.Integer)
    Price = db.Column(db.Float)
    Sales = db.Column(db.Integer)
    CompanyID = db.Column(db.Integer, db.ForeignKey('company.CompID'))
    ReleaseDate = db.Column(db.Date)

    company = db.relationship("Company")


class GameStudio(db.Model):
    __tablename__ = 'gamestudio'
    StudioID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Location = db.Column(db.String(255))


class Game(db.Model):
    __tablename__ = 'game'
    GameID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Price = db.Column(db.Float)
    ReleaseDate = db.Column(db.Date)
    Rating = db.Column(db.Integer)
    StudioID = db.Column(db.Integer, db.ForeignKey('gamestudio.StudioID'))

    studio = db.relationship("GameStudio")


class GameGenre(db.Model):
    __tablename__ = 'gamegenre'
    GenreName = db.Column(db.String(255), primary_key=True)
    GameID = db.Column(db.Integer, db.ForeignKey('game.GameID'), primary_key=True)


class PlayedOn(db.Model):
    __tablename__ = 'playedon'
    PlatID = db.Column(db.Integer, db.ForeignKey('platform.PlatID'), primary_key=True)
    GameID = db.Column(db.Integer, db.ForeignKey('game.GameID'), primary_key=True)


class Review(db.Model):
    __tablename__ = 'review'
    ReviewID = db.Column(db.Integer, primary_key=True)
    Author = db.Column(db.String(255))
    Date = db.Column(db.Date)
    Website = db.Column(db.String(255))
    Rating = db.Column(db.Integer)
    GameID = db.Column(db.Integer, db.ForeignKey('game.GameID'))

    game = db.relationship("Game")


class Achievements(db.Model):
    __tablename__ = 'achievements'
    AchievementID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Rank = db.Column(db.String(255))
    GameID = db.Column(db.Integer, db.ForeignKey('game.GameID'))

    game = db.relationship("Game")


class OnlineService(db.Model):
    __tablename__ = 'onlineservice'
    ServiceID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    CompanyID = db.Column(db.Integer, db.ForeignKey('company.CompID'))
    Tier = db.Column(db.String(255))
    MonthlyPrice = db.Column(db.Float)
    YearlyPrice = db.Column(db.Float)

    company = db.relationship("Company")


class UserAccount(db.Model):
    __tablename__ = 'useraccount'
    UserName = db.Column(db.String(255), primary_key=True)
    Password = db.Column(db.String(255))
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    Region = db.Column(db.String(255))
    OnlineServiceID = db.Column(db.Integer, db.ForeignKey('onlineservice.ServiceID'))
    DoB = db.Column(db.Date)

    service = db.relationship("OnlineService")


class Plays(db.Model):
    __tablename__ = 'plays'
    GameID = db.Column(db.Integer, db.ForeignKey('game.GameID'), primary_key=True)
    UserID = db.Column(db.String(255), db.ForeignKey('useraccount.UserName'), primary_key=True)
    OnlineServiceID = db.Column(db.Integer, db.ForeignKey('onlineservice.ServiceID'))
    Hours = db.Column(db.Float)


class DLC(db.Model):
    __tablename__ = 'dlc'
    DLCID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    GameID = db.Column(db.Integer, db.ForeignKey('game.GameID'))
    ReleaseDate = db.Column(db.Date)
    Description = db.Column(db.String(255))
    Price = db.Column(db.Float)

    game = db.relationship("Game")


class Downloaded(db.Model):
    __tablename__ = 'downloaded'
    DLCID = db.Column(db.Integer, db.ForeignKey('dlc.DLCID'), primary_key=True)
    UserName = db.Column(db.String(255), db.ForeignKey('useraccount.UserName'), primary_key=True)
