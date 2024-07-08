import csv


def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['website', 'headline'])
        writer.writeheader()
        writer.writerows(data)
