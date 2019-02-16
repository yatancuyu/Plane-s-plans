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
lvls_info = [[2300, {"1": "Background(\"data/sprites/background/ship.png\", -214,2400)",
                     "0": " Background('data/sprites/background/see.jpg', -16420, 2400)",

                     "200": "EnemyKnight(100, 100)",
                     "201": "EnemyKnight(200, 167)",
                     "202": "EnemyKnight(300, 246)",
                     "203": "EnemyKnight(400, 127)",
                     "204": "EnemyKnight(450, 300)",

                     "300": "Background(\"data/sprites/background/island.png\", -3266,2400)",

                     "400": "EnemyKnight(100, 100)",
                     "401": "EnemyBishop(100)",
                     "410": "EnemyPawn(0,50,2,3)",
                     "415": "EnemyPawn(0,150,2,3)",
                     "420": "EnemyPawn(0,250,2,3)",
                     "422": "EnemyPawn(0,350,2,3)",
                     "430": "EnemyKnight(450, 300)",
                     "432": "EnemyKnight(200, 167)",
                     "402": "EnemyKnight(300, 246)",
                     "403": "EnemyKnight(400, 127)",
                     "404": "EnemyKnight(450, 300)",
                     "2300": "Background(\"data/sprites/background/ship.png\", -1014,2400)"}]]
with open("data/lvls_info.json", "w") as fileone:
    json.dump(lvls_info, fileone)
