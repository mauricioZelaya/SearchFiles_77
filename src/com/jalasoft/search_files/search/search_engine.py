import os

# for root, dirs, files in os.walk("C:\Users\Administrator\Documents\DevFund2\SearchFiles_77"):
#    for name in files:
#       print(os.path.join(root, name))
   # for name in dirs:
   #    print(os.path.join(root, name))

print("root prints out directories only from what you specified")
print("dirs prints out sub-directories from root")
print("files prints out all files from root and directories")
print("*" * 20)
for root, dirs, files in os.walk("/"):
    print(root)
    print(dirs)
    print(files)