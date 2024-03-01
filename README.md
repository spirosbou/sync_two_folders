
# Two_Folders_Synchronization

Python script to synchronize two folders. You can run it periodically using crontab.


## Lessons-Learned
You learn how to manipulate files and folders. How to use argparse library
to provide command line arguments.

## Skills

Python

## Installation

Download and Install python on your machine

```bash 
  pip install python3
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/spirosbou/sync_two_folders.git
```

Go to the project directory

```bash
  cd "Your project directory"
```





## Crontab

1) Create your Python Script
2) Open Terminal
3) Write crontab -e to create crontab
4) Press i to launch edit mode
5) Write the schedule command * * * * * /usr/bin/python /path/to/file/<FILENAME>.py
6) Press esc to exit edit mode
7) Write :wq to write your crontab

**If you want to delete the running job:
1) Open Terminal
2) Run crontab -r 
