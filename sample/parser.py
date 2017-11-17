#-*- coding: utf-8 -*-

''' Defines the Data Loader class '''
import sys
import pandas as pd

class Parser(object):
    ''' Parse CSV data '''

    def __init__(self, filenames=sys.argv[1:], stdin=sys.stdin):
        ''' Instantiate data from filenames given in command line or piped '''
        self.data = pd.DataFrame() # Create empty dataframe

        if len(filenames):
            # Concatenate all dataframes read from CSV files
            for filename in filenames:
                self.load(filename)

        # if piping data into the script
        if not stdin.isatty():
            self.load(stdin)


    def groupby(self, columns):
        ''' Group series by columns values '''
        return self.data.groupby(columns)


    def load(self, filename):
        ''' Adds content of CSV file to data '''
        self.data = pd.concat([self.data, pd.read_csv(filename)],
                ignore_index=True)
        return self


    def to_csv(self, filename):
        ''' Export data to CSV '''
        if not filename.endswith('.csv'):
            filename += '.csv'
        self.data.to_csv(filename)


    @classmethod
    def to_int(cls, x):
        ''' Converts numeric values to int '''
        try:
            return x.astype(int)
        except:
            return x

