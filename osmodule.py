import os
def current_directory():
    cwd = os.getcwd()
    print(cwd)

def file_path(filename):
    path=os.path.abspath((filename))
    print(path)
    try:
    # Open a file in write mode ('w' or 'w+') or create it if it doesn't exist
        with open('example.txt', 'w') as file:
        # Perform operations on the file if needed
            file.write("This is an example.")
    except IOError as e:
        print("Error:", e)


current_directory()
filename = "sample.txt"
file_path(filename)