import pandas as pd
import time
import random
from openai import OpenAI

# open AI api key
client = OpenAI(api_key='sk-proj-rQ3SVHMcSBcSPHwRQITMT3BlbkFJjrBVYJ6ICR0TC1MFzun4')

# function to generate respond
def generate_text(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        # temperature 0 to 2, deterministic to randomness
        temperature=0.6,
        # top_p 0 to 2, deterministic to randomness
        top_p=1,
        # high frequency_penalty >> decreased repeated words
        frequency_penalty=0,
        # high presence_penalty >> branch into new topics???
        presence_penalty=0,
        # max_tokens: maximum context length
        max_tokens=100)
    return response.choices[0].message.content

# function to generate prompts from csv file
def generate_prompts(file):
    output = []
    with open(file) as file:
        for line in file:
            parts = line.split(",")
            if parts[0] == "emily_invested":
                continue
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
            
# generating input csv file    
def generate_csv_1(size: int, answer_form):
    with open("input_1.csv","w") as file:
        file.write("emily_invested,emily_interst_1,emily_interst_2,uni_steal,mom_invested,mom_interest,moe_steal,answer_form,correct answer,chatGPT\n")
        for i in range(size):
            emily_invested = random.randint(1000,10000)
            emily_interst_1 = random.randint(1,10)
            emily_interst_2 = random.randint(1,10)
            uni_steal = random.randint(1,100)
            mom_invested = random.randint(1000,10000)
            mom_interest = random.randint(1, 10)
            moe_steal = random.randint(1,100)
            correct_answer = ((emily_invested*uni_steal)/100)*(1+(moe_steal/100))
            file.write(f"{emily_invested},{emily_interst_1},{emily_interst_2},{uni_steal},{mom_invested},{mom_interest},{moe_steal},{answer_form},{correct_answer}\n")
        
        
        
if __name__ == "__main__":
    generate_csv_1(5, "one word")
    prompts = generate_prompts("input_1.csv")
    for i in prompts:
        print(generate_text(i))