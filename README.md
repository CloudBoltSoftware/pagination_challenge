# CloudBolt Pagination Challenge

Welcome! This repo is a programming challenge for applicants to work at CloudBolt. We request that you please do not share your answers publicly.

We recommend using Python 3, as that is the version we use here at CloudBolt. You can write your implementation in another language if you prefer. In that case, please include instructions on how to run your program with your submission.

When finished, please email your implementation to the hiring manager you have been communicating with up until now. If you don't get a timely response, feel free to send a follow-up email since it's possible the code may become caught in a spam filter.

# Problem

We are going to write a program that takes a CSV file as input, sorts the records in it, and outputs a specific page of records in CSV format. See the example below for details.

Given an input CSV file, like this example...

names.csv
```
First Name,Last Name
Elva,Gronchi
Alia,Philips
Eutropius,Lavoie
Leland,Salzwedel
Sandra,Yu
Oluwafunmilayo,Tisza
Thierry,Presley
Sati,Sherburn
Gwandoya,Berkowitz
Mia,Antonini
Anka,Lyon
Pamela,Duarte
Rayner,Amadori
```

When I run the program with the following arguments...
```
python main.py names.csv --sort-by "First Name" --page-size 10 --page-num 1
```

Then it prints the first page of 10 records, sorted by the "First name" column.

Expected output:
```
First Name,Last Name
Alia,Philips
Anka,Lyon
Elva,Gronchi
Eutropius,Lavoie
Gwandoya,Berkowitz
Leland,Salzwedel
Mia,Antonini
Oluwafunmilayo,Tisza
Pamela,Duarte
Rayner,Amadori
```

Loading the file, parsing the command line options, and printing the output is already handled by main.py. Your task is to implement the paginate function in pagination.py that takes the file contents and pagination options and returns the new contents to print. Your code must work for the general case, not just for the provided names.csv file.
