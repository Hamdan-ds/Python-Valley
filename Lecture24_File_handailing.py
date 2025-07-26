# Importing required modules for file handling and Excel interaction
import os
import shutil  # Imported but not used in this snippet
import xlrd     # For reading older .xls Excel files
import openpyxl # For newer .xlsx files (not used here but good to keep for compatibility)

# Opening and reading the contents of 'working.txt' in read+write mode
my_file = open("working.txt", 'r+')
print(my_file.read())

# Overwriting the file with new lines of text
my_file = open("working.txt", 'w')
my_file.write("my name is khan sab\n")
my_file.write("my name is asad\n")
my_file.write("my name is hamdan khan")

# Writing a multiline string into the file
my_file.write("""Hi welcome to python class we are very happy to met you
i like to learn something new in this classes 
in future i will do something new """)

# Writing a list of lines using writelines()
new_file = ["\nfirst line\n", "second line\n", "third line\n", "forth line\n"]
my_file.writelines(new_file)

# Writing additional text (note: missing newline chars between lines)
my_file.write("fifth line\nsixth line\nseven line")

#  Loop won't work here
for l in my_file:
    print(l)

# Opening an Excel .xls file and reading sheet named "Sheet1"
my_sheet = xlrd.open_workbook_xls(r"D:\std_excel\stdTable.xls")
data = my_sheet.sheet_by_name("Sheet1")

# Parsing rows to extract student data into a dictionary
dict1 = {}
for x in range(1, 27):
    student_name = data.cell_value(x, 0)
    course = data.cell_value(x, 1)
    student_fee = data.cell_value(x, 2)
    dict1[student_name] = {'Course name': course, 'Fee': student_fee}

# Displaying the parsed dictionary
print(dict1)

print("-----------------------<o>----------------------------")

# Reopening the file for reading to view updated content
with open("working.txt", 'r') as my_file:
    print(my_file.read())

# Appending a new line to the file
with open("working.txt", 'a') as my_file1:
    my_file1.write("he is bad boy\n")

# ️ Misuse of 'writelines' in read mode; no visible effect
with open("working.txt", 'r') as my_file2:
    my_files = ["first line \n", "second line\n", "third line\n"]
    my_file2.writelines(my_files)  # This line won’t work as expected

# Appending a list of lines and printing them to stdout
my_filer = ["fifth line", "sixth line", "seven line"]
with open("working.txt", 'a') as my_file3:
    for l in my_filer:
        print(l)