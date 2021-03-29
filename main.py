"""
main.py
====================================
Main file, includes functions for alghoritms.
"""

import numpy as np
import sys
import os

def p(bi,P,Y):
    """
    Method for creating permutations.
  
    :param bi: [int] elephant number target setting
    :param P: [list] permutation
    :param Y: [list] the target position of the elephants
    :return: ai [int] the destination number of the elephant
    """    
    ai = P[Y.index(bi)]
    return(ai)

def simple_cycles(n,P,Y):
    """
    Method for permutation distribution for simple cycles.
  
    :param n: [int] number of elephants
    :param P: [list] permutation
    :param Y: [list] the target position of the elephants
    :return: C [list] simple cycles list
    :return: c [int] number of cycles
    """ 
    odw = np.zeros((n), dtype=bool)
    c = 0
    d = 0
    C = []
    for i in range(1,n+1):
        if odw[i-1] == False:
            row = []
            c = c+1
            x = i
            while odw[x-1] == False:
                d = d+1
                odw[x-1] = True
                row.append(x)
                x = p(x,P,Y)
            C.append(row)
    return(C,c)

def cycles_parameters(n,P,Y,M):
    """
    Method for calculation of cycle parameters.
  
    :param n: [int] number of elephants
    :param P: [list] permutation
    :param Y: [list] the target position of the elephants
    :param M: [str] weight of elephants
    :return: sum_Ci [list] sum weight of elephants in the cycle
    :return: min_Ci [int] the weight of the lightest elephant in the cycle
    :return: minimum [list] the weight of the lightest elephant
    :return: C [list] simple cycles list
    :return: c [int] number of cycles
    """ 
    
    C,c = simple_cycles(n,P,Y)
    minimum = np.inf
    sum_Ci = []
    min_Ci = []
    for i in range(1,c+1):
        sum_Ci_row = 0
        min_Ci_row = np.inf
        for e in C[i-1]:
            sum_Ci_row += M[e-1]
            min_Ci_row = min(min_Ci_row,M[e-1])
        sum_Ci.append(sum_Ci_row)
        min_Ci.append(min_Ci_row)
        minimum = min(M)
    return(sum_Ci, min_Ci, minimum, C, c)

def result(n,P,Y,M):
    """
    Method for calculation the number of movements.
  
    :param n: [int] number of elephants
    :param P: [list] permutation
    :param Y: [list] the target position of the elephants
    :param M: [list] weight of elephants
    :return: w [int] minimum from result methods
    """ 
    sum_Ci, min_Ci, minimum, C, c = cycles_parameters(n,P,Y,M)
    w = 0
    for i in range(1,c+1):
        method1_Ci = sum_Ci[i-1] + (len(C[i-1]) - 2) * min_Ci[i-1]
        method2_Ci = sum_Ci[i-1] + min_Ci[i-1] + (len(C[i-1]) + 1) * minimum
        w += min(method1_Ci, method2_Ci)
    return(w)

def alghorithm(file):
    """
    Method for implementing the algorithm.
  
    :param file: [str] input file
    :return: result [int] minimum from result methods
    """
    with open(file,"rb") as f:
        n = int(f.readline())
        M = f.readline()
        M = list(map(int, M.split()))
        P = f.readline()
        P = list(map(int, P.split()))
        Y = f.readline()
        Y = list(map(int, Y.split()))
    f.close()
    result_alg = result(n,P,Y,M)
    return(result_alg)