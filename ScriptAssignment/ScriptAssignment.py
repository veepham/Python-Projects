import os
import time

path = "C:\\Users\\vipha\\OneDrive\\Documents\\GitHub\\Python-Projects\\ScriptAssignment\\"

def myScript():    
    dir_list = os.listdir(path)
    print('The files inside the directory ', path, ' :')
    print(dir_list)


def findTxt():
    print('Files that end in ".txt" in ', path, ' :')
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    i = 0
    while i < len(text_files):
        mtime = os.path.getmtime(text_files[i])
        local_time = time.ctime(mtime)
        print(os.path.join(path, text_files[i]), local_time)
        i = i + 1






if __name__ == "__main__":
    myScript()
    findTxt()
  
    
