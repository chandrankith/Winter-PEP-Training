'''Question 1
sort the given dictionary based on there ages give in the input dictionary 
Input:
[{"name": "linga", "age": 30}, {"name": "Bob", "age": 25}, {"name": "churro", "age": 35}]
Output: (sorted by smallest to largest age)
[{"name": "Bob", "age": 25}, {"name": "linga", "age": 30}, {"name": "churro", "age": 35}]'''

my_data = [{"name": "linga", "age": 30}, {"name": "Bob", "age": 25}, {"name": "churro", "age": 35}]

sorted_data = sorted(my_data, key=lambda x: x["age"])

print(sorted_data)