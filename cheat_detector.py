''' Cheat Detector One-file Code '''

#-*- coding: utf-8 -*-

from sys import argv, exit
import os.path
import pandas as pd

def to_int(x):
    ''' Converts numeric values to int '''
    try:
        return x.astype(int)
    except:
        return x

# Read file path from command line
csv_file = argv[1]

# Check if the file exists or not
if os.path.isfile(csv_file):
    # Read the data into a dataframe
    data =  pd.read_csv(csv_file)

    # Create subsets of data grouping by school and booklet
    for school_id in data.csid.unique():
        for booklet_id in data.booklet.unique():
            subset = data.loc[(data['csid'] == school_id) & (data['booklet'] ==
               booklet_id)]

            # log
            print 'Analyzing data from school: {}, booklet: {}'\
                .format(school_id, booklet_id)

            # Compute length of subset
            subset_length = len(subset.index)

            # Create columns' namelist
            old_header = list(subset)
            output_header = ['csid', 'booklet', 'idstu', 'idstu2']
            new_header = output_header + old_header[old_header.index('p1'):]

            # Create empty dataframe
            df = pd.DataFrame(columns = new_header)

            # Loop over the whole subset...
            for i in xrange(subset_length):
                base_student = subset.iloc[i]
                base_student_id = base_student['idstu']
                # ... Then loop again starting one row below main loop's row
                for j in xrange(i + 1, subset_length):
                    test_student = subset.iloc[j]
                    test_student_id = test_student['idstu']

                    # log
                    print 'Comparing student ids: {} and {}'.format(base_student_id,
                            test_student_id)

                    # Only compare when both data Series have same length
                    if len(base_student) == (len(test_student)):
                        # Compare two students' test results for similarities
                        # (bool)*1 => 0: false, 1: true
                        similarities = (base_student['p1':] ==
                                test_student['p1':])*1

                        # Format the row
                        row = pd.Series([school_id, booklet_id,
                            base_student['idstu'],
                            test_student['idstu']], index =
                            output_header).append(similarities)

                        # Append the row
                        df = df.append(row, ignore_index = True)
                    else:
                        # TODO: Report the length-mismatch case
                        print 'Length Mismatch Error: {} and {} on booklet {} from school {}'.format(base_student['idstu'],
                                test_student['idstu'], booklet_id, school_id)

            # Save dataframe to CSV format
            output_file = 'Results_booklet_{}_school_{}'.format(booklet_id,
                    school_id)

            # Save all digit as integer
            print 'Data saved to ' + output_file
            df.appy(to_int).to_csv(output_file)
else:
    # Properly exit the script
    print 'Please provide a valid CSV file as first argument!'
    exit(404)



