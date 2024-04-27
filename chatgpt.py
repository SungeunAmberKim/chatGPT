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

if __name__ == "__main__":
    prompt = "Emily invested $5000 in two different accounts and has a cat named Uni. One account earns 5% annual interest, the other earns 8% annual interest, and her cat stole 1% of her total investment before she invested. And her mom invested $3000 in five accounts and has a cat named Moe. One account earns 9% annual interest, and Moe stole 10% more than Uni. If the total interest earned after one year is $340, how much did Moe steal? Please answer in one word"
    output = generate_text(prompt)
    print(output)
    