from pathlib import PurePath
import vim

def get_directory_name_from_buffer(level = 1):
    if level is None or level == '':
    	level = 1
    level = int(level) - 1
    
    cpath_name = vim.current.buffer.name
    p = PurePath(cpath_name)
    
    while level > 0:
    	p = p.parent
    	level = level - 1
    return p.parent.name
