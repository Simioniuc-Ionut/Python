import os
import sys

import os
import sys


def py_script3():
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print("Invalid path")
        return
    total_size = 0
    for directory, directories, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(directory, file)
            try:
                with open(full_path, 'r') as f:
                    data = f.read()
                    total_size += len(data)
            except Exception as e:
                print("Generic exp", str(e))

    print(f"Total bytes is: {total_size}")

py_script3()
