numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
sum_of_numbers = sum(numbers)
print("Sum of the integers:", sum_of_numbers)


favorite_books = ("Master your emotions", "Women who run with the wolves", "The War of Art", "7 Habits of highly effective people", "Atomic Habits")
print("Favorite Books:")
for book in favorite_books:
    print(book)


person_info = {}
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")
person_info['favourite_country'] = input("Enter your favorite country: ")
person_info['favorite food'] = input("Enter your favorite food")
print("Person Information:", person_info)


set1 = set(input("Enter integers for set 1 separated by spaces: ").split())
set2 = set(input("Enter integers for set 2 separated by spaces: ").split())
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)


words = ["apple", "banana", "orange", "grape", "kiwi"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
