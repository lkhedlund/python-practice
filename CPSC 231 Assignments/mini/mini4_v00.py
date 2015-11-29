# Name: Lars Hedlund
# ID Number: 00308102
# Tutorial number: 02

# >>> insert your function definition here <<<
def multiply(x, y):
    """
    function: multiply
    @multiply(float, float)
    @returns: product of two numbers
    """
    return x * y

def start():
    print("This program will multiply two numbers")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # >>> insert your function call here <<<
    product = multiply(num1, num2)
    print("%f * %f = %f" %(num1,num2,product))

start()
