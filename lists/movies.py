movies = []

totalmovies = int(input("Enter the number of movies: "))

for i in range(totalmovies):
    movie = input(f"Movie title {i+1}: ")
    movies.append(movie)
    
print("\nFavorite Movies:")
for num, movie in enumerate(movies, start=1):
    print(f"{num}. {movie}")
    
print("\nTotal movies: ", len(movies))
print("First movie: ", movies[0])
print("Last movie: ", movies[-1])
    
view = int(input("\nEnter the number of the movie you want to view: "))

if 1 <=view <=len(movies):
    print(f"You selected: {movies[view-1]}")
else:
    print("Please enter a valid number.")




