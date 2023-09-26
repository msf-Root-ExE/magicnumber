import os

# Define a dictionary of file types and their magic numbers in bytes
MAGIC_NUMBERS = {
    "jpg": b'\xFF\xD8\xFF',
    "png": b'\x89PNG',
    "gif": b'GIF8',
    "pdf": b'%PDF',
    "zip": b'PK\x03\x04',
    "mp3": b'\xFF\xFB',
    "mp4": b'\x00\x00\x00\x1Cftyp',
    "avi": b'RIFF....AVI LIST',
    "bmp": b'BM',
    "flac": b'fLaC',
    "wav": b'RIFF....WAVE',
    "tiff": b'II*\x00',
    "7z": b'\x37\x7A\xBC\xAF\x27\x1C',
    "rar": b'Rar!\x1A\x07\x00',
    "tar": b'\x75\x73\x74\x61\x72\x00\x30\x30',
    "mov": b'\x00\x00\x00\x14ftyp',
    "midi": b'MThd',
    "iso": b'\xCD\x01',
    "rtf": b'{\\rtf1',
    "exe": b'MZ',
    "class": b'\xCA\xFE\xBA\xBE',
    "doc": b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1',
    "docx": b'PK\x03\x04',
    "xls": b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1',
    "xlsx": b'PK\x03\x04',
    "ppt": b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1',
    "pptx": b'PK\x03\x04',
    "mdb": b'\x00\x01\x00\x00Standard Jet DB',
    "txt": None,
    "md": None,
    "csv": None,
    "html": None,
    "xml": None,
    "json": None,
    "yaml": None,
    "ini": None,
    "conf": None
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
    print("Select a directory:")
    print("1. Current Directory")
    print("2. Desktop")
    print("3. Root Directory")
    dir_choice = int(input("Enter the number corresponding to the directory: "))
    
    if dir_choice == 1:
        directory = "."
    elif dir_choice == 2:
        directory = os.path.join(os.path.expanduser('~'), 'Desktop')
    elif dir_choice == 3:
        directory = "/"
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
            with open(filename, 'r+b') as file:
                file.write(MAGIC_NUMBERS[tgt_ext])
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

