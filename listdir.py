import os
import pprint

dir_name = input("Enter full path to sort by file size: ")
#dir_name = r"C:\Users\jefni\MyPythonScripts"

dir_contents = os.listdir(dir_name)
print("----Directory:", dir_name)

# ignoring sub and subsubfolders, only getting file and file sizes
def sorted_file_name_size_pair():
    filename_list = []
    filesize_list =[]
    for file in dir_contents:
        if os.path.isdir(file) == True:
            continue
        filename_list.append(file)
        filesize_list.append(round(os.path.getsize(file) / 1000))
    # merge the 2 lists to make a key-value pair 
    file_name_size_pair = dict(zip(filename_list, filesize_list))
    # sort the key value pair according to the file size
    sorted_file_name_size_pair = sorted(file_name_size_pair.items(), key=lambda kv: kv[1], reverse = True)
    # use pprint module for pretty 
    pprint.pprint(sorted_file_name_size_pair)



sorted_file_name_size_pair()
print('\n')


for file in dir_contents:
    if os.path.isdir(file) == True:
        print('----Subdirectory:', file)
        subdir_name = dir_name + "\\" + file
        os.chdir(subdir_name)
        dir_contents = os.listdir(subdir_name)
        sorted_file_name_size_pair()
        if os.path.isdir(file) == True:
            print('--------Subsubdirectory:', file)
            subdir_name = dir_name + "\\" + file
            os.chdir(subdir_name)
            dir_contents = os.listdir(subdir_name)
            sorted_file_name_size_pair()

        
        # exit subdirectories and go back to main directory supplied
        os.chdir(dir_name)
        print('\n')