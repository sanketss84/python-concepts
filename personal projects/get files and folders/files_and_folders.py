# https://realpython.com/get-all-files-in-directory-python/
# you’ll be focusing on the most general-purpose techniques in the pathlib module to list items in a directory, 
# but you’ll also learn a bit about some alternative tools.

## for working with file and folders 
## before pathlib came out you had to use the os module 

## issue with os module 
## 1. handling path as string, gets trickey when you work with multiple os
## 2. you have to use bunch of string manipulation code. things get cryptic pretty quickly.

## it all begins with creating a path object
## windows will get a WindowsPath object
## linux and mac gets PosixPath object

import pathlib
folder_path_to_parse = pathlib.Path("./dummyfolders")
# print(folder_path_to_parse) 

# -iterdir----------------------------------
## With these OS-aware objects, 
# you can take advantage of the many methods and properties available, 
# such as ones to get a list of files and folders.

# Be aware that there are several ways to do this, 
# and picking the right one will depend on your specific use case.

## If you only need to list the contents of a given directory, 
# and you don’t need to get the contents of each subdirectory too, 
# then you can use the Path object’s .iterdir() method.

## The .iterdir() method, when called on a Path object, 
# returns a generator that yields Path objects representing child items. 
# If you wrap the generator in a list() constructor, 
# then you can see your list of files and folders

# .iterdir() produces a generator
# folder_path_to_parse.iterdir()

# Which you can wrap in a list() constructor to materialize
# thelist = list(folder_path_to_parse.iterdir())
# print(thelist)

## Passing the generator produced by .iterdir() to the list() constructor 
# provides you with a list of Path objects representing 
# all the items in the Desktop directory.

# As with all generators, you can also use a for loop to iterate 
# over each item that the generator yields. 
# This gives you the chance to explore some of the properties 
# of each object

# for item in folder_path_to_parse.iterdir():
    # print(f"{item} - {'dir' if item.is_dir() else 'file'}")


# -rglob----------------------------------
## for recursion there is a different function rglob()
# With pathlib, it’s surprisingly easy to recurse through a directory. 
# You can use .rglob() to return absolutely everything:

# .rglob() produces a generator too
# folder_path_to_parse.rglob("*")

# Which you can wrap in a list() constructor to materialize
# thelist2 = list(folder_path_to_parse.rglob("*")) # all files all extensions
# thelist2 = list(folder_path_to_parse.rglob("*.txt")) # only markdowns
# print(thelist2)

# thelist2 = list(folder_path_to_parse.rglob("2*.txt")) # only markdowns
# print(thelist2)
# thelist2 = list(folder_path_to_parse.rglob("r*.txt")) # only markdowns
# print(thelist2)

# thelist2 = list(folder_path_to_parse.rglob("*.md")) # only markdowns
# print(thelist2)

# thelist2 = list(folder_path_to_parse.rglob("4*.md")) # only markdowns
# print(thelist2)

# -pattern----------------------------------
## pattern matching
# *	Every item
# *.txt	Every item ending in .txt, such as notes.txt or hello.txt
# ??????	Every item whose name is six characters long, such as 01.txt, A-01.c, or .zshrc
# A*	Every item that starts with the character A, such as Album, A.txt, or AppData
# [abc][abc][abc]	Every item whose name is three characters long but only composed of the characters a, b, and c, such as abc, aaa, or cba
# more info https://docs.python.org/3/library/fnmatch.html#module-fnmatch 
# Note that on Windows, glob patterns are case-insensitive, because paths are case-insensitive in general. 
# On Unix-like systems like Linux and macOS, glob patterns are case-sensitive.

# -glob----------------------------------
# glob
# The .glob() method of a Path object behaves in much the same way as .rglob(). 
# If you pass the "*" argument, then you’ll get a list of items in the directory, 
# but without recursion

# thelist3 = list(folder_path_to_parse.glob('*.txt'))

# https://realpython.com/python-string-contains-substring/
# for item in thelist3:
#     if "root" in str(item).lower(): # contains operation
#         print('root file!!!')
#     else:
#         print('not root')

# -isdisjoint----------------------------------
## filtering subdirectories with irrelevant data or folders to scan for

# You can check if any two iterables have an item in common by 
# taking advantage of sets. If you cast one of the iterables to a set, 
# then you can use the .isdisjoint() method to determine whether they 
# have any elements in common

# {"documents", "notes", "find_me.txt"}.isdisjoint({"temp", "temporary"})
# returns true
# {"documents", "temp", "find_me.txt"}.isdisjoint({"temp", "temporary"})
# returns false 

# SKIP_DIRS = ['skip this','skip this 2']

# for item in folder_path_to_parse.rglob('*'):
#     # print(item.parts)
#     if set(item.parts).isdisjoint(SKIP_DIRS):
#         print(item)

# These methods are already getting a bit cryptic and hard to follow, though. 
# Not only that, but they aren’t very efficient, because the .rglob() generator 
# has to produce all the items so that the matching operation can discard that result.

# You can definitely filter out whole folders with .rglob(), 
# but you can’t get away from the fact that the resulting generator will yield all the items 
# and then filter out the undesirable ones, one by one. 
# This can make the glob methods very slow, depending on your use case. 
# That’s why you might opt for a recursive .iterdir() function, which you’ll explore next.

# -Recursive .iterdir----------------------------------
import skip_directories as sd

folder_path_to_parse = pathlib.Path("./dummyfolders")
thefinallist = list(sd.get_all_items(folder_path_to_parse))

for item in thefinallist:
    print(item)