import os

# ASCII Art and Authorship
def print_ascii_art():
    print("__________                  __  ___________        ___________")
    print("\\______   \\  ____    ____ _/  |_\\_   _____/___  ___\\_   _____/")
    print(" |       _/ /  _ \\  /  _ \\   __\\|    __)_ \\  \\/  / |    __)_ ")
    print(" |    |   \\(  <_> )(  <_> )|  |  |        \\ >    <  |        \\")
    print(" |____|_  / \\____/  \\____/ |__| /_______  //__/\\_ \\/_______  /")
    print("        \\/                              \\/       \\/        \\/")
    print("")
    print("# Author: Ross Brereton (https://www.linkedin.com/in/ross-b-673872107/)")
    print("# Website: https://github.com/msf-Root-ExE")

# Define a dictionary of file types and their magic numbers in bytes
MAGIC_NUMBERS = {
    # ... (all the magic number entries)
    "txt": None,
    "md": None,
    # ... (other file types)
}

def list_files(directory):
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")
        return files
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return []

def main():
    # Print the ASCII art and authorship details
    print_ascii_art()
    
    print("Select a directory:")
    print("1. Current Directory")
    print("2. Desktop")
    print("3. Documents Directory")
    dir_choice = int(input("Enter the number corresponding to the directory: "))
    
    if dir_choice == 1:
        directory = "."
    elif dir_choice == 2:
        directory = os.path.join(os.path.expanduser('~'), 'Desktop')
    elif dir_choice == 3:
        directory = os.path.join(os.path.expanduser('~'), 'Documents')
    else:
        print("Invalid choice.")
        return
    
    print(f"Available files in {directory}:")
    files = list_files(directory)

    if not files:
        return

    file_index = int(input("Select a file by entering its number: ")) - 1
    if file_index < 0 or file_index >= len(files):
        print("Invalid selection.")
        return
    
    filename = files[file_index]

    print("Available Extensions:")
    for ext in MAGIC_NUMBERS.keys():
        print(ext)

    tgt_ext = input("Enter the target file extension from the available list: ")
    if tgt_ext not in MAGIC_NUMBERS:
        print("Invalid extension.")
        return
    
    new_filename = os.path.splitext(filename)[0] + '.' + tgt_ext
    
    if MAGIC_NUMBERS[tgt_ext]:
        try:
            with open(filename, 'rb') as file:
                content = file.read()
            with open(filename, 'wb') as file:
                file.write(MAGIC_NUMBERS[tgt_ext] + content)
        except Exception as e:
            print(f"Error modifying file: {e}")
            return

    try:
        os.rename(filename, new_filename)
        print(f"Changed {'' if MAGIC_NUMBERS[tgt_ext] else 'extension and '}renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error renaming file: {e}")

if __name__ == "__main__":
    main()


