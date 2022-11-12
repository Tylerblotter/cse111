import csv

def main():
    student_dict = read_dict("students.csv", 0)
    number = input("Please enter an I-Number (xxxxxxxxx): ")
    number = number.replace("-","")
    if len(number) > 9:
        print("Too many digits")
        return
    elif len(number) < 9:
        print("Too few digits")
        return

    valid_number = False
    for keys in student_dict:
        if number == keys:
            valid_number = True
    if valid_number:
        name = student_dict[number][1]
        print(name)
    else:
        print("No such student")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}


    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    
    return dictionary



if __name__ == "__main__":
    main()