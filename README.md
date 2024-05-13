## Data Analysis of ChatGPT’s Correctness
  The objective is to conduct data analysis on ChatGPT's answers for a prompt. This prompt had various values each time Chat GPT was asked about it. It also has unnecessary information to confuse Chat GPT. After running the prompt to Chat GPT several times, the accuracy, and factors that influenced it were computed and visualized via Jupyter Notebook.
### Obtaining Data
- Data was generated in data_generation.py
- model = "gpt-3.5-turbo"
- input.csv changes in every run
- output_1.csv and output_2.csv give raw data from ChatGPT
- clean_1.csv and clean_2.csv give data after cleaning
### Analyzing Data
- Prepared the CSV file by creating data frames
- Calculated Chat GPT's accuracy in answering the prompt
- Created a pie chart to show the frequency of each unique answer
- Calculated average of temperature, average of top_p, and ratio for each unique answer
- Calculated statistics about the keyword mode, a factor that influenced Chat GPT's answer
