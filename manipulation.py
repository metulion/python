if __name__ == "__main__":
    import csv

    with open('C:\\Users\\7378\\Downloads\\random_python_information.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter = 0
        for row in csv_reader:
            if (counter != 0):
                print (row)
            counter = counter +1