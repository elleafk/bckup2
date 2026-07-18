fruits1 = {"Apple", "Banana", "Orange", "Mango"}
fruits2 = {"Banana", "Mango", "Grapes", "Watermelon"}

union = fruits1 | fruits2
print("\nUnion: ",union)
intersection = fruits1 & fruits2
print("\nIntersection: ", intersection)
difference = fruits1 - fruits2
print("\nDifference: ",difference)
symmetricDifference = fruits1 ^ fruits2
print("\nSymmetric Difference: ", symmetricDifference)