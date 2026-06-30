def multiply_by_two(number):      #Pure function 
    return number * 2

total = 0

def total_sum():     #Impure
    total += 2
    return total

# Lambda Function

#1. Single argument

Square = lambda x : x ** 2
print(Square(5))

# 2. Multiple Argument:

Add_two_no = lambda x, y : x+y
print(Add_two_no(9,8))

nums = [1,2,4,6]

doubled = list(map(lambda x: x*2, nums))
print(doubled)

