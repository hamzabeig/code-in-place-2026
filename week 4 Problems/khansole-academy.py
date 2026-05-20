import random

def main():
    print("Khansole Academy")
    number1 = random.randint(10,99)
    number2 = random.randint(10,99)
    result = number1+number2
    print(f"What is {number1} + {number2}?")
    answer = int(input(f"Your answer: "))
    
    if answer == result:
        print("Correct!")
        
    else:
        print("Incorrect.")
        print(f"The expected answer is {result}")
    
    
if __name__ == '__main__':
    main()
