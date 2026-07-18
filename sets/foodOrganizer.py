favFoods = set()

totalFavFoods = int(input("Enter the number of your favorite foods: "))

for i in range(totalFavFoods):
    favFood = input(f"Favorite {i+1}: ")
    favFoods.add(favFood)
    
print("\nFavorite Foods: ")
for foods in favFoods:
    print (foods)

print("\nTotal unique foods: ", len(favFoods))

    