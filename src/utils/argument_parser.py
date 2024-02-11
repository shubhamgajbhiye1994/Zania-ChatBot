"""
Argument Parser : input argument for main.py file
input argument:
    -file = input file name
    -io = embedding or index overwrite
    -q_list = question list to be answered
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-file','--filename', type=str,default="handbook.pdf",\
                    help="file name on which search perform")
parser.add_argument('-io','--index_overwrite', type=bool,default=False,\
                    help="index overwrite or not if present/not persent",choices=[True,False])
parser.add_argument('-q_list','--question_list',type=str,default=None,\
                    nargs='+',help="list of questions to which we need to provide answers")

args = parser.parse_args()