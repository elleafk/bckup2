zodiacs = ("Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces")

print("Zodiac signs:")
for num,zodiac in enumerate(zodiacs, start=1):
    print(f"{num}. {zodiac}")
    
print("\nTotal number of zodiac signs: ", len(zodiacs))
print("First zodiac sign: ", zodiacs[0])
print("Last zodiac sign: ", zodiacs[-1])

def selection():
    selected = int(input("\nEnter a zodiac number: "))

    if 1 <= selected <= len(zodiacs):
        print("\nYou selected: ", zodiacs[selected-1])
    else:
        print("Invalid number")

selection()

while True:
    choose = input("\nDo you want to choose again? (Y/N): ")

    if choose.upper() == "Y":
        selection()
    elif choose.upper() == "N":
        break
    else:
        print("Enter Y or N only.")