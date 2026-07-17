books = []

totalbooks = int(input("Enter the number of books: "))

for i in range(totalbooks):
    book = input(f"Book {i+1} title: ")
    books.append(book)
  
print("Collection of books: ")
for num,book in enumerate(books, start=1):
    print(f"{num}.{book}")
    
print("Total number of books: ", len(books))
print("First book in the collection: ", books[0])
print("Last book in the collection:", books[-1])
    
    