"""Restaurant rating lister."""
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

        return rest_ratings


def print_ratings(file_):
    """
    Takes dictionary of restaurants and rating, and prints them in alphabetical order.
    """
    rest_ratings = read_ratings(file_)
    sorted_rest_ratings = sorted(rest_ratings)

    for item in sorted_rest_ratings:
        print "%s is rated at %s." % (item, rest_ratings[item])

print_ratings('scores.txt')


