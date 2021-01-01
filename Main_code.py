# Darwin Wilmut J

# importing necessary modules
import json
import os
from sys import getsizeof
from datetime import datetime


# path defined by user or default:current working directory (If path not set by user)
def set_path(way=os.getcwd()):
    global path
    path = way
    return

# Time to live (user defined)
def set_delay(time=360):
    global delay
    delay = time
    return

# default Time to live
delay = 360

# must run main function inorder to create and initialize json file
def main_function():
    try:
        f = open(os.path.join(path, "sample.json"))
    except FileNotFoundError:
        f = open(os.path.join(path, "sample.json"),"w")
        if os.stat("sample.json").st_size == 0:
            data = {}
            with open(os.path.join(path, "sample.json"), 'w') as outfile:
                json.dump(data, outfile, indent=4)

# For Time to live
def time_stamp():

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp

# Create
def create(key, value, seconds=0):
    size = getsizeof(value)
    len(key)
    if size <= 16000 and key.isalpha() and len(key) <= 32:
        f = open(os.path.join(path, "sample.json"),"r")
        dict = json.load(f)
        if bool(dict):
            if key in dict:
                return print('Data already Created')
            else:
                dict[key] =  value,seconds
                with open(os.path.join(path, "sample.json"),'w') as outfile:
                    json.dump(dict, outfile, indent=4)
                return print('Data Created')
        else:
            dict[key] =  value,seconds
            with open(os.path.join(path, "sample.json"), "w") as outfile:
                json.dump(dict, outfile, indent=4)
            return print('Data Created')
    else:
        return print(
            " File size must be within 16Kb \n Key must be String \n string length must be less than 32 characters")

# Read
def read(key):
    f = open(os.path.join(path, "sample.json"))
    dict = json.load(f)
    if bool(dict):
        if key in dict:
            value = dict[key]
            if value[-1] == 0:
                value[-1] = time_stamp()
                with open(os.path.join(path, "sample.json"), "w") as outfile:
                    json.dump(dict, outfile, indent=4)
                output = {key:value}
                return print(output)
            else:
                next_time = time_stamp()
                elapsed = next_time - value[-1]
                if elapsed <= delay:
                    output = {key: value}
                    return print(output)
                else:
                    delete(key)
        else:
            return print('No data found')
    else:
        return print('Empty File')

# Delete
def delete(key):
    f = open(os.path.join(path, "sample.json"))
    dict = json.load(f)
    if bool(dict):
        if key in dict:
            del dict[key]
            with open(os.path.join(path, "sample.json"), "w") as outfile:
                json.dump(dict, outfile, indent=4)
            return print('Data Deleted')
        else:
            return print('Data Unavailable')

    else:
        return print('Empty File')

