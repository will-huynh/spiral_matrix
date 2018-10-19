from math import ceil
import argparse
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

streamHandler = logging.StreamHandler(sys.stdout)
streamHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

#Gets parameters to run output method for the given matrix
def get_properties(matrix):
    rows = len(matrix)
    for row in matrix:
        for i in range(0, rows):
            if len(row) is not len(matrix[i]):
                raise ValueError("Invalid matrix; length of columns is uneven.")
    columns = len(matrix[0])
    compare_rows_columns = rows >= columns
    if compare_rows_columns:
        final_x = rows
        final_y = rows - 1
    else:
        final_x = columns - 1
        final_y = rows - 1
    raw_list = [] #Stores the elements of the matrix into a list in ascending order
    for row in matrix:
        for entry in row:
            raw_list.append(entry)
    return columns, rows, final_x, final_y, raw_list

#Spirals the given matrix into a list
def output(columns, rows, final_x, final_y, raw_list):
    entry = 0
    list_len = len(raw_list)
    track_period = (0, True) #Tracks every pair of axis switches; amount and odd/even switch
    track_x = 0
    track_y = 0
    results = []
    while (track_x + track_y < final_x + final_y):
        if track_period[1]:
            if track_x < final_x:
                for x in range(0, columns - track_period[0]):
                    if not (entry == 0 and x == 0):
                        entry += 1
                    results.append(raw_list[entry])
                track_x += 1
            if track_y < final_y:
                for y in range(0, rows - track_period[0] - 1): #loop not dependent on entries of raw_list
                    entry += columns
                    results.append(raw_list[entry])
                track_y += 1
            track_period = (track_period[0] + 1, False)
        if not track_period[1]:
            if track_x < final_x:
                for x in range(0, columns - track_period[0]):
                    entry = entry - 1
                    results.append(raw_list[entry])
                track_x += 1
            if track_y < final_y:
                for y in range(0, rows - track_period[0] - 1):
                    entry = entry - columns
                    results.append(raw_list[entry])
                track_y += 1
            track_period = (track_period[0] + 1, True)
    return results

#Run the methods of this module separate from its status as the main script or not
def run(matrix):
    logger.info("Processing given matrix: {}".format(matrix))
    rows, columns, final_x, final_y, raw_list = get_properties(matrix)
    logger.info("""Retrieved matrix properties.
    >Rows: {0}
    >Columns: {1}
    >Final_x: {2}
    >Final_y: {3}
    >Matrix as a raw list: {4}""".format(rows, columns, final_x, final_y, raw_list))
    results = output(rows, columns, final_x, final_y, raw_list)
    logger.info("Spiraled matrix as a list: {}".format(results))
    return results

#Method runs if script is invoked through the command line; a simple parser is used for this scope (as opposed to a nested parser)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--raw_matrix', nargs='+', type=int, help='Matrix inputted as a raw list of numbers in the form "1 2 3 4 5 6 7 8 9" for a matrix [[1,2,3],[4,5,6],[7,8,9]]')
    parser.add_argument('-r', '--rows', type=int, help='Number of rows in the matrix')
    parser.add_argument('-c', '--columns', type=int, help='Number of columns in the matrix')
    args = parser.parse_args()
    raw_matrix, rows, columns = args.raw_matrix, args.rows, args.columns
    entry = 0
    matrix = []
    row = []
    logger.info("Building matrix.")
    for i in range(0, rows):
        for j in range(0, columns):
            row.append(raw_matrix[entry])
            entry += 1
        matrix.append(row)
        row = []
    logger.info("Matrix built: {}".format(matrix))
    run(matrix)

if __name__ == "__main__":
    main()
