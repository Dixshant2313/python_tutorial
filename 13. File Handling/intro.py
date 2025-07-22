"""
File Handling means Creating, Reading, Updating and Deleting (CRUD) operations that we can perform in files

"""

# p = open(r"D:\Python\problems\prime.py")
# print(p.read())                           # used to read a file 

# q = open("superman.txt","w")              # creates a file or overwrites the existing file
# q.write("Hello this is a text file ")
# q.close()

r = open("superman.txt","a")                # used to append the text without overwriting (end of the file)
r.write("and I am appending this text")
r.close()