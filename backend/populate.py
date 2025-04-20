from app import db, create_app
from app.models import Company, Platform, GameStudio, Game, GameGenre, PlayedOn, Review, Achievements, OnlineService, UserAccount, Plays, DLC, Downloaded
from datetime import date
app = create_app()

with app.app_context():

    # Create Companies
    sony = Company(Name='Sony')
    microsoft = Company(Name='Microsoft')
    nintendo = Company(Name='Nintendo')
    steam = Company(Name = "Steam")
    company_list = [sony, microsoft, nintendo, steam]
    db.session.add_all(company_list)
    db.session.commit()

    # Create Platforms
    ps5 = Platform(
        Name='PlayStation 5',
        Generation=9,
        Price=499.99,
        Sales=50000000,
        CompanyID=sony.CompID,
        ReleaseDate='2020-11-12'
    )

    xbox_series_x = Platform(
        Name='Xbox Series X',
        Generation=9,
        Price=499.99,
        Sales=30000000,
        CompanyID=microsoft.CompID,
        ReleaseDate='2020-11-10'
    )

    switch = Platform(
        Name = "Nintendo Switch",
        Generation = 8,
        Price = 299.99,
        Sales = 150000000,
        CompanyID= nintendo.CompID,
        ReleaseDate = "2017-03-17",
    )

    switch2 = Platform(
        Name = "Nintendo Switch 2",
        Generation = 9,
        Price = 449.99,
        Sales = 0,
        CompanyID= nintendo.CompID,
        ReleaseDate = "2025-06-05",
    )

    ps4 = Platform(
        Name = "PlayStation 4",
        Generation = 8,
        Price = 175.00,
        Sales = 117000000,
        CompanyID= sony.CompID,
        ReleaseDate = "2013-11-15",
    )

    steam_player = Platform(
        Name = "Steam/PC",
        Generation = 9,
        Price = 0,
        Sales = 0,
        CompanyID= steam.CompID,
        ReleaseDate = "2003-09-12",
    )

    platform_list = [ps5, xbox_series_x, switch, switch2, ps4, steam_player]

    db.session.add_all(platform_list)
    db.session.commit()

    # Create Game Studio
    santa_monica = GameStudio(Name='Santa Monica Studio', Location='USA')
    ubisoft = GameStudio(Name = "Ubisoft", Location = "Canada")
    nintendo_epd = GameStudio(Name = "Nintendo(EPD)", Location = "Japan")
    bandai = GameStudio(Name = "Bandai Namco", Location = "Japan")
    spike_chunsoft = GameStudio(Name = "Spike Chunsoft", Location = "Japan")
    toby_fox = GameStudio(Name='Toby Fox', Location='USA')
    ninja_kiwi = GameStudio(Name='Ninja Kiwi', Location='New Zealand')
    blue_mammoth = GameStudio(Name='Blue Mammoth Games', Location='USA')
    three_four_three = GameStudio(Name='343 Industries', Location='USA')
    insomniac = GameStudio(Name='Insomniac Games', Location='USA')
    atlus = GameStudio(Name='Atlus', Location='Japan')
    sonic_team = GameStudio(Name='Sonic Team', Location='Japan')
    epic_games = GameStudio(Name='Epic Games', Location='USA')
    mojang = GameStudio(Name='Mojang', Location='Sweden')
    naughty_dog = GameStudio(Name = "Naughty Dog", Location = "USA")

    studio_list = [santa_monica, nintendo_epd, bandai, spike_chunsoft, toby_fox, ninja_kiwi,
        blue_mammoth, three_four_three, insomniac, atlus, sonic_team,
        epic_games, mojang, naughty_dog]
    db.session.add_all(studio_list)
    db.session.commit()

    # Create Game
    gow_ragnarok = Game(
        Name='God of War: Ragnarok',
        Price=69.99,
        ReleaseDate='2022-11-09',
        Rating=9,
        StudioID=santa_monica.StudioID
    )

    botw = Game(
        Name='The Legend of Zelda: Breath of the Wild',
        Price=59.99,
        ReleaseDate=date(2017, 3, 3),
        Rating=10,
        StudioID=nintendo_epd.StudioID
    )

    totk = Game(
        Name='The Legend of Zelda: Tears of the Kingdom',
        Price=69.99,
        ReleaseDate=date(2023, 5, 12),
        Rating=10,
        StudioID=nintendo_epd.StudioID
    )

    tekken8 = Game(
        Name='Tekken 8',
        Price=69.99,
        ReleaseDate=date(2024, 1, 26),
        Rating=9,
        StudioID=bandai.StudioID
    )

    dbsk = Game(
        Name='Dragon Ball: Sparking! Zero',
        Price=69.99,
        ReleaseDate=date(2024, 10, 11),
        Rating=9,
        StudioID= spike_chunsoft.StudioID
    )

    tlou_part1 = Game(
        Name='The Last of Us Part I',
        Price=69.99,
        ReleaseDate=date(2022, 9, 2),
        Rating=9,
        StudioID=naughty_dog.StudioID
    )

    mario_odyssey = Game(
        Name='Super Mario Odyssey',
        Price=59.99,
        ReleaseDate=date(2017, 10, 27),
        Rating=10,
        StudioID=nintendo_epd.StudioID
    )

    mario_kart8 = Game(
        Name='Mario Kart 8 Deluxe',
        Price=59.99,
        ReleaseDate=date(2017, 4, 28),
        Rating=9,
        StudioID=nintendo_epd.StudioID
    )

    undertale = Game(
        Name='Undertale',
        Price=14.99,
        ReleaseDate=date(2015, 9, 15),
        Rating=9,
        StudioID=toby_fox.StudioID
    )

    bloons_td6 = Game(
        Name='Bloons TD 6',
        Price=9.99,
        ReleaseDate=date(2018, 6, 13),
        Rating=9,
        StudioID=ninja_kiwi.StudioID
    )

    brawlhalla = Game(
        Name='Brawlhalla',
        Price=0.00,
        ReleaseDate=date(2017, 10, 17),
        Rating=8,
        StudioID=blue_mammoth.StudioID
    )

    smash_ultimate = Game(
        Name='Super Smash Bros. Ultimate',
        Price=59.99,
        ReleaseDate=date(2018, 12, 7),
        Rating=10,
        StudioID=nintendo_epd.StudioID
    )

    halo = Game(
        Name='Halo Infinite',
        Price=59.99,
        ReleaseDate=date(2021, 12, 8),
        Rating=8,
        StudioID=three_four_three.StudioID
    )

    spiderman2 = Game(
        Name='Marvel\'s Spider-Man 2',
        Price=69.99,
        ReleaseDate=date(2023, 10, 20),
        Rating=9,
        StudioID= insomniac.StudioID
    )

    persona5 = Game(
        Name='Persona 5 Royal',
        Price=59.99,
        ReleaseDate=date(2020, 3, 31),
        Rating=10,
        StudioID=atlus.StudioID
    )

    sonic_frontiers = Game(
        Name='Sonic Frontiers',
        Price=59.99,
        ReleaseDate=date(2022, 11, 8),
        Rating=7,
        StudioID=sonic_team.StudioID
    )

    fortnite = Game(
        Name='Fortnite',
        Price=0.00,
        ReleaseDate=date(2017, 7, 21),
        Rating=8,
        StudioID=epic_games.StudioID
    )

    minecraft = Game(
        Name='Minecraft',
        Price=26.95,
        ReleaseDate=date(2011, 11, 18),
        Rating=10,
        StudioID=mojang.StudioID
    )

    games_list = [
        gow_ragnarok, botw, totk, tekken8, dbsk, tlou_part1,
        mario_odyssey, mario_kart8, undertale, bloons_td6,
        brawlhalla, smash_ultimate, halo, spiderman2, persona5,
        sonic_frontiers, fortnite, minecraft
    ]
    db.session.add_all(games_list)
    db.session.commit()

    played_on_records = []

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=gow_ragnarok.GameID) for platform in [ps4, ps5, steam_player]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=botw.GameID) for platform in [switch, switch2]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=totk.GameID) for platform in [switch, switch2]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=tekken8.GameID) for platform in [ps5, steam_player, xbox_series_x]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=dbsk.GameID) for platform in [ps5, steam_player, xbox_series_x]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=tlou_part1.GameID) for platform in [ps5, steam_player]]

    played_on_records.append(PlayedOn(PlatID=switch.PlatID, GameID=mario_odyssey.GameID))

    played_on_records.append(PlayedOn(PlatID=switch.PlatID, GameID=mario_kart8.GameID))

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=undertale.GameID) for platform in [ps4, ps5, steam_player, switch, xbox_series_x]]

    played_on_records.append(PlayedOn(PlatID=steam_player.PlatID, GameID=bloons_td6.GameID))

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=brawlhalla.GameID) for platform in [ps4, steam_player, switch, xbox_series_x]]

    played_on_records.append(PlayedOn(PlatID=switch.PlatID, GameID=smash_ultimate.GameID))

    played_on_records.append(PlayedOn(PlatID=xbox_series_x.PlatID, GameID=halo.GameID))

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=spiderman2.GameID) for platform in [ps5, steam_player]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=persona5.GameID) for platform in [ps4, ps5, steam_player, switch, xbox_series_x]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=sonic_frontiers.GameID) for platform in [ps4, ps5, steam_player, switch, xbox_series_x]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=fortnite.GameID) for platform in [ps4, ps5, steam_player, switch, xbox_series_x]]

    played_on_records += [PlayedOn(PlatID=platform.PlatID, GameID=minecraft.GameID) for platform in [ps4, ps5, steam_player, switch, xbox_series_x]]

    db.session.add_all(played_on_records)
    db.session.commit()

    print("Database seeded successfully!")