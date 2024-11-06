# OverTheWire-bandit Level 3 Writeups
## Method 1: 
Download bandit_level_3.py and run the file.
#### Output
    inhere

    total 24
    drwxr-xr-x  3 root root 4096 Sep 19 07:08 .
    drwxr-xr-x 70 root root 4096 Sep 19 07:09 ..
    -rw-r--r--  1 root root  220 Mar 31  2024 .bash_logout
    -rw-r--r--  1 root root 3771 Mar 31  2024 .bashrc
    -rw-r--r--  1 root root  807 Mar 31  2024 .profile
    drwxr-xr-x  2 root root 4096 Sep 19 07:08 inhere
    2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

## Method 2:
### 1. using ssh connecting server
    ssh bandit3@bandit.labs.overthewire.org -p 2220
    password: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
### 2.check the file in server
    $ls
    inhere
### 3. entry inhere
    $cd inhere
### 4.find the hidden file
    $ls -la
    total 24
    drwxr-xr-x  3 root root 4096 Sep 19 07:08 .
    drwxr-xr-x 70 root root 4096 Sep 19 07:09 ..
    -rw-r--r--  1 root root  220 Mar 31  2024 .bash_logout
    -rw-r--r--  1 root root 3771 Mar 31  2024 .bashrc
    -rw-r--r--  1 root root  807 Mar 31  2024 .profile
    drwxr-xr-x  2 root root 4096 Sep 19 07:08 inhere
### 4.open the hidden file
    $cat ...Hiding-From-You
    2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

