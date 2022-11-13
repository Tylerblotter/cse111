import csv

def main():
    products_dict = read_dictionary("products.csv", 0)
    print("All Products")
    print(products_dict)
    print()
    with open ("request.csv") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        print("Requested Items")
        for row_list in reader:
            product = products_dict[row_list[0]][1]
            print(f"{product}: {row_list[1]} @ {products_dict[row_list[0]][2]}")
            


def read_dictionary(filename, key_column_index):
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

    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    
    return dictionary
    

if __name__ == "__main__":
    main()