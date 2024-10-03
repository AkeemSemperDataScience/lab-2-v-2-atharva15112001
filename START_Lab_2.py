def lab2Question1(word):
    # Note - you'll need to change the signature (above) to match the arguments for this lab...
    # Create a function that takes in a string 
    # Return True if that string is a palindrome, False otherwise
    # Clean the string by converting to lowercase and removing non-alphanumeric characters
    cleaned_word = ''.join(c.lower() for c in word if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_word == cleaned_word[::-1]

# Example usage:
print(lab2Question1("A man, a plan, a canal, Panama"))  # True
print(lab2Question1("Hello"))  # False

# Example usage:
print(lab2Question1("A man, a plan, a canal, Panama"))  # True
print(lab2Question1("Hello"))  # False
def lab2Question2(number_val):
    # Create a function that takes in a number
    # Return a list of the fibonacci sequence up to that number
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate Fibonacci numbers up to number_val
    while fib_sequence[-1] + fib_sequence[-2] <= number_val:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Return the Fibonacci sequence
    return fib_sequence

# Example usage:
print(lab2Question2(21))  # [0, 1, 1, 2, 3, 5, 8, 13, 21]
print(lab2Question2(10))  # [0, 1, 1, 2, 3, 5, 8]

def lab2Question3(str1, str2):
    # Create a function that takes in two strings - str1 and str2
    # Return the number of times str2 appears in str1
    # For example if str1 = "coding is cool" and str2 = "co" then output should be 2.
    # Use the count method to find how many times str2 will show in str1 return str1.count (str2)
    # Use the count method to find how many times str2 appears in str1
    return str1.count(str2)

# Example usage:
print(lab2Question3("coding is cool", "co"))  # Output: 2
print(lab2Question3("hello hello hello", "hello"))  # Output: 3

def lab2Question4(list1, list2):
    # Create a function that takes in two equal length list of numbers. 
    # Return a list of the element-wise sum of the two lists - i.e. the first element of the output list is the sum of the first elements of the input lists
    # If the condition of the function is not satisfied, return a blank list
    # Return an empty list if the lists are not of equal length
    if len(list1) != len(list2):
        return []
    
    # Return the element-wise sum of the two lists
    return [x + y for x, y in zip(list1, list2)]

# Example usage:
print(lab2Question4([1, 2, 3], [4, 5, 6]))  # Output: [5, 7, 9]
print(lab2Question4([1, 2], [3, 4, 5]))     # Output: []

def lab2Question5():
    # Create a function* that asks a user to enter a password that meets the following criteria:
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # Keep asking the user to enter a password until they enter a valid password.
    # Return the valid password.
    # *Note: This function should call another function, called isValidPassword(password), 
    # that takes in a password and returns True if the password is valid, False otherwise.
    # You will need to make that function, exactly as described above. 
    password = None

    return password
# Check if the password meets the specified criteria
    if (len(password) < 8):
        return False
    if not any(c.isupper() for c in password):  # Check for at least one uppercase letter
        return False
    if not any(c.islower() for c in password):  # Check for at least one lowercase letter
        return False
    if not any(c.isdigit() for c in password):  # Check for at least one number
        return False
    return True
    password = None
    while True:
        password = input("Enter a password: ")
        if isValidPassword(password):
            break  # Exit the loop if a valid password is entered
        else:
            print("Invalid password. Please try again.")

    

def isValidPassword(password):
    # Create a function that takes in a password and returns True if the password is valid, False otherwise
    # - At least 8 characters long
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
     # Check if the password meets the specified criteria
    if len(password) < 8:  # At least 8 characters long
        return False
    if not any(c.isupper() for c in password):  # At least one uppercase letter
        return False
    if not any(c.islower() for c in password):  # At least one lowercase letter
        return False
    if not any(c.isdigit() for c in password):  # At least one number
        return False
    return True  # All criteria met

# Example usage:
print(isValidPassword("Password1"))  # True
print(isValidPassword("pass"))        # False
print(isValidPassword("PASSWORD"))    # False
print(isValidPassword("Pass1"))       # False
print(isValidPassword("PassWord"))    # False

