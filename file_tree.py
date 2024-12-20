#!/usr/bin/python3.12

import os
import re
import os.path as path

def find_files(pattern, base='.'):
    """
    Finds files under the base directory that match the given pattern.

    Parameters:
    pattern (str): The regex pattern to match filenames.
    base (str): The base directory to start the search (default is current directory).

    Returns:
    list: A list of file paths that match the pattern.
    """
    # Compile the regex pattern for matching filenames
    regex = re.compile(pattern)
    
    # List to store the matching file paths
    matches = []
    
    # Walk through the directory tree starting from base
    for root, dirs, files in os.walk(base):
        for f in files:
            # If the filename matches the regex pattern, add it to the matches list
            if regex.match(f):
                matches.append(path.join(root, f))
    
    return matches

# Call the find_files function with a pattern to match Python files
if __name__ == "__main__":
    # List and print all Python files in the current directory and subdirectories
    python_files = find_files(r'.*\.py')
    for file in python_files:
        print(file)
