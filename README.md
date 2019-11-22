<img align="center" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png"  width="100%"/>

# AirBnB clone - The console

This is the first step towards building a first full web application: the AirBnB clone.

## Description

This console was built for an object managing specific use-case, with functionalities like:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

## Functionality

1. Clone this repository

```
$ git clone https://github.com/luiseduardiazc/AirBnB_clone
```

2. Change directory to "AirBnB_clone"

```
$ cd AirBnB_clone
```

3. Open the console

```
$ ./console.py
```

## Usage

| Command | Use | Description |
| --- | --- | --- |
| help | ```(hbnb) help or (hbnb) help [COMMAND]``` | Displays console commands or specific command usage |
| quit or EOF | ``` (hbnb) quit ``` | Quit command to exit the program |
| create | ``` (hbnb) create [CLASS] ``` | Creates a new instance of a class |
| show | ``` (hbnb) show [CLASS] [ID] ``` | Prints the string representation of an instance |
| destroy | ``` (hbnb) destroy [CLASS] [ID] ``` | Deletes an instance based on the class name and id |
| all | ``` (hbnb) all or (hbnb) all [CLASS] ``` | Prints all string representation of all instances or a specific instance |
| update | ``` (hbnb) update [CLASS] [ID] [ATTRIBUTE] [VALUE] ``` | Update instance attribute and save changes to JSON file |

The console has two possible forms:

**INTERACTIVE**

Where the console stays on a loop prompting the user's input, then executes it, after executing the output is shown and finally the console goes back to prompting.

```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

**NON INTERACTIVE**

Where the console doesn't loop, it just executes the written command on echo and closing when finished.

```
(hbnb) echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```
---

**EXAMPLES**
(Interactive mode)

* Creation of an instance

```
(hbnb) create User
59e76fde-f140-471f-a966-92ffb121ed84
(hbnb)
```

* Show created instance 

```
(hbnb) User 59e76fde-f140-471f-a966-92ffb121ed84
[User] (59e76fde-f140-471f-a966-92ffb121ed84) {'id': '59e76fde-f140-471f-a966-92ffb121ed84', 'updated_at': datetime.datetime(2019, 11, 11, 15, 4, 15, 477387), 'created_at': datetime.datetime(2019, 11, 11, 15, 4, 15, 477414), '__class__': 'User'}
(hbnb)
```

* All with previously create City ( ```(hbnb) create City``` )

```
(hbnb) all
["[City] (fd6c1294-c8d3-4f52-b163-f39387df721a) {'id': 'fd6c1294-c8d3-4f52-b163-f39387df721a', 'updated_at': datetime.datetime(2019, 11, 10, 21, 8, 19, 636294), 'created_at': datetime.datetime(2019, 11, 10, 21, 8, 19, 636307), '__class__': 'City'}", "[User] (59e76fde-f140-471f-a966-92ffb121ed84) {'id': '59e76fde-f140-471f-a966-92ffb121ed84', 'updated_at': datetime.datetime(2019, 11, 11, 15, 4, 15, 477387), 'created_at': datetime.datetime(2019, 11, 11, 15, 4, 15, 477414), '__class__': 'User'}"]
(hbnb)
```

* Update email for User

```
(hbnb) update User 59e76fde-f140-471f-a966-92ffb121ed84 email "mrdoom.official@gmail.com"
(hbnb)
```

* All just for User
    
```
(hbnb) all User
["[User] (03c28b38-c4be-422a-a75b-b9a576ce57e0) {'id': '03c28b38-c4be-422a-a75b-b9a576ce57e0', 'updated_at': datetime.datetime(2019, 11, 10, 21, 8, 2, 993936), 'created_at': datetime.datetime(2019, 11, 10, 21, 8, 2, 993958), '__class__': 'User'}", "[User] (59e76fde-f140-471f-a966-92ffb121ed84) {'id': '59e76fde-f140-471f-a966-92ffb121ed84', 'updated_at': datetime.datetime(2019, 11, 11, 15, 4, 15, 477387), 'created_at': datetime.datetime(2019, 11, 11, 15, 4, 15, 477414), '__class__': 'User', 'email': 'mrdoom.official@gmail.com'}"]
(hbnb)
```

* Remove User

```
(hbnb) User 59e76fde-f140-471f-a966-92ffb121ed84
(hbnb)
```

* Show deleted instance User

```
(hbnb) show User 59e76fde-f140-471f-a966-92ffb121ed84
** no instance found **
(hbnb)
```

## Files

This is a table with the files and their respective description used to create the console.

| File | Description |
| --- | --- |
| console.py | Module that supports the console behavior |
| base_model.py | Module used as base class for files below |
| city.py | Module that manages City |
| place.py | Module that manages Place |
| review.py | Module that manages Review |
| state.py | Module that manages State |
| user.py | Module that manages User |
| file_storage.py | serialization-deserialization module |

## Version
* 1.0
(11 | 11 | 2019) First version

## Authors

Luis Eduardo Díaz <luis.diaz.car@gmail.com>

Camilo José Villegas Jiménez <mrdoom.official@gmail.com>
