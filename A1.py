with open("your_file.txt", "r") as file:
    content = file.read()
    print("Full content of the file:\n", content)

with open("your_file.txt", "r") as file:
    print("\nFirst 10 characters:", file.read(10))

with open("your_file.txt", "r") as file:
    print("\nFirst line:", file.readline().strip())

with open("your_file.txt", "r") as file:
    print("\nFirst 4 lines:")
    for _ in range(4):
        print(file.readline().strip())

with open("your_file.txt", "r") as file:
    print("\nAll lines one by one:")
    for line in file:
        print(line.strip())