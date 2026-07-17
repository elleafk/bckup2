months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print("Months of the Year:")
for num,month in enumerate(months, start=1):
    print(f"{num}. {month}")

print("\nTotal numbers of month: ", len(months))
print("First month: ", months[0])
print("Last month: ",months[-1])

selected = int(input("\nEnter a month number: "))

if 1<= selected <=len(months):
    print("You selected: ", months[selected-1])
else:
    print("Invalid number")
    