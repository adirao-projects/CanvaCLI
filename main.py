import requests
import argparse
import fuzzywuzzy as fw
import numpy as np
import eel
import pandas as pd
import sqlite3

def connect_to_canva(token):
    return NotImplementedError

def add_file(path):
    return NotImplementedError

def upload_file(idx):



def get_assignment(classid, assignmentid):
    return NotImplementedError

def get_list_classes():
    return NotImplementedError

def get_list_assignments(time_frame=None):
    return NotImplementedError

if __name__ == "__main__":
    print("WIP")
