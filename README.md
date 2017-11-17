# Cheat Detector

Does a student-against-student comparison of multiple-choice-test answers and reports results in binary format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For the very least, you should have the following software up and running:

- [Git] ;
- [(Ana| Mini)conda].

### Installing

First, you will need to clone this repo as so:
```sh
$ git clone git@github.com:19r3ka/cheat-detector.git 
```

Once **Conda** is installed, and the clone process complete, install all required dependencies simply by running the following command in the shell:
```sh
$ cd cheat-detector/
$ conda env create
```
Afterwards, activate the newly setup work environment as so:
```sh
$ activate cheat-detector
```

**And you are all set to run some analysis :)**

### Usage
All the script needs to do its magic are properly formatted CSV files as so:

| csid | booklet | idstu | p1 | p2 | ... |
| ---- | ------- | ---- | -- | -- | --- |
| 10065-65 | 3 | 134 | 4 | 6 | ... |
| 10054-69 | 2 | 541 | 7 | 6 | ... |

#### From the command line

##### feeding it CSV files
! WARNING: It is a good practice to format file names without empty spaces or dots within. E.g: Good alternatives to `file name.csv` or `file.name.csv` are `filename.csv`, `file-name.csv` or even `file_name.csv`

```sh
$ python run.py file1.csv file2.csv ...file_n.csv
```

##### piping in data from another program
You could also pipe in a buffer containing comma-separated data, e.g. output data from, say, an R script:

```sh
$ some_other_program | python cheat-detector.py
```

or

```sh
$ python cheat-detector.py < some_csv_data
```

### Running the tests

Test support, instructions, and examples coming soon-ish!

## Deployment

This section will very soon feature additional notes about how to deploy this app on a live system.

## Contributing

Feel free to fork or clone this repo while I put together details on the code of conduct, and the process for submitting pull requests.

## Versioning

We use SemVer for versioning. For the versions available, see the tags on this repository.

## Authors

Yem Ahiatsi

## License

This project is licensed under the GNU GPL V.3 License - see the LICENSE file for details.

## Acknowledgments

Hat tip to anyone who's code was used

   [Git]: <https://git-scm.com/downloads>
   [(Ana| Mini)conda]: <https://conda.io/docs/user-guide/install/index.html#regular-installation>
