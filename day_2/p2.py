import math

with open(0) as file:
    red_thresh = 12
    green_thresh = 13
    blue_thresh = 14
    inp = file.readlines()

    possible_games = 0

    power_sum = 0

    for i, game in enumerate(inp):

        game_id, sets = game.split(':')

        sets = sets.strip().split(";")

        is_possible = True

        game_colors = {
                "red": 0,
                "blue": 0,
                "green": 0
        }

        for s in sets:
            cubes = s.split(',')
            for cube in cubes:
                val, color = cube.strip().split(' ')
                # game_colors[color] += int(val)
                game_colors[color] = max(int(val), game_colors[color])


        power_sum += math.prod(game_colors.values())

    print(power_sum)



