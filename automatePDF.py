import os 
import shutil 

os.chdir('/home/nopc/Downloads/SCRAP DOWNLOAD')

def move_pdf ():
    path_to_new_folder = os.getcwd() + '/PDFINHERE'
    for f in os.listdir():
        if f.endswith('.pdf'):
            current_file = os.getcwd() + '/'+ f
            shutil.move(current_file, path_to_new_folder)
            print("Success")

list_having_all_extensions = [] 

def findall () :
    for f in os.listdir():
        ch = f.split('.')
        if len(ch) == 2:
            list_having_all_extensions.append(ch[1])
    removing_duplicates()    
    
def removing_duplicates ():
    unique_extensions = list(dict.fromkeys(list_having_all_extensions))
    print(unique_extensions)


findall()