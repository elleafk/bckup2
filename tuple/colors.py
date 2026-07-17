colors = ("Red", "Blue", "Green", "Yellow", "Purple")

print("Collection of Colors:")
for num,color in enumerate(colors, start=1):
    print(f"{num}. {color}")
    
print("\nTotal numbers of colors: ", len(colors))
print("First color: ", colors[0])
print("Last color: ", colors[-1])
    
index = int(input("\nEnter a color number: "))

if 1<= index <= len(colors):
    print("You selected: ", colors[index-1])
else:
    print("invalid input")