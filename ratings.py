"""Restaurant rating lister."""


def ask_user_rating():
    new_name = raw_input("What is a restaurant name? ")
    new_rating = int(raw_input("What rating would you give this restaurant? "))

    while new_rating not in range(1, 6):
        new_rating = int(raw_input("What rating would you give this restaurant? Please enter a number between 1 and 5! "))

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


# def ask_user_options(files_):
#     user_choice = int(raw_input('Enter 1 to see all restaurant ratings. \nEnter 2 to add your own rating. \nEnter 3 to quit. \nYour choice: '))

#     while user_choice not in range(1, 4):
#         user_choice = int(raw_input('Enter 1 to see all restaurant ratings. \nEnter 2 to add your own rating. \nEnter 3 to quit. \nYour choice: '))
  
#     if user_choice == 1:
#         rest_ratings = read_ratings(files_)
#         print_ratings(rest_ratings)

#     elif user_choice == 2:
#         user_input = ask_user_rating()
#         read_ratings('scores.txt')

#     elif user_choice == 3:
#         return


# ask_user_options('scores.txt')

# rest_ratings = read_ratings('scores.txt')
# print_ratings(rest_ratings)


while True:

    # ratings = get_ratings(sys.argv[1])

    # display(ratings)

    user_choice = int(raw_input('Enter 1 to see all restaurant ratings. \nEnter 2 to add your own rating. \nEnter 3 to quit. \nYour choice: '))

    if user_choice == 3:
        break

    elif user_choice == 1:

        rest_ratings = read_ratings('scores.txt')
        print_ratings(rest_ratings)

    elif user_choice == 2:
        ask_user_rating()

    else:
        print'not valid'


