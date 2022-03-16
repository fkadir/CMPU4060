# Week 7 Lab 12 Q6

def main():
    f = open('movie_list.txt', 'r')
    movie_dict = {}
    for line in f:
        create_movie_dict(line, movie_dict)

    print(compare_movies(movie_dict))


def create_movie_dict(line, movie_dict):
    rl = line.strip().lower().split(',')
    a = rl[0]  # actor name

    # looping through movies and adding them to dictionary
    for x in range(1, len(rl)):
        l = rl[x].split('(')
        l[0] = l[0].strip()  # strip movie name of spaces
        l[1] = l[1].replace(')', '', 1)
        m = (l[0], l[1])  # movie name, date
        if m in movie_dict:
            movie_dict[m].add(a)
        else:
            set_a = {a}
            movie_dict[m] = set_a  # assign key to be movie name
    f1 = open('movie_dict.txt', 'w')
    f1.write(str(movie_dict))
    f1.close()


def compare_movies(movie_db):
    compare = input('Insert your movie comparison here (insert help if unclear): ')
    if input == 'help':
        compare = input('input comparison such as: movie title (year) comparison movie title (year): ')
    while True:
        try:
            compare = compare.strip().lower()
            # l = two strings of the movie and year together
            if '&' in compare:
                l = compare.split('&')
                comparison = '&'
            elif '|' in compare:
                l = compare.split('|')
                comparison = '|'
            elif '-' in compare:
                l = compare.split('-')
                comparison = '-'
            else:
                raise ValueError("invalid comparison")
        except ValueError:
            compare = input('Insert your correct movie comparison here: ')
        else:
            break
    # split l string into movie name and year separated
    mn1, d1 = l[0].split('(')
    mn2, d2 = l[1].split('(')
    # refine strings
    mn1, mn2 = mn1.strip(), mn2.strip()
    d1, d2 = d1.replace(')', '', 1).strip(), d2.replace(')', '', 1).strip()
    # create tuples consisting of (movie name, year)
    m1, m2 = (mn1, d1), (mn2, d2)

    # I
    if comparison == '|':
        actors_result = movie_db[m1] | movie_db[m2]
    # II
    elif comparison == '&':
        actors_result = movie_db[m1] & movie_db[m2]
    # III
    elif comparison == '-':
        actors_result = movie_db[m1] ^ movie_db[m2]

    # check if result set is empty
    if len(actors_result) == 0:
        return "No Actors Found"
    else:
        return actors_result


main()
