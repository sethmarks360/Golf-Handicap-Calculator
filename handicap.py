"""
Handicap calculator

The handicap index is representative of a golfer's potential ability
"""

# The course rating is derived from the scores of scratch golfers

# The slope rating (or just slope) is found by comparing the course rating
# to the bogey rating

"""
Calculates the differential for a single round by one golfer
"""
def calculate_differential(strokes, course_rating, slope_rating):

        d = ((strokes - course_rating) * 113) / slope_rating

        d = round(d, 1)

        return d

"""
Calculates all differentials for a single golfer
"""
def calculate_all_differentials(list_of_rounds):

    differential_list = []

    for game in list_of_rounds:

        diff = calculate_differential(game[0], game[2], game[1])

        differential_list.append(diff)

    return differential_list

def calculate_course_handicap(index, slope_rating):

    return round((index * slope_rating / 113))

"""
This function returns the amount of scores to be used to calculate a player's index
"""
def calculate_round_count(amount_of_scores):

    score_dict = {6: 1, 7: 2, 8: 2, 9: 3, 10: 3, 11: 4, 12: 4, 
                13: 5, 14: 5, 15: 6, 16: 6, 17: 7, 18: 8, 19: 9, 20: 10}

    if amount_of_scores < 5:

        print("You need to enter 5 or more scores.")
        return -99

    elif 5 < amount_of_scores < 20:

        return score_dict[amount_of_scores]

    elif amount_of_score >= 20:

        return 10



def find_x_min(my_list, x):
    
    mins = []
    i = 0

    while i < len(my_list):

        num = min(my_list)

        mins.append(num)

        my_list.remove(num)

        i += 1

    return mins


def main():

    player_round_stats = []

    #=======ENTER SCORES HERE=======
    # Format is score, slope, rating
    rounds = [[93, 134, 73.0],
        [95, 129, 71.1],
        [83, 122, 72.1],
        [94, 134, 73.0],
        [94, 138, 73.5],
        [85, 123, 69.1],
        [90, 128, 72.1],
        [85, 124, 70.3], 
        [79, 124, 70.3],
        [86, 124, 70.3],
        [83, 124, 70.3],
        [75, 124, 70.3],
        [83, 127, 71.0]]


    player_differentials = calculate_all_differentials(rounds)

    for x in range(len(player_differentials)):

        rounds[x].append(player_differentials[x]) # Add the differential to the round list

    for x in range(len(rounds)):
        player_round_stats.append(rounds[x])
    

    amount_of_scores = calculate_round_count(len(player_round_stats))

    print("\n", "YOUR ROUND".center('=', 30))

    for game in player_round_stats:

        print("SCORE: " + str(game[0]) + " | SLOPE: " + str(game[1]) + " | RATING: " + str(game[2]) + " | DIFFERENTIAL: " + str(game[3]))

    print("\nYour index will be calculated using your lowest (" + str(amount_of_scores) + ") differentials:\n")

    lowest_diffs = find_x_min(player_differentials, amount_of_scores)

    total = 0

    for x in range(amount_of_scores):

       print(lowest_diffs[x])
       total += lowest_diffs[x]

    total = total / amount_of_scores # Find average to get Index

    total = total * .96

    print("\nYour Handicap Index is", round(total, 1), "\n")
    


if __name__ == '__main__':

    main()