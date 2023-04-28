file = open("basic.txt", "w")

file.write("Hello Python Programming...!\n")

file.close()

with open("basic.txt", "a") as file:
    file.write("#2Hello Python Programming...!")