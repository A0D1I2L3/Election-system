
<div align="center">

  <h1> :trollface: Election System Using Python and tkinter :trollface:</h1>

</div>



## Introduction 

 - Completely programmed using Python and frontend using Python-tkinter
 - Data entry using Python and tkinter into Database managed by Mysql
  
## Features
- Fully controlled by admin 
- Result in Pie as well as Bar graphs
- Ability to host main database in one system and vote to it through other systems
  
## Requirements
  To actually use this project for your advantage you need the following
  - IQ >5
  - Ability to follow the instructions given

## Basic Setup
I believe you my friend , have all the requirements mentioned above

So lets get started 

### Install python 3 (preferably 3.10)
 Install [Python for windows](https://www.python.org/downloads/).
![Python download](assets/download_python.png)
After downloading double click and install
We can check if it is installed on our local machine by opening our device terminal or command prompt.
```sh
$ python --version
Python 3.10.7
```

### Download git repository

![Download repository](assets/download_repo.png)
Download ZIP and extract 

<div align="center">
OR</div>

### Clone git repository

Open git Bash.
Change the current working directory to the location where you want the cloned directory.

```sh
$ git clone https://github.com/A0D1I2L3/Election-system.git
> Cloning into 'Election-system'...
>remote: Enumerating objects: 135, done.
>remote: Counting objects: 100% (135/135), done.
>remote: Compressing objects: 100% (93/93), done.
>Receiving objects:  57% (77/135)used 104 (delta 33), pack-reused 0
>Receiving objects: 100% (135/135), 21.42 KiB | 4.28 MiB/s, done.
>Resolving deltas: 100% (59/59), done.
```

### Install All Required Python 3 Modules.

Modules

  - matplotlib
  - mysql-connector
  - tkinter

Use autorun.bat to install all required modules (Windows)

Double-Click on autorun.bat in Election-system.
![autorun install](assets/running_autorun.png)
Now, Click any key to close cmd window.


<div align="center">

OR

</div>

You can install modules using PIP
```
pip install MODULE-NAME
```


#### Fonts used
![Fonts](assets/fonts.png)
- Queental
- Consolas Bold

#### Installing fonts

Open fonts folder in the repository.
Install one by one
![installing fonts](assets/installing_fonts.png)

## Connectivity setup(mysql)

1. Open MySQL  Command Line Client and login with your password
2. Create a user with create option
    ```sh
    mysql> Create user 'root'@'%' identified by 'desired password';
    Query OK, 0 rows affected (0.11 sec)
    ```
    >Replace % with IP address for slected  IP
3. Grant privileges to user
    ```sh
    mysql> Grant select on database_name.* to 'root'@'%';
    Query OK, 0 rows affected (0.06 sec)
    ```
    ```sh
    mysql> Grant all privileges on database_name.* to 'root'@'%';
    Query OK, 0 rows affected (0.01 sec)
    ```
    Example :-
    ```sh
    mysql> Grant select,update on *.* to 'root'@'%';
    Query OK, 0 rows affected (0.02 sec)
    ```
4. ```sh
    mysql> flush privileges;
    Query OK, 0 rows affected (0.02 sec)
    ```
5. >Mysql user and passwd is 'root'and 'tiger' respectively, You might need to change in [adminside.py (line 8)](https://github.com/A0D1I2L3/Election-system/blob/master/adminside.py#L8) . You may need to change [voterside.py (line 5)](https://github.com/A0D1I2L3/Election-system/blob/master/voterside.py#L5) to
   
    
    ```sh
    import mysql.connector as broker
    mydb = broker.connect(host='<IP of admin system>',user='root', password='<yourpassword>')
    ```

You are basically done with the setup. enjoy voting (no one ever)

---

<div align=center>
<sub>Author: <a href='https://github.com/A0D1I2L3'>Adil Haneef M.K </a>,Sreerag Unni N,Athul Krishna K</a><br>    
<small>January, 2023</small> </sub>

</div>

----