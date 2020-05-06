import os 
import shutil 

os.chdir('/home/nopc/Downloads/SCRAP DOWNLOAD')

path_to_new_folder = os.getcwd() + '/PDFINHERE'
for f in os.listdir():
    if f.endswith('.pdf'):
        current_file = os.getcwd() + '/'+ f
        shutil.move(current_file, path_to_new_folder)
        print("Success")