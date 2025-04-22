def read_and_modify_file():
    # Step 1: Ask for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Step 2: Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("Original file read successfully!")

        # Step 3: Modify the content (e.g., make it uppercase)
        modified_content = content.upper()

        # Step 4: Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Run the function
read_and_modify_file()
