### INSIGHT H1B STATISTICS CHALLENGE 

# Procedure
Python language was used to solve the insight challenge. Following is the approach 
I have used to solve the insight H1B statistics challenge:
1. Read h1b_counting.csv file and store the necessary field data by getting their index values. 
2. While reading the h1b_counting.csv file, to accomodate for different header names in 
different csv files, I have tried finding a pattern and searching the common string in headers. 
For example I observed H1B_FY_2014 and H1B_FY_2015 datafile, the column with certified status is 
labelled as 'STATUS' in H1B_FY_2014 whereas 'CASE_STATUS' in H1B_FY_2015. So, the common string 
'STATUS'was used to search this field in this case. Similar logic has been followed to search 
'WORK STATE' and 'SOC NAME' attribute.
3. The count for each field in 'STATE' and 'OCCUPATION' was stored in a data dictionary if their 
corresponding 'STATUS' was 'CERTIFIED'. The fields were sorted in descending order of values and if
values are same sorted alphabetically by key.
4. Top 10 fields were selected and their corresponding percentages were calculated and rounded to 
1 decimal.
5. Finally the results were written in two .txt files
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
Each line of the `top_10_states.txt` file will have the following fields:
1. __`TOP_STATES`__: State where the work will take place
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for work 
in that state.
3. __`PERCENTAGE`__: % of applications that have been certified in that state compared to total 
number of certified applications regardless of state.
* `top_10_states.txt`: Top 10 states for certified visa applications
Each line of the `top_10_occupations.txt` file will have the following fields: 
1. __`TOP_OCCUPATIONS`__: The occupation name associated with an application's 
Standard Occupational Classification (SOC) code.
2. __`NUMBER_CERTIFIED_APPLICATIONS`__: Number of applications that have been certified for that 
occupation.
3. __`PERCENTAGE`__: % of applications that have been certified for that occupation compared to 
total number of certified applications regardless of occupation. 

# How to run the program
Use the following procedure to run the program
1. Download the H1B_Counting Folder
2. Open command terminal and check if python is installed. If not, install Python.
3. Change directory to where H1B_Counting folder is located
3. Type *`chmod 777./run.sh `to give file permissions
4. Type *`./run.sh` to execute the file
5. Output files will be created and stored in output folder. 
5. Go to output folder to view output files. Program will create 2 output files:
* `top_10_occupations.txt`: Top 10 occupations for certified visa applications
* `top_10_states.txt`: Top 10 states for certified visa applications
6. Now, to run the tests, change directory to insight_testsuite
7. Type *`chmod 777./run_tests.sh `to give file permissions
8. Type *`./run_tests.sh` to execute the file. This will show how many of the 
given test cases passed by thr program
 
