with open("output.txt","wt") as data:
    text = input("Enter text to write to the file: ")
    data.write(text)
    print("Data successfully written to 'output.txt'\n")

with open("output.txt","at") as data:
    add_text=input("Enter additional text to append: ")
    data.write("\n"+add_text)
    print("Data successfully append\n")

with open("output.txt", "r") as file:
    print("Final content of 'output.txt': ")
    for line in file:
        print(line.strip("\n"))