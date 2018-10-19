# spiral_matrix

This Python script is a solution to the spiral matrix problem, which is a common benchmark problem for developers. The spiral matrix problem is where a matrix must be traversed in a "spiral" path and returned as a list. An example is below:

![alt text](http://1.bp.blogspot.com/-CD9C_7oeI3I/VgwL3AO-IeI/AAAAAAAACBc/EG-WAf-y_7E/s1600/spiral-circular-matrix.jpg)
>Image Source: http://1.bp.blogspot.com/-CD9C_7oeI3I/VgwL3AO-IeI/AAAAAAAACBc/EG-WAf-y_7E/s1600/spiral-circular-matrix.jpg

## Installation:

### Requirements:
This script was developed using Python 3.6. For best performance, Python 3.6 or greater is required.

### Installing The Script:
1. Clone the repository to your machine using git:
>git clone https://github.com/will-huynh/spiral_matrix.git

2. Go to the cloned directory on your local machine and check for the latest version using git:
>Navigate to the cloned spiral_matrix folder

>git branch master

>git pull

## Using The Script:
The script can be used in a variety of ways including the system terminal, Python interactive interpreter, and execution through other scripts.

### Use Through The System Terminal
First, navigate to the script directory. The script is then run with a terminal command using three required arguments: the matrix as a list of numbers, the number of columns the matrix contains, and the number of rows the matrix contains. 

For a 3 x 3 matrix:
>[0, 1, 2]

>[3, 4, 5]

>[6, 7, 8]

The following commands are used:
>python3 spiral_matrix.py -m 0 1 2 3 4 5 6 7 8 -r  3 -c 3
or:
>python3 spiral_matrix.py --raw_matrix 0 1 2 3 4 5 6 7 8 --rows 3 --columns 3

### Use Through the Python Interactive Interpreter or Other Scripts
To use the script through the interactive interpreter or other scripts, first import the module:
>import /<PATH_TO_REPO>/spiral_matrix

Alternatively, you could add the script to your PYTHONPATH using the Python command:
>sys.path.append("/<PATH_TO_REPO>/spiral_matrix.py")

Afterwards you can use the script with:
import spiral_matrix

The Python command to run the script for the matrix above is:
>spiral_matrix.run([[0,1,2],[3,4,5],[6,7,8]])
