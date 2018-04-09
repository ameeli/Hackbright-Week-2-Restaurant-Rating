"""Restaurant rating lister."""


def read_ratings(file_):
    """
    Opens and reads file and splits each line into a pair which is used in a dictionary.
    """
    rest_ratings = {}
    new_name = raw_input ("What is a restaurant name? ")
    new_rating = raw_input ("What rating would you give this restaurant? ")

    with open(file_) as info:
        for line in info:
            split_rest_rating = line.split(':')
            restaurant = split_rest_rating[0]
            rating = split_rest_rating[1].strip()

            rest_ratings[restaurant] = rating

        rest_ratings[new_name] = new_rating
        return rest_ratings


def print_ratings(rest_ratings):
    """
    Takes dictionary of restaurants and rating, and prints them in alphabetical order.
    """
    sorted_rest_ratings = sorted(rest_ratings)

    for restaurant in sorted_rest_ratings:
        print "%s is rated at %s." % (restaurant, rest_ratings[restaurant])

rest_ratings = read_ratings('scores.txt')
print_ratings(rest_ratings)
