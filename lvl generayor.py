import json

info = [("PLANE'S", 100, 250, 25, True), ("PLANS", 100, 250, 125, True), ("LEVEL        SCORE", 25, 275, 225, True),
        ["1. FIRSTBLOOD        000000", 25, 225, 250, True],
        ["2. CITYSIEGE        000000", 25, 225, 275, False],
        ["3. MARATHON       000000", 25, 225, 300, False],
        ["4. MANHUNT       000000", 25, 225, 325, False],
        ["5. ESCAPE       000000", 25, 225, 350, False],
        ["6. EVERGONE       000000", 25, 225, 375, False],
        ["7. THE_END      000000", 25, 225, 400, False], ["PRESS F TO START", 25, 275, 700, True]]
with open("data/menu_list.json", "w") as s:
    json.dump(info, s)
# "EnemyPawn(-30,50,2,2)"
# "EnemyPawn(500,50,-2,2)"
# "EnemyPawn(-20,-30,0,3)"
# "EnemyKnight(250,200)"
# "EnemyKnight(125,100)"
# "EnemyKnight(125,400)"
lvls_info = [[3400, {"1": "Background(\"data/sprites/background/ship.png\", -214,3400)",
                     "0": " Background('data/sprites/background/see.jpg', -16420, 3500)",
                     "202": "EnemyPawn(-30,50,2,2)",
                     "203": "EnemyPawn(500,50,-2,2)",
                     "204": "EnemyPawn(275,-30,0,3)",
                     "205": "EnemyPawn(225,-30,0,3)",
                     "256": "EnemyKnight(250,200)",
                     "257": "EnemyKnight(125,100)",
                     "258": "EnemyKnight(125,400)",

                     "300": "Background(\"data/sprites/background/city.png\", -4000,3100)",
                     "402": "EnemyBishop(125)",
                     "456": "EnemyKnight(250,200)",
                     "457": "EnemyKnight(125,100)",

                     "602": "EnemyBishop(250)",
                     "656": "EnemyKnight(250,200)",
                     "657": "EnemyKnight(125,100)",
                     "802": "EnemyBishop(125)",
                     "856": "EnemyKnight(250,200)",
                     "857": "EnemyKnight(125,100)",
                     "1002": "EnemyBishop(250)",
                     "1056": "EnemyKnight(250,200)",
                     "1057": "EnemyKnight(125,100)",
                     "1202": "EnemyBishop(125)",
                     "1302": "EnemyPawn(-30,50,2,2)",
                     "1303": "EnemyPawn(500,50,-2,2)",
                     "1304": "EnemyPawn(275,-30,0,3)",
                     "1305": "EnemyPawn(225,-30,0,3)",
                     "1500": "Background(\"data/sprites/background/oasis.png\", -3266,3100)",
                     "1602": "EnemyKing()",
                     "1802": "EnemyBishop(250)",
                     "2002": "EnemyBishop(125)",
                     "2202": "EnemyBishop(250)",
                     "2402": "EnemyBishop(125)",
                     "2602": "EnemyBishop(250)",
                     "2802": "EnemyBishop(125)",
                     "3002": "EnemyBishop(250)",
                     "3202": "EnemyBishop(125)",

                     "3400": "Background(\"data/sprites/background/ship.png\", -1014,3500)"}],
             [3400, {"1": "Background(\"data/sprites/background/ship.png\", -214,3400)",
                     "0": " Background('data/sprites/background/see.jpg', -16420, 3500)",
                     "202": "EnemyPawn(-30,50,2,2)",
                     "203": "EnemyPawn(500,50,-2,2)",
                     "204": "EnemyPawn(275,-30,0,3)",
                     "205": "EnemyPawn(225,-30,0,3)",
                     "206": "EnemyKnight(250,200)",
                     "207": "EnemyKnight(125,100)",
                     "208": "EnemyKnight(125,400)",

                     "300": "Background(\"data/sprites/background/city.png\", -4000,3100)",
                     "402": "EnemyBishop(125)",

                     "602": "EnemyBishop(250)",
                     "802": "EnemyBishop(125)",
                     "1002": "EnemyBishop(250)",
                     "1202": "EnemyBishop(125)",
                     "1500": "Background(\"data/sprites/background/oasis.png\", -3266,3100)",
                     "1602": "EnemyKing()",
                     "1802": "EnemyBishop(250)",
                     "2002": "EnemyBishop(125)",
                     "2202": "EnemyBishop(250)",
                     "2402": "EnemyBishop(125)",
                     "2602": "EnemyBishop(250)",
                     "2802": "EnemyBishop(125)",
                     "3002": "EnemyBishop(250)",
                     "3202": "EnemyBishop(125)",

                     "3400": "Background(\"data/sprites/background/ship.png\", -1014,3500)"}]
             ]
with open("data/lvls_info.json", "w") as fileone:
    json.dump(lvls_info, fileone)
