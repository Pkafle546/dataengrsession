print("Hello World")

"""
    Question 2: 
    find all unique elements in a list
    l = [0,0,0,1,1,1,1,2,2,3,3,4]
"""

l = [0,0,0,1,1,1,1,2,2,3,3,4]
unique_list = set(l)
print(list(unique_list))


"""
    find sum of largest numbers in the list
    num1 = [1, 2]
    num2 = [1, 9, 8, 1, 1, 1]
"""

num1 = [1, 2]
num2 = [1, 9, 8, 1, 1, 1]
def great_sum(list1,list2):
    greatest_sum= lambda list1,list2: max(list1)+max(list2)
    return greatest_sum(list1,list2)
total = great_sum(num1, num2)
print(total)


"""
    Q4: find if the given number is prime or not
"""

a=int(input("Enter a number greater than 1: "))
def is_prime(num):
    check_prime = lambda x: all(num%i !=0 for i in range(2, num) )
    return check_prime(num)

flag = is_prime(a)

if flag:
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")


"""
    Question 1
"""

def question_1():
    with open("test.txt", "r") as file:
        currentfile= file.read()
    







        





