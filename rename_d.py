import os

directory = r'.'

# Use underscore? Otherwise defaults to hyphen
is_use_underscore = True
char_to_use = '_' if is_use_underscore else '-'   

print("Renaming files now!")
for root, dirs, files in os.walk(directory):
    print(f"root: {root}")
    print(f"dirs: {dirs}")

    for current_dirname in dirs:
        new_dirname = current_dirname.replace(' ', char_to_use)

        print(f"current dirname: {current_dirname}")
        print(f"    new dirname: {new_dirname}")

        os.rename(
            os.path.join(root, current_dirname), 
            os.path.join(root, new_dirname)
        )   

print("All done!")
