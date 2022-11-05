import os
from typing import List
import openai
import os
import openai
import argparse
import re

def main():
    print('Running Brand First...')
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    result = generate_branding_snippet(user_input)
    keywords_results = generate_branding_keywords(user_input)
    print(result)
    print(keywords_results)
    
def generate_branding_snippet(prompt: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    new_prompt = f'Generate upbeat branding snippet for {prompt}: '
    response = openai.Completion.create(engine='davinci-instruct-beta-v3', prompt=new_prompt, max_tokens=32)
    #extract the text data returned from the response dictionary
    branding_text = response['choices'][0]['text']
    #removes the white space fromn the left and right side of the branding text
    branding_text = branding_text.strip()
    #this will get the last character from the branding text
    last_char = branding_text[-1]
    #this will check to see if the branding with the proper punctuation if not an elipses will be added.
    if last_char not in {'.', '!', '?'}:
        branding_text += '...'

    return branding_text

def generate_branding_keywords(prompt: str) -> List[str]:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    new_prompt = f'Generate related branding keywords for {prompt}: '
    response = openai.Completion.create(engine='davinci-instruct-beta-v3', prompt=new_prompt, max_tokens=32)
    #extract the text data returned from the response dictionary
    branding_keywords: str = response['choices'][0]['text']
    #removes the white space fromn the left and right side of the branding text
    branding_keywords = branding_keywords.strip()
    branding_keyword_array = re.split(',|\n|;|-', branding_keywords)
    branding_keyword_array = [k.strip().lower() for k in branding_keyword_array]
    branding_keyword_array = [k for k in branding_keyword_array if len(k) > 0]
    
    return branding_keyword_array
    

if __name__ == '__main__':
    main()
