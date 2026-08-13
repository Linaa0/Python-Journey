def readFile(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()



file_path=b"C:\\Users\\HP\\Desktop\\test.txt"

for line in readFile(file_path):
    print(line)