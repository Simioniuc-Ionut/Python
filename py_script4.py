import os
import sys
def py_script():
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print("Error invalid path")
        return
    map_dir = {}
    try:
        files=os.listdir(dir_path)
        print("All files",files)
        if not files:
            raise "The directory is empty"

        for file in files:
            full_path  = os.path.join(dir_path,file)
            if os.path.isfile(full_path):
                extension = os.path.splitext(full_path)[-1]
                if extension not in map_dir.keys():
                    map_dir[extension] = 1
                else:
                    map_dir[extension] += 1
    except FileNotFoundError:
        print("Not file found")
        return
    except PermissionError:
        print("Permission denied")
        return
    except Exception as e:
        print("Generic error", str(e))
    finally:
        print("Map dir is ",map_dir)


py_script()