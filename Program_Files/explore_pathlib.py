from pathlib import Path

# path = Path("ecommerce")
# print(path.exists())

'''
path= Path("new_dir")
path.mkdir()
# creates a new directory under the main Python_Data_Analytics dir.

path.rmdir()
# removes the directory

path.glob('*.*')
path.glob("*.xls") or path.glob("*.py") etc.
# search for directory & files in the current path
'''

path = Path("Program_Files")
for i in path.glob("*.py"):
    print(i)