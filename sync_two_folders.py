import os
import argparse
import time
import shutil


def check_folders_existance(source, replica):
    '''Check if source folder exist'''
    if not os.path.isdir(source):
        log_file(f'{source} folder does not exist')
        raise argparse.ArgumentError(None, "Source folder does not exist")
    

    '''Check if replica folder exist, if not then create it'''    
    if not os.path.isdir(replica):
        os.makedirs(replica)
        log_file(f'{replica} folder has been created')


def sync_files(source, replica):
    '''Copy the files from source folder to replica folder''' 
    source_files = os.listdir(source)
    for file in source_files:
        source_folder = source + "\\" + file
        if os.path.isdir(source_folder):
            if file not in os.listdir(replica):
                shutil.copytree(source_folder, replica + "\\" + file,  dirs_exist_ok=True)
                print(f'Folder {file} was added')
                log_file(f'Folder {file} was added')
                
        else:          
            if file not in os.listdir(replica):
                shutil.copy2(source+"\\"+file, replica)
                print(f'{file} is copied to replica folder')
                log_file(f'{file} is copied to replica folder')

        



def log_file(message):
    '''Prints information to the log_file'''
    log_information_from_file=open(args.log+"\\"+"LogFile.txt", "a", encoding="utf-8")
    log_information_from_file.write(message + " at " + time.ctime() + '\n')            





if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sync files between two folders')
    parser.add_argument("--source", type=str, help='Path to Folder with original files', required=True)
    parser.add_argument("--replica", type=str, help="Path to Folder with copied files", required=True)
    parser.add_argument("--log", type=str, help="Path to Logging File", required=True)
    args = parser.parse_args()

log_file("***Start of synchronization***")
check_folders_existance(args.source, args.replica)
sync_files(args.source,args.replica)