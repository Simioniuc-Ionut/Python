import os
import sys

def py_script2():
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print("Invalid path")
        return
    count_file = 1
    for file in os.listdir(dir_path):
        try:
            file_path= os.path.join(dir_path,file)
            # print("fp:",file_path)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    base_name = os.path.basename(f.name)
                    new_name = f"{base_name[:base_name.find('.')]}_{count_file}{base_name[base_name.find('.'):]}"
                # print("nm,:", new_name)
                new_path_file = os.path.join(dir_path,new_name)
                # print("ff ", file_path,new_path_file)
                os.rename(file_path,new_path_file)
                count_file+=1
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Generic error ",str(e))

py_script2()
