from collections import Counter

votes = []

v = int(input("Enter the number of voters: "))

for i in range(v):
    vote = input(f"Enter the name of candidate {i+1}: ")
    votes.append(vote)
    
counter = Counter(votes)
highest = max(counter.values())
winner = []

for candidate, count in counter.items():
    if count == highest:
        winner.append(candidate)
        
if len(winner) == 1:
    print("\nWinner: ", winner[0])
else:
    print("\nIt's a tie between: ",", ".join(winner))