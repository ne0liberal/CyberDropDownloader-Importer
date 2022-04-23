import os, shutil
from fuzzywuzzy import fuzz

tags = [
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
    "Teen"
    "Trans",
    "Twitch",
    "XXX",
    "Youtube",
]

def ready_to_import(input_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".part"):
                return True
    return False


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
    
    collections_prefix = "path/to/your/collections/"
    collections_dirs = next(os.walk(collections_prefix))[1]
    
    for cyber_dir in cyberdrop_dirs:
        cyber_dir_split = cyber_dir.split(" - ")
        for tag in tags:
            if tag in cyber_dir_split:
                cyber_dir_split.remove(tag)
        for model_cyber in cyber_dir_split:
            model_cyber = model_cyber.lower()
            for model_collections in collections_dirs:
                if fuzz.ratio(model_cyber, model_collections.lower()) > 90:
                    input_dir = os.path.join(cyberdrop_prefix, cyber_dir)
                    output_dir = os.path.join(collections_prefix, model_collections)
                    
                    if os.path.exists(input_dir):
                        if os.path.exists(output_dir):
                            if ready_to_import(input_dir):
                                print(f'{input_dir}\n->\n{output_dir}')
                                if input("Continue? [y/n]: ") == "y":
                                    try:
                                        move_files(input_dir, output_dir)
                                    except Exception as e:
                                        print(f"error: {e}")
                                    os.system("cls")
                                else:
                                    os.system("cls")
                            else:
                                print(f"{output_dir} has nothing to import")
                                continue
                        else:
                            print(f"{input_dir} does not exist")
                            return
                    else:
                        print(f"{output_dir} does not exist")
                        return


if __name__ == "__main__":
    main()
    input("Press enter to exit...")
