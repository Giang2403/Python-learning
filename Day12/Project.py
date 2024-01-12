import json
USER_CHOICE = """ Enter your choice
1 - Add movie
2 - Show movies list
3 - Find movie
4 - Delete movie
5 - Update movie
6 - Quit
""" 
movies_list = []
prevs = set()


#Add movie
def add_movie():
    name = input("Enter movie's name: ").capitalize().strip()
    while name in prevs:
        print("Movie is already in list! Please enter another movie")
        name = input("Enter movie's name: ").capitalize().strip()

    prevs.add(name)
    director = input("Enter director: ").capitalize().strip()
    year = input("Enter year: ")
    movie = {
        "name": name,
        "director": director,
        "year": year
    }
    movies_list.append(movie)

def show_movies():
    if movies_list:
        for idx, movie in enumerate(movies_list, start=1):
            print(f"----Movie number {idx}----")
            print("Name: " + movie["name"])
            print("Director: " + movie["director"])
            print("Year: " + movie["year"])
    else:
        print("The movie list is empty!")

def find_movie():
    if movies_list:
        name = input("Enter movie name want to find: ").capitalize().strip()
        for idx, movie in enumerate(movies_list, start = 1):
            if name == movie["name"]:
                print(f"---Found movie number {idx}!---")
                print("Name: " + movie["name"])
                print("Director: " + movie["director"])
                print("Year: " + movie["year"])
                break
        else:
            print("Movie not found")
    else:
        print("Movie list is empty")

def del_movie():
    if movies_list:
        name = input("Enter movie want to delete: ").capitalize().strip()
        for idx, movie in enumerate(movies_list,start=1):
            if name == movie["name"]:
                movies_list.pop(idx-1)
                print("---Delete successful---")
                break
        else:
            print("Movie is not exist in the list")
    else:
        print("The movie list is empty!")

def update_movie():
    if movies_list:
        name = input("Enter movie want to update: ").capitalize().strip()
        for idx, movie in enumerate(movies_list, start=1):
            if name == movie["name"]:
                print("Enter new name: ")
                movie["name"] = input().capitalize().strip()
                print("Enter new director: ")
                movie["director"] = input().capitalize().strip()
                print("Enter new year: ")
                movie["year"] = input().capitalize().strip()
                print("---Update successful---")
                break
        else:
            print("Movie is not exist in the list")
    else:
        print("The list is empty")

operations = {
    "1": add_movie,
    "2": show_movies,
    "3": find_movie,
    "4": del_movie,
    "5": update_movie,
}

choice = input(USER_CHOICE)
while choice != "6":
    operation = operations[choice]
    operation()
    choice = input(USER_CHOICE)

    

