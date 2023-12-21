from typing import List, Union
import os, logging

def getFiles(path :str) -> Union[List[str], str]: 
    try:
        # Get all files in the directory
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return files, path
        
    except FileNotFoundError:
        logging.error("The specified path was not found.")
        return [], path

if __name__=='__main__': print(getFiles(os.path.join(os.path.expanduser('~'), 'Downloads')))