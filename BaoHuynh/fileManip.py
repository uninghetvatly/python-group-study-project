#Python has built-in functions to create, read, update, and delete files.
#The key function for working with files is open().
#Format: file_object = open("filename", "mode")

#Common Modes:
#'r' - Read (Default). Opens for reading, throws an error if the file doesn't exist.
#'w' - Write. Opens for writing, creates the file if it doesn't exist, OVERWRITES if it does.
#'a' - Append. Opens for appending, creates the file if it doesn't exist. Additions go to the end.
#'x' - Create. Creates the specified file, returns an error if the file already exists.

#Writing to a file using 'w'
#Important: Always close the file when done using .close() to free up system resources.
file = open("my_notes.txt", "w")
file.write("First line of the file.\n")
file.write("Second line of the file.")
file.close()

#Appending to a file using 'a'
file = open("my_notes.txt", "a")
file.write("\nThis third line is appended to the end.")
file.close()

#Reading a file using 'r'
file = open("my_notes.txt", "r")
print("--- Reading the whole file ---")
content = file.read() # Reads the entire file content into a single string
print(content)
file.close()

#Reading a file line by line using .readline()
file = open("my_notes.txt", "r")
print("\n--- Reading line by line ---")
print(file.readline()) # Reads the first line
print(file.readline()) # Reads the second line
file.close()

#Reading all lines into a list using .readlines()
file = open("my_notes.txt", "r")
lines_list = file.readlines()
print("\n--- Reading into a list ---")
print(lines_list)
file.close()

#The 'with' statement (Context Manager) - BEST PRACTICE
#Automatically closes the file for you when the block ends, even if an error occurs.
#Format: with open("filename", "mode") as file_object:
print("\n--- Using 'with' statement ---")
with open("my_notes.txt", "r") as file:
    # Iterating directly over the file object is memory efficient for large files
    for line in file:
        print(line.strip()) # .strip() removes the trailing newline character (\n)

#File and Directory Operations (Requires the built-in 'os' module)
import os

#Check if a file exists before trying to interact with it
print("\n--- Checking existence ---")
if os.path.exists("my_notes.txt"):
    print("my_notes.txt exists!")
else:
    print("The file does not exist.")

#Rename a file using os.rename(old_name, new_name)
#os.rename("my_notes.txt", "renamed_notes.txt")

#Delete a file using os.remove(filename)
#if os.path.exists("my_notes.txt"):
#    os.remove("my_notes.txt")
#    print("\nmy_notes.txt has been successfully deleted.")
#else:
#    print("The file does not exist.")