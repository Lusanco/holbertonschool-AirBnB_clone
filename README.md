# HBNB Project

This project aims to create an interpreter for managing data using Python. It provides a command-line interface for creating, updating, deleting, and showing instances of various classes.

# Installation

1. Clone the repository:
`git clone <repository-url>`

2. Navigate to the project directory:
`cd <project-directory>`

3. Run the console.py file:
`./console.py`

4. You will be greeted with a prompt '(hbnb)', where you can enter commands to interact with the application. Here are some example commands:

To create a new instance:
`(hbnb) create BaseModel`

To show an instance:
`(hbnb) show BaseModel <instance-id>`

To destroy an instance:
`(hbnb) destroy BaseModel <instance-id>`

To update an instance:
`(hbnb) update BaseModel <instance-id> <attribute-name> <attribute-value>`

To list all instance of a class:
`(hbnb) all BaseModel`

# File Structure

The project contains the following files:

- 'console.py': The main Python file containing the command-line interface (CLI) for interacting with the application.
- user.py: Defines the User class that inherits from BaseModel.
- file_storage.py: Defines the FileStorage class responsible for serializing and deserializing instances to and from a JSON file.
- base_model.py: Defines the BaseModel class that serves as the base class for other classes in the project.
- __init__.py: Initializes the project as a Python module.
- Other files: Define classes such as Amenity, City, Place, Review, and State, all of which inherit from BaseModel.

# Authors
- [Luis Santiago](https://github.com/Lusanco)
- [Livan Hernandez](https://github.com/Livanhernandez)
