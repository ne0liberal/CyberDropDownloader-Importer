import os, shutil

"""this is my alt for when i cant automatically use fuzzy matching to find the correct folder to import to
it just iterates thru every folder you have downloaded and then asks for the full path to move said folders contents to.
also this is deprecated, and i wont be cleaning it up"""

def move_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith('.part'):
                file_path = os.path.join(root, file)
                try:
                    print(f"Moving {file} to {output_dir}")
                    shutil.move(file_path, output_dir)
                except shutil.Error as e:
                    print(f"error: {e}")


def main():
    parent_dir = "path/to/CyberDropDownloader/Downloads"
    dirs = next(os.walk(parent_dir))[1]
    for dir in dirs:
        input_dir = os.path.join(parent_dir, dir)
        print(f"Searching {input_dir}")
        output_dir = input("Enter the full directory path to move the files to: ")
        move_files(input_dir, output_dir)
        os.system("cls")


if __name__ == '__main__':
    main()
