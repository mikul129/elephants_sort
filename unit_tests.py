"""
unit_tests.py
====================================
The file includes unit tests.
"""

from main import alghorithm

def test_result(file):
    """
    Method for test result from input file.
  
    :param file: [str] input file
    """    
    file_data_input = file + ".in"
    result = alghorithm(file_data_input)
    file_correct_result = file + ".out"
    with open(file_correct_result) as f:
        correct_result = int(f.readline())
    f.close()
    if correct_result == result:
        print(file_data_input, "OK")
    else:
        print(file_data_input, "Error, wrong result!")

"""
Unit tests process.
"""
for x in range(1,5):
    file = r"C:\Users\User\Desktop\elephants_sort\test_data\slo"+str(x)
    test_result(file)