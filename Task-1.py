print("Reading file content:\n")
filename = "sample.txt"
try:
    with open(filename, "r") as file:
        for i, line in enumerate(file,start=1):
            print(f"Line {i}: {line.strip("\n")}")

except FileNotFoundError:
    print(f"The file '{filename}' was not found")


