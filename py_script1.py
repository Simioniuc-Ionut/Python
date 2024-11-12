import sys as sys
import os as os


def py_script():
    dir_path = sys.argv[1]
    if not dir_path:
        print("Directory path is missing")
        return
    if not os.path.isdir(dir_path):
        print("Invalid directory path")
        return
    file_extention = sys.argv[2]
    if not file_extention.startswith("."):
        print("Invalid File extension")
        return
    print("IN FISIER")
    for (directory, directories, files) in os.walk(dir_path):
        for file in files:
            if file.endswith(file_extention):
                try:
                    with open(os.path.join(directory,file),'r') as f:
                        print(f.read())
                        f.close()
                except FileNotFoundError:
                    print("File not found")
                except Exception as e:
                    print("Generic error ", str(e))

py_script()