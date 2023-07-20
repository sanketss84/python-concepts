import frontmatter
import frontmatter_helper as fh

filepath = './dummydata/test.md'
filepath_nofrontmatter = './dummydata/nofrontmatter.md'

## check if file has frontmatter ✅
# print(fh.is_file_having_frontmatter(filepath)) # returns true
# print(fh.is_file_having_frontmatter(filepath_nofrontmatter)) # returns false

## load the file only if it has front matter else we might need to add it
markdown_file = frontmatter.load(filepath) 

## read content ✅
# print(markdown_file.content) 

## read metadata ✅
# print(markdown_file['title'])
# print(markdown_file['type'])
# print(markdown_file['description'])
# print(markdown_file['tags'])
# print(markdown_file['tags_two'])
# print(markdown_file['created'])

## tags as list ✅
# tags = list(markdown_file['tags'])

# for tag in tags:
#     print(tag)

## tags as list ✅
# tags2 = list(markdown_file['tags_two'])

# for tag in tags2:
#     print(tag)

## get all yaml properties in markdown_file
# print(markdown_file.keys())

## get all props and auto list ✅
# fh.list_all_yaml_properties(markdown_file)

## check if list ✅
# print(fh.is_list(markdown_file['tags'])) ## returns true
# print(fh.is_list(markdown_file['tags_two'])) ## returns true
# print(fh.is_list(markdown_file['title'])) ## returns false
# print(fh.is_list(markdown_file['created'])) ## returns false

## check if is date ✅
# print(fh.is_date(markdown_file['created'])) ## returns true
# print(fh.is_date(markdown_file['title'])) ## returns false
# print(fh.is_date(markdown_file['tags'])) ## returns false

## date and date time ✅
# fh.getdatenow()
# fh.getdatetimenow()
