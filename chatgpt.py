import csv
import re
import random
from openai import OpenAI

# open AI api key
client = OpenAI(api_key='')


# generating input csv file    
def generate_input_file(size: int, answer_form, filename):
    with open(filename,"w") as file:
        for i in range(size):
            emily_invested = random.randrange(1000, 100000, 100)
            emily_interst_1 = random.randrange(1, 10, 1)
            emily_interst_2 = random.randrange(1, 10, 1)
            uni_steal = random.randrange(0, 100, 5)
            mom_invested = random.randrange(1000,10000, 10)
            mom_interest = random.randrange(1, 10, 1)
            moe_steal = random.randrange(0,100, 5)
            correct_answer = ((emily_invested*uni_steal)/100)*(1+(moe_steal/100))
            file.write(f"{emily_invested},{emily_interst_1},{emily_interst_2},{uni_steal},{mom_invested},{mom_interest},{moe_steal},{answer_form},{correct_answer}\n")
# generating input csv file; correct_answer is always 55   
def generate_input_file_1(size: int, answer_form, filename):
    with open(filename,"w") as file:
        for i in range(size):
            emily_invested = 5000
            emily_interst_1 = random.randrange(1, 10, 1)
            emily_interst_2 = random.randrange(1, 10, 1)
            uni_steal = 1
            mom_invested = random.randrange(1000,10000, 10)
            mom_interest = random.randrange(1, 10, 1)
            moe_steal = 10
            correct_answer = 55
            file.write(f"{emily_invested},{emily_interst_1},{emily_interst_2},{uni_steal},{mom_invested},{mom_interest},{moe_steal},{answer_form},{correct_answer}\n")
# function to generate prompts from csv file
def generate_prompts(infile,outfile):
    output = []
    with open(infile) as file:
        for line in file:
            parts = line.split(",")
            emily_invested = parts[0]
            emily_interst_1 = parts[1]
            emily_interst_2 = parts[2]
            uni_steal = parts[3]
            mom_invested = parts[4] 
            mom_interest = parts[5]
            moe_steal = parts[6]
            answer_form = parts[7]
            prompt_each = f'''Emily invested ${emily_invested} in two different accounts and has a cat named Uni. One account earns {emily_interst_1}% annual interest, the other earns {emily_interst_2}% annual interest, and her cat stole {uni_steal}% of her total investment before she invested. And her mom invested ${mom_invested} in five accounts and has a cat named Moe. One account earns {mom_interest}% annual interest, and Moe stole {moe_steal}% more than Uni. If the total interest earned after one year is $340, how much did Moe steal? Please answer in {answer_form}'''
            output.append(prompt_each)
    return output

# function to generate respond
def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        # temperature 0 to 2, deterministic to randomness
        temperature=0,
        # top_p 0 to 2, deterministic to randomness
        top_p=0,
        # high frequency_penalty >> decreased repeated words
        frequency_penalty=0,
        # high presence_penalty >> branch into new topics???
        presence_penalty=0,
        # max_tokens: maximum context length
        max_tokens=20)
    
    return response.choices[0].message.content
        
def generate_output_file(prompt, input_file, output_file):
    with open(input_file, 'r') as infile:
    # Open the output file for writing
        with open(output_file, 'w', newline='') as outfile:
            # Create CSV reader and writer objects
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            index = 0
            # Iterate over each row in the input file
            for row in reader:
                # Add the new element to each row
                row.append(generate_text(str(prompt[index])))
                row.append(prompt[index])
                # Write the modified row to the output file
                writer.writerow(row)
                index += 1

def data_cleaning(output_file, clean_file):
    with open(output_file, 'r') as outfile:
    # Open the output file for writing
        with open(clean_file, 'w', newline='') as cleanfile:
            # Create CSV reader and writer objects
            reader = csv.reader(outfile)
            writer = csv.writer(cleanfile)
            
            # Iterate over each row in the input file
            for row in reader:
                regex = regex = r"\d+"
                match = re.search(regex, row[9].replace(",",""))
                if match:
                    row[9] = match.group()
                    writer.writerow(row[8:10])

def correctness(clean):
    size = 0
    correct = 0
    incorrect = 0
    with open(clean, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if abs(float(row[0]) - float(row[1])) < 1:
                correct += 1
            else:
                incorrect += 1
            size += 1
    correctness = f"{correct}/{size}"
    percentage = correct/size*100
    print(f"correctness: {correctness}") 
    print(f"percentage: {percentage}%")
    return correctness, percentage
        

if __name__ == "__main__":
    # temperature = 0; top_p = 0; frequency_penalty = 0; presence_penalty = 0
    # one integer
    input_csv = "input_1.csv"
    ouput_csv = "output_1.csv"
    clean_csv = "clean_1.csv"
    #generate_input_file_1(1000, "one integer ", input_csv)
    #prompts = generate_prompts(input_csv,ouput_csv)
    #generate_output_file(prompts, input_csv, ouput_csv)
    data_cleaning(ouput_csv, clean_csv)
    result_1 = correctness(clean_csv)
    with open('result.txt', 'a') as file:
        file.write("\n")
        file.write("input_1.csv, output_1.csv, clean_1.csv; one integer; 1000 iterations\n")
        file.write("temperature = 0; top_p = 0; frequency_penalty = 0; presence_penalty = 0\n")
        file.write(f"{result_1[0]} : {result_1[1]}%\n")
        file.write("___________________________________________________________________________\n")
    
        
    