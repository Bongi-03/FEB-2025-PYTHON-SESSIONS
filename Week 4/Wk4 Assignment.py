def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")
        
        # Open and read the file
        with open(filename, "r") as file:
            content = file.readlines()
        
        # Modify content (Example: Convert text to uppercase)
        modified_content = [line.upper() for line in content]

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"File processed successfully! Modified content saved in '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read the file. Please check the file permissions.")

# Run the function
read_and_modify_file()
