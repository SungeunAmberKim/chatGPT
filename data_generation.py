import csv
import re
import random
import key
from openai import OpenAI

# open AI api key
client = OpenAI(api_key=key.api_key)

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
            file.write(f"{emily_invested}, {emily_interst_1}, {emily_interst_2},
                       {uni_steal}, {mom_invested},{mom_interest},
                       {moe_steal}, {answer_form},{correct_answer}\n")
            
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
            file.write(f"{emily_invested}, {emily_interst_1}, {emily_interst_2},
                       {uni_steal},{mom_invested},{mom_interest},
                       {moe_steal},{answer_form},{correct_answer}\n")
            
# function to generate prompts from csv file
def generate_prompts(infile):
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
            prompt_each = f'''Emily invested ${emily_invested} in two different accounts and has a cat named Uni. 
                One account earns {emily_interst_1}% annual interest, the other earns {emily_interst_2}% annual interest, 
                and her cat stole {uni_steal}% of her total investment before she invested. 
                And her mom invested ${mom_invested} in five accounts and has a cat named Moe. 
                One account earns {mom_interest}% annual interest, and Moe stole {moe_steal}% more than Uni. 
                If the total interest earned after one year is $340, how much did Moe steal? Please answer in {answer_form}'''
            output.append(prompt_each)
    return output
# without emily mom investing
def generate_prompts_1(infile):
    output = []
    with open(infile) as file:
        for line in file:
            parts = line.split(",")
            emily_invested = parts[0]
            emily_interst_1 = parts[1]
            emily_interst_2 = parts[2]
            uni_steal = parts[3]
            moe_steal = parts[6]
            answer_form = parts[7]
            prompt_each = f'''Emily invested ${emily_invested} in two different accounts and has a cat named Uni. One account earns {emily_interst_1}% annual interest, the other earns {emily_interst_2}% annual interest, and her cat stole {uni_steal}% of her total investment before she invested. And her mom has a cat named Moe stole {moe_steal}% more than Uni. If the total interest earned after one year is $340, how much did Moe steal? Please answer in {answer_form}'''
            output.append(prompt_each)
    return output

# function to generate respond
def generate_text(prompt, temp, top, freq, pre):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        # temperature 0 to 2, deterministic to randomness
        temperature=temp,
        # top_p 0 to 2, deterministic to randomness in word choices
        top_p=top,
        # high frequency_penalty >> decreased repeated words
        frequency_penalty=freq,
        # high presence_penalty >> branch into new topics
        presence_penalty=pre,
        # max_tokens: maximum context length
        max_tokens=20)
    
    return response.choices[0].message.content
        
def generate_output_file(prompt, input_file, output_file, temperature, top_p, frequency_penalty, presence_penalty):
    with open(input_file, 'r') as infile:
    # Open the output file for writing
        with open(output_file, 'a', newline='') as outfile:
            # Create CSV reader and writer objects
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            index = 0
            # Iterate over each row in the input file
            for row in reader:
                # Add the new element to each row
                row.append(generate_text(str(prompt[index]),temperature, top_p, frequency_penalty, presence_penalty))
                row.append(-1)
                row.append(temperature)
                row.append(top_p)
                row.append(frequency_penalty)
                row.append(presence_penalty)
                row.append(prompt[index])
                # Write the modified row to the output file
                writer.writerow(row)
                index += 1

def data_cleaning(output_file, clean_file):
    with open(output_file, 'r') as outfile:
    # Open the output file for writing
        with open(clean_file, 'a', newline='') as cleanfile:
            # Create CSV reader and writer objects
            reader = csv.reader(outfile)
            writer = csv.writer(cleanfile)
            
            # Iterate over each row in the input file
            for row in reader:
                # this is to get the only number value from ChatGPT's response
                regex = regex = r"\d+"
                match = re.search(regex, row[9].replace(",",""))
                if match:
                    row[9] = match.group()
                    # calculating difference between ChatGPT's response and correct answer
                    row[10] = abs(float(row[8])-float(row[9]))
                    writer.writerow(row[:])
        
def test(input_csv, output_csv, clean_csv, iterations, mode, temperature, top_p, frequency_penalty, presence_penalty):
    # temperature = 0.6; top_p = 1; frequency_penalty = 0; presence_penalty = 0
    # one integer
    generate_input_file_1(iterations, mode, input_csv)
    prompts = generate_prompts(input_csv)
    generate_output_file(prompts, input_csv, output_csv, temperature, top_p, frequency_penalty, presence_penalty)
    data_cleaning(output_csv, clean_csv)
    
def test_1(input_csv, output_csv, clean_csv, iterations, mode, temperature, top_p, frequency_penalty, presence_penalty):
    # temperature = 0.6; top_p = 1; frequency_penalty = 0; presence_penalty = 0
    # one integer
    generate_input_file_1(iterations, mode, input_csv)
    prompts = generate_prompts_1(input_csv)
    generate_output_file(prompts, input_csv, output_csv, temperature, top_p, frequency_penalty, presence_penalty)
    data_cleaning(output_csv, clean_csv)

if __name__ == "__main__":
    # input file; output file; data cleaned file; iterations; mode; temperature, top_p, frequency_penalty, presence_penalty
    
    #test("input.csv","output_2.csv","clean_2.csv",100,"one word", 0.6, 1, 0, 0)
    data_cleaning("output_2.csv","clean_2.csv")
    
    
    