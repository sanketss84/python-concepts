import frontmatter
import datetime

## misc

# https://www.w3schools.com/python/python_datetime.asp
# https://www.programiz.com/python-programming/datetime/current-datetime

def getdatenow():
    print(datetime.date.today()) # this is all I need to create date
    # print(datetime.date.today().strftime("%d/%m/%Y"))
    # print(datetime.date.today().strftime("%B %d, %Y"))

def getdatetimenow():
    # print(datetime.datetime.now())
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) # 24 hrs  
    print(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")) ## 12 hrs with am pm

## checks
def is_file_having_frontmatter(filepath):
    if (frontmatter.check(filepath)):
        return True
    return False

def is_list(property):
    if isinstance(property, list):
        return True
    return False

def is_date(property):
    if isinstance(property, datetime.date):
        return True
    return False

## read operations

def list_all_yaml_properties(markdown_file):
    for prop in markdown_file.keys():
        print(markdown_file[prop])


## write file

# https://techoverflow.net/2019/07/24/how-to-write-bytesio-content-to-file-in-python/
def write_bytesio_to_file(filename, bytesio):
    # Write the contents of the given BytesIO to a file.
    # Creates the file or overwrites the file if it does
    # not exist yet. 
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())