''' Processes data '''

import pandas as pd

class DataProcessor(object):
    @classmethod
    def compare(cls, input1, input2):
        ''' Reports similarities in 2 lists in binary format '''

        if len(input1) != len(input2):
            error = 'Length mismatch: student {}: {}, student {}:\
                {}'.format(
                        input1['idstu'],
                        len(input1),
                        input2['idstu'],
                        len(input2))
            raise Exception(error)

        ''' (bool)*1 => 0: false, 1: true'''
        return (input1['p1':] == input2['p1':])*1


    @classmethod
    def concat(cls, row_list):
        ''' Creates dataframe from a series of rows '''
        return pd.DataFrame(row_list)


    @classmethod
    def estimate_ops(cls, data):
        ''' Estimate number of ops needed to process data '''
        total = 0
        i = data.shape[0]

        while i > 0:
            i -= 1
            total += i

        return total


    @classmethod
    def format_row(cls, input1, input2, analysis):
        ''' Formats output row '''

        if (input2['csid'] != input1['csid'] or input1['booklet'] !=
        input2['booklet']):
            error = 'Students to process should be from same school and\
            booklet'
            raise Exception(error)

        return pd.Series([
            input1['csid'],
            input1['booklet'],
            input1['idstu'],
            input2['idstu']], index =
            ['csid', 'booklet', 'idstu1', 'idstu2']).append(analysis)

