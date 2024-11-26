# create dictionary for book
bookDays = {}
print("\n\nEnter the book history borrwed in format: \"Book Title - Days Borrwed\"")
print("Keep the line empty and press \"Enter\" to exist.")
# sign the book title and days of borrwed
while True:
    sign = input("Enter the book Title and number of days Example( Harry - 10 ): ")
    # if not enter data stop while and display
    if not sign:  
        break
    # split title and days by " - "
    title, days = sign.split(" - ") 
    # convert days to "int" 
    days = int(days)  
    # plus the day of book title
    if title in bookDays:
        bookDays[title] += days  
    else:
        # add a book title and days borrwed
        bookDays[title] = days 
# find the max book title borrwed
mostBorrowed = max(bookDays, key=bookDays.get)
print("Most Borrwed: ", mostBorrowed)
# find the min book title borrwed
leastBorrowed = min(bookDays, key=bookDays.get)
print("Least Borrwed: ", leastBorrowed)
# find the avverage for a book title borrwed
averageDays = sum(bookDays.values()) / len(bookDays)
print("Avverage days: ", averageDays)
# print the all unique book title
uniqueTitles = set(bookDays.keys())
print("Unique Titles:", uniqueTitles)
# sort the books max to min
sortedBooks = sorted(bookDays.items(), key=lambda x: x[1], reverse=True)
print("Sorting by days from (largest to smallest)")
# print the sorted books
for book, days in sortedBooks:
    print(f"{book}: {days} Days")
