import os, shutil, subprocess
from fuzzywuzzy import fuzz

categories = [
    "Thotsbay Forums",
    "3D",
    "ASMR",
    "Asian",
    "Brethren Court",
    "Cam Girls",
    "Celebrities",
    "Hentai",
    "Instagram",
    "ManyVids",
    "MILF",
    "OnlyFans",
    "Other",
    "Patreon",
    "Petite",
    "Reddit",
    "Requests",
    "SG",
    "Snapchat",
    "Suicide Girls",
    "TikTok",
    "Trans",
    "Twitch",
    "XXX",
    "Youtube",
]


def move_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".part"):
                file_path = os.path.join(root, file)
                try:
                    print(f"Moving {file} to {output_dir}")
                    shutil.move(file_path, output_dir)
                except shutil.Error as e:
                    print(f"error: {e}")


def main():
    cyberdrop_prefix = "path/to/CyberDropDownloader/Downloads/"
    cyberdrop_dirs = next(os.walk(cyberdrop_prefix))[1]
    
    collections_prefix = "path/to/collections/"
    collections_dirs = next(os.walk(collections_prefix))[1]
    
    for cyber_dir in cyberdrop_dirs:
        cyber_dir_sanitized = cyber_dir.split(" - ")
        for category in categories:
            if category in cyber_dir_sanitized:
                cyber_dir_sanitized.remove(category)
        for sanit in cyber_dir_sanitized:
            sanit = sanit.lower()
            for collections_dir in collections_dirs:
                collections_dir_sanitized = collections_dir.lower()
                if fuzz.ratio(sanit, collections_dir_sanitized) > 90:
                    input_dir = os.path.join(cyberdrop_prefix, cyber_dir)
                    output_dir = os.path.join(collections_prefix, collections_dir)
                    
                    if os.path.exists(input_dir):
                        if os.path.exists(output_dir):
                            try:
                                print(f'{input_dir}\n->\n{output_dir}')
                                if input("Continue? [y/n]: ") == "y":
                                    move_files(input_dir, output_dir)
                                    os.system("cls")
                            except Exception as e:
                                pass
                        else:
                            print(f"{input_dir} does not exist")
                            return
                    else:
                        print(f"{output_dir} does not exist")
                        return


if __name__ == "__main__":
    main()
    input("Press enter to exit...")
