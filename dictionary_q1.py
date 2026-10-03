# List of friends' names
friends = ["Bishnupriya", "Rajesh", "Priyambada", "Sthitipragnya", "Rohan"]

# Create a list of tuples containing name and length
friends_info = []

for name in friends:
    friends_info.append((name, len(name)))

print("List of tuples:")
print(friends_info)
