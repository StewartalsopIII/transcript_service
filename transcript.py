import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Set your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_text(input_text):
    # Read the prompt template from a file
    prompt_file_path = 'prompt_template.txt'
    with open(prompt_file_path, 'r') as file:
        prompt_template = file.read()

    # Format the prompt with the input text
    prompt = prompt_template.format(input_text=input_text)

    # Make the API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an objectively minded and centrist-oriented analyst."},
            {"role": "user", "content": prompt}
    ]
)

    return response.choices[0].message.content.strip()


# Define the path to the input text file
input_file_path = 'podcast_transcript.txt'

# Ensure the file exists
if os.path.exists(input_file_path):
    with open(input_file_path, 'r') as file:
        input_text = file.read()

    # Analyze the text
    analysis = analyze_text(input_text)
    print(analysis)
else:
    print(f"File not found: {input_file_path}")
