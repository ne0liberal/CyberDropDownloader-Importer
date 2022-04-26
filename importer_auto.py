import os, shutil
from fuzzywuzzy import fuzz

tags = [
    "Thotsbay Forums",
    "3D",
    "ASMR",
    "Asian",
    "Brethren Court",
    "Cam Girls",
    "Celeb",
    "Cosplay",
    "Hentai",
    "Instagram",
    "ManyVids",
    "MILF",
    "OnlyFans",
    "Other",
    "Patreon",
    "Petite",
    "Reddit",
    "Request",
    "SG",
    "Snapchat",
    "TikTok",
    "Teen",
    "T H I C C",
    "Trans",
    "Twitch",
    "XXX",
    "Youtube",
]


def ready_to_import(input_dir: str):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".part"):
                return True
    return False


def move_and_sort(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith(".part"):
                file_path = os.path.join(root, file)
                try:
                    message = f"Moving {file} to {output_dir}"
                    shutil.move(file_path, output_dir)
                except shutil.Error as e:
                    message = f"error: {e}"
                finally:
                    print(message)
  

def import_files(input_dir, output_dir, token_set_ratio, auto_move=False):
    if os.path.exists(input_dir) and os.path.exists(output_dir):
        if ready_to_import(input_dir):
            
            os.system("cls")
            print(f"Ratio: {token_set_ratio}")
            print(f'{input_dir}\n->\n{output_dir}')
            
            if auto_move:
                move_and_sort(input_dir, output_dir)
                
            else:
                if input("Move files? (y/n) ") == "y":
                    move_and_sort(input_dir, output_dir)
                    
            os.system("cls")
        else:
            print(f"{output_dir} has nothing to import")
            os.system("cls")
    else:
        print(f"{output_dir} does not exist")
        print("Something went very wrong...")

def main():
    unsorted = []
    
    cyberdrop_prefix = "path/to/CyberDropDownloader/Downloads/"
    cyberdrop_dirs = next(os.walk(cyberdrop_prefix))[1]
    collections_prefix = "path/to/collections/"
    collections_dirs = next(os.walk(collections_prefix))[1]

    for cyber_dir in sorted(cyberdrop_dirs):
        cyber_dir_split = cyber_dir.split(" - ")
        
        for tag in sorted(tags):
            if tag in cyber_dir_split:
                cyber_dir_split.remove(tag)
                
        for model_cyber in cyber_dir_split:
            model_cyber = model_cyber.lower()
            
            for model_collections in sorted(collections_dirs):
                model_collections = model_collections.lower()
                
                token_set_ratio = fuzz.token_set_ratio(model_cyber, model_collections)
                input_dir = os.path.join(cyberdrop_prefix, cyber_dir)
                output_dir = os.path.join(collections_prefix, model_collections)
                
                unsorted.append({"ratio": token_set_ratio, "input_dir": input_dir, "output_dir": output_dir})
    
    for item in sorted(unsorted, key=lambda x: x["ratio"], reverse=True):
        if item["ratio"] == 100:
            import_files(item["input_dir"], item["output_dir"], item["ratio"], auto_move=True)
        elif item["ratio"] >= 45 and item["ratio"] < 100:
            import_files(item["input_dir"], item["output_dir"], item["ratio"], auto_move=False)
        elif item["ratio"] > 25 and item["ratio"] < 45:
            if ready_to_import(item["input_dir"]):
                print(item["input_dir"], "needs to be manually imported.")
                output_dir = input("Enter the output directory: ")
                import_files(item["input_dir"], output_dir, item["ratio"], auto_move=False)
                break

if __name__ == "__main__":
    main()
    input("Press enter to exit...")
