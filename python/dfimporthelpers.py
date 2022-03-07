# By: David Fahnestock
# This file includes helper utility functions for importing csv files into dataframes

import os
from os.path import join, isdir
from os import mkdir, path

import glob

import pandas as pd


#-----------------------------------------------------
# Function: load_csvs_to_df
# Loads all CSVs in the src_dir to a dataframe that
# is returned by the function.  If col_names is 
# supplied, the header rows in each file are ignored
# and the names from col_names are used instead
def load_csvs_to_df(src_dir: str, col_names: list):    
    os.chdir(src_dir)
    
    # Get all csv filenames from th src directory
    filenames = [i for i in glob.glob('*.{}'.format('csv'))]
    
    # Now load and merge all of the csv's into a dataframe
    if col_names != None:
        df = pd.concat([pd.read_csv(f, low_memory=False, names=col_names, skiprows=1) for f in filenames])
    else:
        df = pd.concat([pd.read_csv(f, low_memory=False) for f in filenames]) 
        
    return df

