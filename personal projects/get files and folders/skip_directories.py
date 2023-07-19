import pathlib

SKIP_DIRS = ['skip this','skip this 2']

def get_all_items(root: pathlib.Path, exclude=SKIP_DIRS):
    for item in root.iterdir():
        if item.name in exclude:
            continue
        yield item        
        if item.is_dir():
            yield from get_all_items(item)