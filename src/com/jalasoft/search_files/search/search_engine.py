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
directory_list = print_directory("D:\MauricioZ\\")
print(directory_list)
