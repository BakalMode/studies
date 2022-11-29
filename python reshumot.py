import csv

def read_info():
    file = "C:\\Users\\turht\\Desktop\\employees.csv"
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        summ = 0
        row_count = 0
        for row in reader:
            row_count += 1
            print(row['SALARY'])
            summ+=(int(row['SALARY']))

        print(summ/row_count)


read_info()


