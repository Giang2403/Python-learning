#1 Create a movie list
movie_list = ["Doraemon",
              "Conan",
              "Oppenheimer",
              "Gió",
              "Avenger"]

#2 Use input function to add a new movie
new_movie = input("Enter new movie: ")

#3 Add new movie to the end of the list
movie_list.append(new_movie)

#4 Print the first, last, and middle movie of the list
print(f"The first movie: {movie_list[0]}")
print(f"The last movie: {movie_list[-1]}")
count=len(movie_list)
print(f"The middle movie: {movie_list[count//2]}")

#5 Print the number of movies
print(count)

#6 Delete the first and the last movie
del movie_list[0]
del movie_list[count-2]
print(movie_list)

#7 Pop out the last movie
print(movie_list.pop())

#8 Insert a new movie at the begining of the list
movie_list.insert(0,"Harry Potter")
print(movie_list)

#9 Count number of "One Piece"
print(movie_list.count("One Piece"))

#10 Find the index of "Gió"
index = movie_list.index("Gió")
print(f"The index of Gió is: {index}")

#11 Add a new list to the end of the old list
movie_list.extend(["Go",
                    "Stay",
                    "Leave"])
print(movie_list)