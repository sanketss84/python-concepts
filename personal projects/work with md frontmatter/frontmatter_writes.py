from io import BytesIO
import frontmatter
import frontmatter_helper as fh

filepath = './dummydata/test.md'
f = BytesIO()

## load the file only if it has front matter else we might need to add it
markdown_file = frontmatter.load(filepath) 


## get all yaml properties in markdown_file ✅
# print(markdown_file.keys()) # this lists everything in order
# print(markdown_file.metadata)
# print(markdown_file.content)

## Serialize a post to a string and return text. ✅
# This always returns unicode text, which can then be encoded.
# print(frontmatter.dumps(markdown_file)) 

## get item ✅ 
print(markdown_file.get('title'))

## add new item or update exisiting ✅
markdown_file.__setitem__('title','a new title new')
print(markdown_file.get('title'))

# markdown_file.__setitem__('new_prop','new prop')
# markdown_file.__setitem__('new_prop 2','new prop 2')

## delete item ✅
# markdown_file.__delitem__('delete_me')


# https://github.com/eyeseast/python-frontmatter/issues/26 discussed here 
# we need to wite the file without sorting the metadata entries, the default code applied sorting 
# https://github.com/eyeseast/python-frontmatter/blob/main/examples/sorted.py
# frontmatter.dumps(markdown_file, sort_keys=False)
frontmatter.dump(markdown_file,f,sort_keys=False) # this is what writes to the ByteIO f object

## writing the modifications to the yaml meta data to the file ✅
# this is what it will write to the file ✅
# print(f.getvalue().decode('utf-8'))  # The getvalue() function just takes the value from the Buffer as a String.

# https://techoverflow.net/2019/07/24/how-to-write-bytesio-content-to-file-in-python/
# https://www.digitalocean.com/community/tutorials/python-io-bytesio-stringio
# code to write the ByteIO to the file ✅
# with open(filepath, "wb") as outfile:
#     outfile.write(f.getbuffer())

fh.write_bytesio_to_file(filepath,f)
