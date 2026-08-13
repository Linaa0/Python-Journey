
def count_to(n):
    count=1
    while count<= n:
        yield count
        count+=1

  

number=int(input("Enter the number to count to: "))

for n in count_to(number):
    print(n)