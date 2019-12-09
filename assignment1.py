''' Name: Nguyen Hoang Ba Han
Date: 09/12/2019
Program: Update movie list
GitHub URL: https://github.com/JCUS-CP1404/assignment-01-NguyenHan123-Aston/edit/master/assignment1.py'''


'''opening the movies.csv file at the start and assigning it to a global variable (FILES) for the 4 functions of menu(),list(),add(),and watch() to use.
Global lists are added are to be used to store universal values to be used by the 4 functions of menu(),list(),add(),and watch() below.'''
input_file = open("movies.csv", "r")
FILES = input_file.readlines()
TOTAL = [0]
REMAINDER = [1]
EXPORT_LIST = []

'''main() function serves the purpose of only displaying the intial message,and then moving forward directly to the menu() function'''
def main():
    print("Movies To Watch 1.0 - by Nguyen Han")
    first = menu()

'''menu() function displayes the three main options of the program for user to access the three main fucntions (L - List, A - Add, W - Watch, and Q - Quit)
The Q - Quit option allows the user to see the total number of movies they have saved or/and input in the song list to the csv file itself, overwrting it in the process '''
def menu():
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")
    option = input(">>> ").upper()
    print("-" * 86)
    while option not in ['L', 'A', 'W', 'Q']:
        option = input("Invalid input, please re-input").upper()
    if option == "L":
        list()
    elif option == "A":
        add()
    elif option == "W":
        watch()
    else:
        confirm = input("Are you sure you want to quit? - (Y) Yes, (N) No ").upper()
        while confirm not in ['Y', 'N']:
            confirm = input("Invalid, please re-input appropriate option").upper()
        if confirm == "Y":
            with open("movies.csv", "w") as input_file:
                for item in FILES:
                    input_file.write("{}".format(item))
            print("=> Updates to your playlist has been saved")
            print("-- Exited playlist --")
            quit()
        else:
            menu()

'''list functions displays all the values from the movies.csv files (all stored in the FILES variable created above instead of having to directly access the csv file itself) in a neatly organized format at any point within the program, whether its before or after more data is inputed into the movies.csv file'''
def list():
    list = []
    count = 0
    count_1 = 0
    for spaces in FILES:
        count += 1
        next_spaces = spaces.split(",")
        movie_name = next_spaces[0]
        year_show = next_spaces[1]
        category_movie = next_spaces[2]
        status = next_spaces[3].replace("y", "u").replace("n", "w").replace("\n", "")
        list.append(count)
        result_movies_list = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, status, movie_name, year_show, category_movie))
        print(result_movies_list)
        if "w" in status:
            count_1 += 1
    print("-" * 86)
    print("Total number of movies:", max(list))
    TOTAL.append(max(list))
    print("Number of movies watched:", max(list) - count_1)
    print("Number of movies still to watch:", count_1)
    REMAINDER.append(count_1)
    print("-" * 86)
    menu()

'''add function serves the purpose of allowing the user to add data to the FILES varible which would be printed and formatted appropriately in the list() function'''
def add():
    remove_status = "y\n"
    movie_name_input = input("Title:")
    while movie_name_input in [""," ","  ","   "]:
        print("Title: ")
        movie_name_input = input("Title: ")
    category_input = input("Category: ")
    flag = True
    while (flag == True):
        try:
            year_show_input = int(input("Year: "))
            flag = False
        except ValueError:
            print("Invalid input; please enter a number")
    while len(str(year_show_input)) <= 0:
        print("Number must be >=0")
        year_show_input = int(input("Year:"))
    while category_input in ["", " ","   ", "   "]:
        print("Category: ")
        category_input = input("Category: ")
    if REMAINDER[-1] == 0:
        REMAINDER.remove(REMAINDER[-1])
    result_1 = ("{},{},{},{}".format(movie_name_input, year_show_input, category_input,remove_status))
    FILES.append(result_1)
    EXPORT_LIST.append(result_1)
    print("{} by {} from ({}) added to movie list".format(movie_name_input, year_show_input, category_input))
    print("-" * 86)
    menu()

'''the watch() function serves the purpose of allowing the user to mark the data or movies within the list as finished'''
def watch():
    remove_status = "n\n"
    if min(REMAINDER) == 0:
        print("No more movies to watch!")
        print("-" * 86)
        menu()
    flag=True
    while (flag==True):
        try:
            number = int(input("Enter the number of a movie to mark as watched"))
            flag=False
        except ValueError:
            print("Invalid input, please enter a number")
    if max(TOTAL) == 0:
        print("Please first load list and then proceed to input movie number value")
        menu()
    while number > max(TOTAL):
        print("Error, please re-input appropriate value")
        number = int(input("Enter the number of a movie to mark as watched"))
    rows = FILES[number - 1]
    new_rows = rows.split(",")
    movie_name3 = new_rows[0]
    category_name = new_rows[1]
    year_movie = new_rows[2]
    result_3 = ("{},{},{},{}".format(movie_name3, category_name, year_movie,remove_status))
    result_4 = ("=> '{} by {} from {}' learnt".format(movie_name3, category_name, year_movie))
    FILES.append(result_3)
    FILES.remove(FILES[number - 1])
    print(result_4)
    print("-" * 86)
    menu()

main()
