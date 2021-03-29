# elephants_sort
## Description

This program is a solution to a problem, whose command is in the file instruction.pdf

## Documentation

Documentation created with the Sphinx tool. You can use documentation from the link https://mikul129.github.io/elephants_sort/ or location docs\index.html. Correctly launched documentation looks like this:
![image](https://user-images.githubusercontent.com/41323564/112475962-aee50e80-8d71-11eb-97d1-55f608f884a8.png)

## Files

dosc - folder with documentation files<br />
sphinx - folder with files for generate documentation<br />
test_data.py - folder with input and output test data<br />
instruction.pdf - file with the original task command<br />
main.py - file with the main functions of the program<br />
unit_tests.py - aplication unit tests<br />
quick_start.py - script for quick start program<br />

## Libraries

numpy==1.19.3

## Quick start

1. You must in cmd open location with files program. <br />
2. Type the command `python quick_start.py`<br />
3. In the next step you must type location file with input data. (For Example `tests_data\slo1.in`).

## Input data structure
The first line of input contains one integer
![image](https://user-images.githubusercontent.com/41323564/112841011-4747ff80-90a0-11eb-9d77-d8ac9a8baef3.png)
, meaning the number of elephants in the Byteotian Zoo. For simplicity, we assume that the elephants are numbered from 1 to n. The second line contains n integers (mi)
![image](https://user-images.githubusercontent.com/41323564/112841364-ac9bf080-90a0-11eb-95e6-ceb3bcab9c3e.png)
separated by single spaces and denoting the weights of individual elephants (expressed
in kilograms). The third line of input contains n distinct integers
![image](https://user-images.githubusercontent.com/41323564/112841070-59c23900-90a0-11eb-9195-768209247417.png)
separated spaces to denote the numbers of the elephants in sequence in the current alignment. The fourth line contains n distinct integers
![image](https://user-images.githubusercontent.com/41323564/112841095-5f1f8380-90a0-11eb-86de-b125d9d16f55.png)
, separated by single spaces and representing the numbers of subsequent elephants in the arrangement proposed by the director of the zoo. You can assume that the settings represented by the strings (ai) and (bi) aredifferent.

## Contact

mikulski.michal2@gmail.com
