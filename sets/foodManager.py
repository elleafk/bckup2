foods = set()

totalFoods = int(input("Enter the number of the foods: "))

for i in range(totalFoods):
    food = input(f"Food number {i+1}: ")
    foods.add(food)
    
print("\nFood Collection: ")
for food in foods:
    print(food)
    
removeFood = input("\nEnter a food to remove: ")
foods.discard(removeFood)
addFood = input("Enter a food to add: ")
foods.add(addFood)

print("\nTotal unique numbers of food: ", len(foods))
print("\nFinal Collections of food: ")
for food in foods:
    print(food)


