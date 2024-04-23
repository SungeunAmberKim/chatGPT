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
    prompt = "what's the address of cal poly pomona"
    output = generate_text(prompt)
    
    