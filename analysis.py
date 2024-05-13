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
    for i in difference:
        if float(i) < 1:
            correct += 1
            size += 1
        else:
            size += 1
    percent = float(correct) / float(size) * 100
    with open('percent.txt', 'a') as file:  
        file.write(f"mode: {mode}\n")
        file.write(f"{correct}/{size} - {percent}%\n\n")
    
def percent_correct_temperature(temp):
    size = 0
    correct = 0
    difference = []
    with open('clean_3.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if float(row[11]) == temp:
                difference.append(row[10])
    for i in difference:
        if float(i) < 1:
            correct += 1
            size += 1
        else:
            size += 1
    percent = float(correct) / float(size) * 100
    with open('percent.txt', 'a') as file:  
        file.write(f"temperature: {temp}\n")
        file.write(f"{correct}/{size} - {percent}%\n\n")

def percent_correct_top_p(top_p):
    size = 0
    correct = 0
    difference = []
    with open('clean_3.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if float(row[12]) == top_p:
                difference.append(row[10])
    for i in difference:
        if float(i) < 1:
            correct += 1
            size += 1
        else:
            size += 1
    percent = float(correct) / float(size) * 100
    with open('percent.txt', 'a') as file:  
        file.write(f"top_p: {top_p}\n")
        file.write(f"{correct}/{size} - {percent}%\n\n")
        
        


percent_correct_mode("one word")

percent_correct_mode("one integer")

percent_correct_mode("one float")

percent_correct_mode("one floating point value")


        
    


