import csv

csv_file = "student.csv"

def read_csv():
    print("\nReading CSV file...\n")
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def write_csv(name, age, grade):
    print("\nAdding new row...\n")
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])
    print("Data added!")

def delete_row(student_name):
    print("\nDeleting row...\n")
    rows = []

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != student_name:
                rows.append(row)

    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Row with name '{student_name}' deleted!")


read_csv()
write_csv("Nisha", 19, "B")
delete_row("Asha")
read_csv()
