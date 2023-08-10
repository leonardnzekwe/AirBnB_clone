# AirBnB Clone
ALX SWE AirBnB Clone Project

![AirBnB Clone](images/hbnb.png)

### Authors
- [@leonardnzekwe](https://www.github.com/leonardnzekwe)
- [@rahma-cloud](https://www.github.com/rahma-cloud)

## 1.0: The console
It is a command interpreter used to create, manage, store and persist our objects.

### 1.1: Features:
- creates the data model
- manages (create, update, destroy, etc) objects via a console / command interpreter
- stores and persists objects to a file (JSON file)

### 1.2: Aim:
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between "My object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won’t have to pay attention (take care) of how our objects are stored.

This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

The console will be a tool to validate this storage engine

![The Console](images/console.png)

### 1.3: Startup:
Interactively:  `./console.py`

Non-interactively: `<input cmd> | ./console.py`

### 1.4: Usage: 
Execute `help` for list of commands to display

### 1.5: Examples:
Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## 2.0: Data Model
![Data Model](images/data_model.png)
