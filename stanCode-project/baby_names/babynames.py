"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name not in name_data:
        name_data[name] = {year: rank}
    else:
        if year in name_data[name]:
            if int(name_data[name][year]) > int(rank):
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    # Import the Year from the first line in the file.
    with open(filename, 'r') as f:
        line_num = 0
        for line in f:
            line_num += 1
            # In order the get the year at the first line in each file.
            if line_num == 1:
                year = line.split( )[0]

            # In order the get the rank of the male and the female at the other lines in each file.
            else:
                info_lst = line.split(',')
                rank = info_lst[0]
                name1 = info_lst[1]
                name2 = info_lst[2]
                rank = str(rank.strip( ))
                name1 = str(name1.strip( ))
                name2 = str(name2.split( ))
                name2_final = ''
                for i in range(len(name2)):
                    if (name2[i].isalpha()) == True:
                        name2_final += name2[i]

                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2_final)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for i in range(len(filenames)):
        filename = filenames[i]
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []
    # Situation 1: If the words you input to search don't include the first word in the name.
    target_lower = target.lower()

    # Situation 2: If the first word you input to search includes the first word in the name.
    target_first = ''
    for i in range(len(target)):
        if i == 0:
            target_first += target[i].upper()
        else:
            target_first += target[i].lower()

    # In order to ensure whether we input the exact words that are within the name in dataset.
    for key, value in sorted(name_data.items(), key=lambda t: t[0]):
        if target_lower in key:
            names += [key]
        if target_first in key:
            names += [key]
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
