# HBNB Project

![AirbnbClone Logo](https://www.tabbykatz.com/hbnb.png)

### Table of content
- [Description](#description)
- [Installation](#installation)
- [Available commands](#available-commands)
- [File Structure](#file-structure)
- [Resources](#resources)
- [Authors](#authors)

## Description
This project is an Airbnb clone, a web application designed to provide a platform for users to rent or lease short-term lodging accommodations. Inspired by the popular Airbnb service, our clone offers similar functionality, allowing users to search for properties, view listings, make reservations, and manage their bookings.

This project aims to create an interpreter for managing data using Python. It provides a command-line interface for creating, updating, deleting, and showing instances of various classes.

# Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```bash
cd <project-directory>
```

3. Run the console.py file:
```bash
./console.py
```

4. You will be greeted with a prompt '(hbnb)', where you can enter commands to interact with the application. Here is how it should look:
```bash
(hbnb)
```

### Available commands
- 'quit' : Quit the program.
- 'EOF' : Exit the program.
- 'help' : Display available commands.
- 'create <class_name> : Create a new instance of the specified class.
- 'show >class_name> <instance.id>' : Show the string representation of an instance.
- 'destroy <class_name> <instance.id>' : Delete an instance based on the class name and ID.
- 'all [class_name]' : Print all string representation of instances or of a specific class.
- 'update <class_name> <instance.id> <attribute_name> "<attribute_value>"' : Update an instance attribute based on the class name and ID.
- 'count()' : Prints total number of instances of a class or all instances.

## File Structure

The project contains the following files:

- 'README.md' : Contains description of the project with instructions.
- 'console.py': The main Python file containing the command-line interface (CLI) for interacting with the application.
- user.py: Defines the User class that inherits from BaseModel.
- file_storage.py: Defines the FileStorage class responsible for serializing and deserializing instances to and from a JSON file.
- base_model.py: Defines the BaseModel class that serves as the base class for other classes in the project.
- __init__.py: Initializes the project as a Python module.
- Other files: Define sub-classes such as Amenity, City, Place, Review, and State, all of which inherit from BaseModel.

## Resources
- *[Args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)*
- *[Cmd module](http://docs.python.org/3.4/library/cmd.html)*
- *[Uuid module](http://docs.python.org/3.4/library/uuid.html)*
- *[Datetime](http://docs.python.org/3.4/library/datetime.html)*
- *[Unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)*
- *[Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)*
- *[Packages concept page](https://www.geeksforgeeks.org/python-packages/)*
## Authors
- [Luis Santiago](https://github.com/Lusanco)
- [Livan Hernandez](https://github.com/Livanhernandez)
