import random

# Generate a random list of size between 20 and 40
random_list_size = random.randint(20, 40)
random_list = [random.randint(0, 40) for _ in range(random_list_size)]

# Create a second list with "some elements" from the first list and "-" symbols
second_list = []
for i in range(random_list_size):
    if i < 2:
        second_list.append('-')
    elif random_list[i] > random_list[i - 1] and random_list[i] > random_list[i - 2] and random_list[i - 1] > random_list[i - 2]:
        second_list.append(random_list[i])
    else:
        second_list.append('-')

# Print the original list
print("Original list:", random_list)
# Print the modified list
print("Modified list:", second_list)