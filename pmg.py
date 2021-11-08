import pandas as pd
import os
import sys
from pathlib import Path

""" THIS COMMAND IS OPTIONAL """
#if you already have this file and want to rewrite it with new data then delete it or if you want to append data to the existing file, then below command can be commented
if os.path.exists("output.csv"):
  os.remove("output.csv")

"""MAIN CODE STARTS HERE"""
# Defining the function to combine csv's

def combine_csv(csvfile):

#TO CHECK FOR POSSIBLE ERRORS
    
#To check if the file exists
    if not len(csvfile):

        return None
      
    for i in range(len(csvfile)):
        
        _, fileext = os.path.splitext(csvfile[i])

# To check if the file format is correct i.e.,(.csv)
        if fileext!= '.csv':
            raise Exception('File extension is not correct(it should be CSV)')
           
#Checking if the path of the file is correct 
        filepath = Path(csvfile[i])

        if not filepath.exists():
            raise IOError('File doesnt exist')
            
#BUILDING THE NEW COLUMN

    for i in range(len(csvfile)):
        
#To obtain the file name
        file_name = csvfile[i].split('/')[-1]

#Creating chunks to reduce storage and process files faster

        for block in pd.read_csv(csvfile[i], chunksize=10e5):
            
            block['filename'] = file_name
            if i==0:
                print(','.join(block.columns))
            print(block.to_csv(header=False, index=False,chunksize=10e5))

# IF YOU WANT TO SAVE THIS FILE LOCALLY ON YOUR SYSTEM, ELSE BELOW CODE CAN BE COMMENTED OUT
            block.to_csv('/Users/amanchaturvedi/desktop/output.csv', index=False,chunksize=10e5,mode='a')


# Main Function

if __name__ == '__main__':
   
    combine_csv(sys.argv[1:])