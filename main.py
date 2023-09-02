def my_name():
    print("my name is mariam ")
my_name()
def my_meal (food,drink):  
    print(f"i like{food} and while drinking{drink}")
my_meal("fish","pepse")
def cube(number):
    return(number**3)
print(cube(9))
def by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return cube(num)
print(by_three(99))
print(by_three(77))
