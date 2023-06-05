from pathlib import Path

fname = input("enter name to create a folder")
delete = True
if len(fname) >= 1:
    path = Path(fname)
    print(path, " file created from your directory", path.mkdir())


else:
    print("Enter the Correct file name at least one character")

# print(fname)


delete = input("do you want to delete the folder? y/n")
delete1 = delete.lower()

if delete1 == 'y':
    path = Path(fname)
    print(path, " file removed from your directory", path.rmdir())
elif delete1 == 'n':
    print("File saved in your directory")
else:
    print("enter only 'y' or 'n'")

print("_______________________________________________________")

#path = Path('ttt')
#print(path, " file removed from your directory", path.rmdir())