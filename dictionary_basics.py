#Create a dictionary called movie with three keys: "title", "director", and "year". Fill in the values with a movie of your choice, 
# and write a line of code to print out just the "director".
movie={
    "title":"Godha",
    "Director":"Basil Joseph",
    "Year":2020
}
print(movie.get("Director"))


#You have this inventory: stock = {"apples": 5, "bananas": 2}.
#Write the code to update the number of "bananas" to 12, and add a new item "oranges" with a stock of 8.
stock = {"apples": 5, "bananas": 2}
stock['bananas']=12
stock['oranges']=8
print(stock)


#You have a dictionary of test scores: grades = {"Math": 85, "Science": 92, "History": 78}.
#Write a for loop using .items() that prints out each subject and score.
grades = {"Math": 85, "Science": 92, "History": 78}
for subject,mark in grades.items():
    print(f"Mark of {subject} is {mark}")


data = "apple,apple,banana,apple,banana,orange"
print(data.split(","))
fruit_counts = {}
for word in data.split(","):
    if word in fruit_counts:
        fruit_counts[word]+=1
    else:
        fruit_counts[word]=1
print(fruit_counts)            


library = {"1984": "Checked Out", "Dune": "Available"}
print(library.get("The Hobbit"))
if 'The Hobbit' in library:
    print(" found in system")
else:
    print("Not found in system")