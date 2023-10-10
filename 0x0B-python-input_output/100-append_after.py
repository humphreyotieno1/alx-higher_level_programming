#!/usr/bin/python3
"""Define function that appends str after lines having keyword"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of a text file after each line"""
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_txt = ""
        for line in f:
            new_txt += line
            if search_string in line:
                new_txt += new_string
        f.seek(0)
        f.write(new_txt)
