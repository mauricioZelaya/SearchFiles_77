"""
class Search_Engine perform the search on a given path of a given file_name applying all the desired filters
"""
import os


def print_directory(path):
    return os.listdir(path)

# def search_file(path, file_name):
#     for root, dirs, files in os.walk(path):
#         print(root)
#         # if file_name in files:
#         #     print("file path directory: %s" % root)
#         #     print(dirs)
#         #     print(files)
#         #     print("exist!!!")


# search_file("D:", "Behave_1.pptx")
path = "D:\MauricioZ\\"
directory_list = print_directory(path)
print(directory_list)
