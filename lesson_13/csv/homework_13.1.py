import csv


# Reading CSV file and getting strings as list
def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


# Writing data in CSV file
def write_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


# Removing duplicates and writing in the result file
def remove_duplicates(file1, file2, result_file):
    # Reading files
    data1 = read_csv(file1)
    data2 = read_csv(file2)

    # Combining data from two files
    combined_data = data1 + data2

    # Removing duplicates, using set for unique strings
    unique_data = [list(x) for x in set(tuple(row) for row in combined_data)]

    # Writing unique strings in result file
    write_csv(result_file, unique_data)
    print(f"Result data is saved: {result_file}")


file1 = 'random-michaels.csv'
file2 = 'random.csv'
result_file = 'result_data.csv'

remove_duplicates(file1, file2, result_file)
