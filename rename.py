# Rename all files inside a folder (directory)
# Format : pic(number).extension
import os
path = 'images'

files = os.listdir(path)

file_counter = 0

# Count files inside folder
for i, filename in enumerate(files):
    file_counter += 1
    file_extension = filename.split('.')[-1]

    original = os.path.join(path, filename)
    new = os.path.join(path, 'pic' + str(i+1) + '.' + file_extension)
    
    # Rename each file
    os.rename(original, new)

