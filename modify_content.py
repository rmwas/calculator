def modify_file_content(content):
    """Modify the content (example: convert to uppercase)"""
    return content.upper()

def read_and_write_file():
    """Reads a file, modifies its content, and writes to a new file."""
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_file_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File '{filename}' read successfully! Modified content saved to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
