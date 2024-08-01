def reverse_number(number):
    return int(str(number)[::-1].lstrip('0'))
print(reverse_number(11223344)) 

def main():
    while True:
        user_input = input("Enter a number to reverse: ")
        
        try:
            number = int(user_input)
            reversed_num = reverse_number(number)
            print(f"Reversed number: {reversed_num}")
            break  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
