#Create a function to read a number (minimum 4 digits) from the user and find the reverse of the 
#number using loop in another function and display both number and reverse of the number

def reverse_number(num):
    if num < 0:
        return "Enter a positive number"
    
    rev = 0
    while num > 0:
        last_dig = num % 10
        rev = rev * 10 + last_dig
        num = num // 10
    return rev

def main():
    number = input("Enter a number with minimum 4 digits: ")
    if len(number) < 4:
        print("Please enter a valid number with at least 4 digits.")
        return 
    
    number = int(number)
    reversed_number = reverse_number(number)
    print(f"Reversed number: {reversed_number}")

if __name__ == "__main__":
    main()
