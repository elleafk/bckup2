foods = set()

totalFoods = int(input("Enter the number of the foods: "))

for i in range(totalFoods):
    food = input(f"Food number {i+1}: ")
    foods.add(food)
    
print("\nFood Collection: ")
for food in foods:
    print(food)
    
remove = input("\nEnter a food to remove: ")
foods.discard(remove)
add = input("Enter a food to add: ")
foods.add(add)

print("\nTotal unique numbers of food: ", len(foods))
print("Final Collections of food: ")
for finalfood in foods:
    print(finalfood)


