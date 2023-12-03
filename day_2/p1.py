with open(0) as file:
    red_thresh = 12
    green_thresh = 13
    blue_thresh = 14
    inp = file.readlines()

    possible_games = 0

    for i, game in enumerate(inp):

        game_id, sets = game.split(':')

        sets = sets.strip().split(";")

        is_possible = True
        for s in sets:
            cubes = s.split(',')
            game_colors = {
                    "red": 0,
                    "blue": 0,
                    "green": 0
            }
            for cube in cubes:
                val, color = cube.strip().split(' ')
                game_colors[color] += int(val)

            i
            if (game_colors["red"] > red_thresh or
               game_colors["blue"] > blue_thresh or
                game_colors["green"] > green_thresh):
                is_possible = False

        if is_possible:
            possible_games += (i+1)

    print(possible_games)



