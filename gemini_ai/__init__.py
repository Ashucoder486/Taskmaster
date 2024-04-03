import textwrap

import google.generativeai as genai

# Function to get API key for Google Generative AI
def get_google_api_key():
    # Fetch your Google API key from environment variables or wherever it's stored
    # Example: GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    return "AIzaSyCUQRfjNUChPsXuv2qMH1ijqeQqHMwqm2U"

# Function to ask a question to the Gemni model
def ask_gemini(question):
    # Configure the API key
    genai.configure(api_key=get_google_api_key())
    # Selecting an appropriate model
    model = genai.GenerativeModel('gemini-pro')
    # Generate content using the model
    response = model.generate_content(question)
    text =  response._result.candidates[0].content.parts[0].text
    return textwrap.dedent( text.strip().replace('*', ''))


# Test the function
if __name__ == "__main__":
    question = "who is yogi adityanath"
    response = ask_gemini(question)
    # print(response.result.candidates[0].content.parts[0].text)
    print(response)
