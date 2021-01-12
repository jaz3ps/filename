"""""This is middle version of filename task"""

# Input
file_list = [
    '/home/python/learning/good_stuff/code1.py',
    '/home/python/learning/folder/x/new folder/hidden_file.dat',
    '/home/python/learning/my/files/funny_cat.jpeg',
    '/home/python/learning/files/this.is.weird.file.name.pdf' # this one as bonus
]
# New list for all new filenames
filenames = []

# iterate through all elements in given list with strings
for item in file_list:
    new_item_list = list(item.split(sep='/'))                           # seperate words in strings
    filename = new_item_list[len(new_item_list) - 1:]                   # get file name with extension
    filenames.extend(filename)                                          # add seperated file names in a new list

# iterate through all seperated elements in new list
for item in filenames:
    dot_count = item.count('.')

    if dot_count > 1:                                                          # If more then 5 dots in string, then do seperation
        dot_list = list(item.split(sep='.'))
        file_name_and_type = dot_list[len(dot_list)-2:]
        print(f"\nFilename: {file_name_and_type[0]}\nExtension: {file_name_and_type[1]}\n") # Print result

    else:
        dot_split = item.split('.', 1)                                         # Split file extension from file name
        print(f"\nFilename: {dot_split[0]}\nExtension: {dot_split[1]}\n")      # Print result

