
def count_to(n):
    # numbers=[]
    count=1
    while count<= n:
        # numbers.append(count)
        yield number
        count+=1

    # return numbers

number=int(input("Enter the number to count to: "))

for n in count_to(number):
    print(n)