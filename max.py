def find_max_element(arr):
    if not arr:
        return None
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

def main():
    while True:
        user_input = input("Enter the elements of the array separated by spaces: ")
        
        try:
            arr = list(map(int, user_input.split()))
            
            if not arr:
                print("The array cannot be empty. Please enter at least one number.")
                continue

            max_element = find_max_element(arr)
            print(f"The maximum element is: {max_element}")
            break  
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces.")

if __name__ == "__main__":
    main()