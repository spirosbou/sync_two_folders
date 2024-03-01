import os
import argparse




def check_folders_existance(source):
    '''Check if source folder exist'''
    if not os.path.isdir(source):
        raise argparse.ArgumentError(None, "Source folder does not exist")





if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sync files between two folders')
    parser.add_argument("--source", type=str, help='Path to Folder with original files', required=True)
    parser.add_argument("--replica", type=str, help="Path to Folder with copied files", required=True)
    parser.add_argument("--log", type=str, help="Path to Logging File", required=True)
    args = parser.parse_args()

check_folders_existance(args.source)