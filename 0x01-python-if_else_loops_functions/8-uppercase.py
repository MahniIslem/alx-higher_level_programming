def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII manipulation
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end="")
        else:
            print("{}".format(char), end="")
    
    print()  # Print a new line after processing the entire string

# Test the function with the provided main code
uppercase("best")
uppercase("Best School 98 Battery street")
