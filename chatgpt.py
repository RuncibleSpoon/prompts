def read_file(filename):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): Path to the file to read.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python file_reader.py <filename>")
    else:
        read_file(sys.argv[1])
