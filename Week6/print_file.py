file_name = input("Enter name of the file to read: ")
try:
     infile = open(file_name, "r")
     line = infile.readline()
     while line !='':
          print(line.rstrip())
          line = infile.readline()
except FileNotFoundError:
     print('The file does not exist!')

