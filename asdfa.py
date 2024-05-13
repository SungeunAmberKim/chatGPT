import csv

def percent_correct_mode(mode):
    size = 0
    correct = 0
    difference = []
    with open('clean_3.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[7] == mode:
                difference.append(row[10])
    print(len(difference))
    for i in difference:
        if float(i) < 1:
            correct += 1
            size += 1
        else:
            size += 1
    percent = float(correct) / float(size) * 100
    
    print(f"{correct}/{size} - {percent}%\n\n")
        
percent_correct_mode("one word")