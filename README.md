[link](https://i.imgur.com/X8EA2Zv.png)

## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

### Command interpreter funcionalities:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Execution
## Execution
The console executes in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```
But also in non-interactive mode: (like the Shell project in C)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create

        Create command to create a new instance according Class name.
        Print the assigned id.
        Usage: create <class name>
        Classes: [BaseModel, User, Place, State, City, Amenity, Review]
        
(hbnb) 
(hbnb) quit
$
```
## Supported commands
|Command| Description |
|--|--|
| **create** | Creates a new instance based on the [class name], saves it (to a JSON file) and prints the [ID]. `$ create BaseModel`
|
| **show** | Prints the string representation of an instacnce based on the [class name] and [ID]. `$ BaseModel 1234-1234-1234-1234` | 
| **destroy** | Deletes an instance based on the [class name] and [ID] by adding or updating attribute (saves changes into a JSON file). `$

