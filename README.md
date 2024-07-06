
# List Creator and Updater

This Python script allows users to create, view, and update lists stored in CSV files. It uses the tabulate library to display data in a tabular format.


## Features

- Create a New List: Start a new list by specifying headers and rows of data.
- Add Data to an Existing List: Append new rows of data to an existing list.
- View an Existing List: Display the contents of an existing list.


## Requirements

- Python 3.x
- tabulate library (pip install tabulate)
## Usage
- Run the script:

    ```javascript
    python list_creator.py

    ```
    
-  Follow the on-screen instructions to create a new list, add data, or view an existing list




## Example
- Creating a New List:

    ```javascript
    Enter the operation number to perform:- 1
    Enter the file name: my_list.csv
    Enter the headers (comma-separated): Name,Age,Occupation
    Enter a row of data (comma-separated) or 'done' to finish: Alice,30,Engineer
    Enter a row of data (comma-separated) or 'done' to finish: Bob,25,Designer
    Enter a row of data (comma-separated) or 'done' to finish: done

    ```
- Adding Data to an Existing List:
    ```javascript
    Enter the operation number to perform:- 2
    Enter the file name: my_list.csv
    Enter a row of data (comma-separated) or 'done' to finish: Charlie,28,Teacher
    Enter a row of data (comma-separated) or 'done' to finish: done
    ```

- Viewing an Existing List:
    ```javascript
    Enter the operation number to perform:- 3
    Enter the file name: my_list.csv
    ```
## Authors

- [Atharva Inagle](https://github.com/Atharvingale)


The data will be displayed in a tabular format.

