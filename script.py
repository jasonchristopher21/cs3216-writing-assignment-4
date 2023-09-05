import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def open_file(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        content = f.read()
    return content

def get_completion(prompt, model="gpt-3.5-turbo-16k"):

    system_prompt = open_file("./system_prompt.txt")
    user_example = open_file("./user_example.txt")
    assistant_example = open_file("./assistant_example.txt")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_example},
        {"role": "assistant", "content": assistant_example},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,  # this is the degree of randomness of the model's output
    )
    return response

def main():
    prompt = open_file("./user_prompt.txt")
    response = get_completion(prompt)
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()