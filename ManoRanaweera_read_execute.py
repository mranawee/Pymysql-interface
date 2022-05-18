#!/usr/bin/python
import pymysql
import sys

# START FUNCTION DEFINITIONS
def read_query(filename):
    # open the file
    f = open(filename, 'r')
    
    # initialize a variable (to store the query) as empty string
    query = ''
    
    # concatenate each line (remove \n) to the sequence
    for line in f:
        stripLine = line.rstrip('\n')
        query += stripLine
    
    # close the file
    f.close()
    
    # return the sequence
    return(query)

def execute_query(dtbs,usrnm,pswd,query):
    
    
        
    # connect to the database
    connection = pymysql.connect(host='bioed.bu.edu', 
                                 port=4253,
                                 user = usrnm,
                                 database = dtbs,
                                 password = pswd)
                                 
    
    # get cursor
    cursor = connection.cursor()
    
    # run query
    try:
        cursor.execute(query)
    except pymysql.Error as e:
        print(e)
    # fetch results 
    result = cursor.fetchall()
    
    
    # close the connection
    connection.close()
    
    # return the results
    return(result)
	


# FUNCTIONS FINISHED


# THIS IS THE MAIN BODY OF CODE THAT WILL CALL THE FUNCTIONS:

# get arguments from system argument list
dtbs = sys.argv[1]
usr  = sys.argv[2]
pswd = sys.argv[3]
filename = sys.argv[4]

# parse the query file using function read_query
parsed = read_query(filename)

# execute the query and get the results
execute = execute_query(dtbs, usr, pswd, parsed)

# print the results, one row at a time
print(execute)