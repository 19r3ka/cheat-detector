''' Runs the main algorithm on the main thread '''

# Add the 'sample' directory to path to import files simply
import os, sys
sys.path.append(os.path.abspath('./sample/'))

import multiprocessing as mp
import pandas as pd
from Queue import Queue

from dprocessor import DataProcessor as dp
from parser import Parser
from progressbar import ProgressBar
from worker import Worker

def main():
    # Create an output directory as to not pollute the script folder
    directory = 'results'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # splice data by booklet by school
    columns = ('csid', 'booklet')
    groups = Parser().groupby(columns)

    # Create progress bar for reporting data processing updates
    bar_length = 30
    status = 'Ready to process data!'
    progress_bar = ProgressBar(bar_length, 0, status)

    r = Queue() # Stores the processed data
    q = Queue() # Stores the initial data to process

    # Create Thread workers for parallelism using system cpu cores
    for core in xrange(mp.cpu_count()):
       worker = Worker(core + 1, q, r,

           # Add function to format row with computed similarities
           lambda x, y: dp.format_row(x, y, dp.compare(x, y)),

           # Add progress bar to worker to enable computation tracking
           progress_bar)
       worker.daemon = True
       worker.start()

    # Start processing the data
    for name, data in groups:
        school, booklet = name

        # Prepend 'id' to the list of dataframe header
        col_names = ['id']
        col_names.extend(list(data))

        # Calculate the number of iterations needed to process data
        total_ops = dp.estimate_ops(data)

        # Set the goal of the progressbar
        progress_bar.set_goal(total_ops)

        # Record index of first row in group
        # given that indices seem to be cumulative
        # over the whole dataset
        first_id = int(data.iloc[0].name)

        # Iterate over the data for line-by-line analysis
        for input1 in data.itertuples():
            i = int(input1[0]) - first_id + 1
            for input2 in data.iloc[i:].itertuples():
                q.put((
                    pd.Series(input1, index=col_names),
                    pd.Series(input2, index=col_names))) # Add data to compare to queue as tuple

        # Wait for all the work queue to be processed
        q.join()

        # Concatenate all data processed into one dataframe
        data_to_save = dp.concat([r.get() for i in xrange(r.qsize())])

        # Save data to file
        filename = 'school_{}-booklet_{}.csv'.format(school, booklet)
        output_path = os.path.join(directory, filename)

        data_to_save.apply(Parser().to_int).to_csv(output_path)
        print '\nData saved to {}\n'.format(output_path)

if __name__ == '__main__':
    main()

