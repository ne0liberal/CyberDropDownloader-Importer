import os
import shutil
import subprocess
from fuzzywuzzy import fuzz


def ready_to_import(input_dir):
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
            print(f"{input_dir}\n->\n{output_dir}")

            if auto_move:
                move_and_sort(input_dir, output_dir, auto_sort=True)

            else:
                if input("Move files? (y/n) ") == "y":
                    move_and_sort(input_dir, output_dir, auto_sort=True)

            os.system("cls")
        else:
            print(f"{output_dir} has nothing to import")
            os.system("cls")
    else:
        print(f"{output_dir} does not exist")
        print("Something went very wrong...")


def get_fuzz_ratio(input_dir, output_dir):
    return fuzz.token_set_ratio(input_dir, output_dir)


def main():
    unsorted = []

    cyberdrop_root = "path/to/CyberDropDownloader/Downloads/"
    cyberdrop_dirs = next(os.walk(cyberdrop_root))[1]
    collections_root = "path/to/collections/"
    collections_dirs = next(os.walk(collections_root))[1]

    for dir_collections in sorted(collections_dirs):
        dir_collections = dir_collections.lower()

        for dir_cyberdrop in sorted(cyberdrop_dirs):
            dir_cyberdrop = dir_cyberdrop.lower()

            token_set_ratio = get_fuzz_ratio(dir_cyberdrop, dir_collections)
            input_dir = os.path.join(cyberdrop_root, dir_cyberdrop)
            output_dir = os.path.join(collections_root, dir_collections)

            unsorted.append(
                {
                    "ratio": token_set_ratio,
                    "input_dir": input_dir,
                    "output_dir": output_dir,
                    "dir_cyberdrop": dir_cyberdrop,
                    "dir_collections": dir_collections,
                }
            )

    for item in sorted(unsorted, key=lambda x: x["ratio"], reverse=True):
        if item["ratio"] == 100:
            import_files(
                item["input_dir"], item["output_dir"], item["ratio"], auto_move=False
            )
        elif item["ratio"] >= 45 and item["ratio"] < 100:
            import_files(
                item["input_dir"], item["output_dir"], item["ratio"], auto_move=False
            )
        elif item["ratio"] > 25 and item["ratio"] < 45:
            if ready_to_import(item["input_dir"]):
                print(item["input_dir"], "needs to be manually imported.")
                output_dir = None

                while True:
                    output_dir = input("Enter the output directory: ")
                    if not output_dir:
                        print("Please enter a valid directory.")
                        continue
                    else:
                        break

                if not os.path.exists(output_dir):
                    os.mkdir(output_dir)

                import_files(
                    item["input_dir"],
                    output_dir,
                    get_fuzz_ratio(item["input_dir"], output_dir),
                    auto_move=False,
                )
                break


if __name__ == "__main__":
    main()
    input("Finished.\nPress enter to exit...")
