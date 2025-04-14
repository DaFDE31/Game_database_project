from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


Company, Platform, GameStudio, Game, GameGenre, PlayedOn, Review, Achievements, OnlineService, UserAccount, Plays, DLC, Downloaded

class Company(Base):
    __tablename__ = 'company'
    CompID = Column(Integer, primary_key=True)
    Name = Column(String)


class Platform(Base):
    __tablename__ = 'platform'
    PlatID = Column(Integer, primary_key=True)
    Name = Column(String)
    Generation = Column(Integer)
    Price = Column(Float)
    Sales = Column(Integer)
    CompanyID = Column(Integer, ForeignKey('company.CompID'))
    ReleaseDate = Column(Date)

    company = relationship("Company")


class GameStudio(Base):
    __tablename__ = 'gamestudio'
    StudioID = Column(Integer, primary_key=True)
    Name = Column(String)
    Location = Column(String)


class Game(Base):
    __tablename__ = 'game'
    GameID = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Float)
    ReleaseDate = Column(Date)
    Rating = Column(Integer)
    StudioID = Column(Integer, ForeignKey('gamestudio.StudioID'))

    studio = relationship("GameStudio")


class GameGenre(Base):
    __tablename__ = 'gamegenre'
    GenreName = Column(String, primary_key=True)
    GameID = Column(Integer, ForeignKey('game.GameID'), primary_key=True)


class PlayedOn(Base):
    __tablename__ = 'playedon'
    PlatID = Column(Integer, ForeignKey('platform.PlatID'), primary_key=True)
    GameID = Column(Integer, ForeignKey('game.GameID'), primary_key=True)


class Review(Base):
    __tablename__ = 'review'
    ReviewID = Column(Integer, primary_key=True)
    Author = Column(String)
    Date = Column(Date)
    Website = Column(String)
    Rating = Column(Integer)
    GameID = Column(Integer, ForeignKey('game.GameID'))

    game = relationship("Game")


class Achievements(Base):
    __tablename__ = 'achievements'
    AchievementID = Column(Integer, primary_key=True)
    Name = Column(String)
    Rank = Column(String)
    GameID = Column(Integer, ForeignKey('game.GameID'))

    game = relationship("Game")


class OnlineService(Base):
    __tablename__ = 'onlineservice'
    ServiceID = Column(Integer, primary_key=True)
    Name = Column(String)
    CompanyID = Column(Integer, ForeignKey('company.CompID'))
    Tier = Column(String)
    MonthlyPrice = Column(Float)
    YearlyPrice = Column(Float)

    company = relationship("Company")


class UserAccount(Base):
    __tablename__ = 'useraccount'
    UserName = Column(String, primary_key=True)
    Password = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    Region = Column(String)
    OnlineServiceID = Column(Integer, ForeignKey('onlineservice.ServiceID'))
    DoB = Column(Date)

    service = relationship("OnlineService")


class Plays(Base):
    __tablename__ = 'plays'
    GameID = Column(Integer, ForeignKey('game.GameID'), primary_key=True)
    UserID = Column(String, ForeignKey('useraccount.UserName'), primary_key=True)
    OnlineServiceID = Column(Integer, ForeignKey('onlineservice.ServiceID'))
    Hours = Column(Float)


class DLC(Base):
    __tablename__ = 'dlc'
    DLCID = Column(Integer, primary_key=True)
    Name = Column(String)
    GameID = Column(Integer, ForeignKey('game.GameID'))
    ReleaseDate = Column(Date)
    Description = Column(String)
    Price = Column(Float)

    game = relationship("Game")


class Downloaded(Base):
    __tablename__ = 'downloaded'
    DLCID = Column(Integer, ForeignKey('dlc.DLCID'), primary_key=True)
    UserName = Column(String, ForeignKey('useraccount.UserName'), primary_key=True)