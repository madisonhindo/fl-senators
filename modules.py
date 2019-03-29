import csv

def convert_to_dict(filename):
    """
    Convert a CSV file to a list of Python dictionaries.
    """

    datafile = open(filename, newline='')

    my_reader = csv.DictReader(datafile)

    list_of_dicts = []
    for row in my_reader:
        list_of_dicts.append( dict(row) )


    datafile.close()

    return list_of_dicts


def make_ordinal(num):
    """
    Create an ordinal (1st, 2nd, etc.) from a number.
    """
    base = num % 10
    if base in [0,4,5,6,7,8,9] or num in [11,12,13]:
        ext = "th"
    elif base == 1:
        ext = "st"
    elif base == 2:
        ext = "nd"
    else:
        ext = "rd"
    return str(num) + ext

def test_make_ordinal():
    for i in range(1,41):
        print(make_ordinal(i))

def search_the_list(list):
    for item in list:
        if "Republican" in item['Political-party']:
            print(item['Senator'] + " is a Republican.")
    for k in list[0].keys():
        print(k)


if __name__ == '__main__':
    test_make_ordinal()
    senator_list = convert_to_dict("florida-senators.csv")
    search_the_list(senator_list)
    print(make_ordinal(12))
    print(make_ordinal(32))
