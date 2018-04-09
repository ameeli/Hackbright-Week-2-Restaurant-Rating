"""Restaurant rating lister."""

def ask_user_rating():
    new_name = raw_input ("What is a restaurant name? ")
    new_rating = raw_input ("What rating would you give this restaurant? ")

    return [new_name, new_rating]


def read_ratings(file_):
    """
    Opens and reads file and splits each line into a pair which is used in a dictionary.
    """
    rest_ratings = {}

    with open(file_) as info:
        for line in info:
            split_rest_rating = line.split(':')
            restaurant = split_rest_rating[0]
            rating = split_rest_rating[1].strip()

            rest_ratings[restaurant] = rating

        rest_ratings[user_input[0]] = user_input[1]

        return rest_ratings


def print_ratings(rest_ratings):
    """
    Takes dictionary of restaurants and rating, and prints them in alphabetical order.
    """
    sorted_rest_ratings = sorted(rest_ratings.items())

    for restaurant, rating in sorted_rest_ratings:
        print "%s is rated at %s." % (restaurant, rating)


user_input = ask_user_rating()
rest_ratings = read_ratings('scores.txt')
print_ratings(rest_ratings)
