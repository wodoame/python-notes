# In Python, you can delete a file using the `os` module.
# Here's a simple example:

import os

file_path = 'example.txt'  # Replace with the path to the file you want to delete

# Check if the file exists before attempting to delete
if os.path.exists(file_path):
    os.remove(file_path)
    print(f'The file {file_path} has been deleted.')
else:
    print(f'The file {file_path} does not exist.')


# In this example:

# 1. `os.path.exists(file_path)` checks if the file exists.
# 2. If the file exists, `os.remove(file_path)` deletes the file.
# 3. If the file does not exist, a message is printed indicating that the file doesn't exist.

# Make sure to replace `'example.txt'` with the actual path and filename of the file you want to delete.
# Also, be cautious when using `os.remove()` as it permanently deletes the file without moving it to the recycle bin.

# If you are working with directories, you can use `os.rmdir()` to remove an empty directory or `shutil.rmtree()` to remove a directory and its contents.
# Be careful when using these functions, especially with `shutil.rmtree()`, as it will permanently delete all files and subdirectories in the specified directory.
