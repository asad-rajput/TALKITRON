# Talkitron Chatbot

This repository contains a Django project that integrates a chatbot functionality using AIML and Pytholog, and also utilizes the OpenAI GPT-3.5 model for generating responses.

## Prerequisites
- Python 3.x
- Django
- nltk
- aiml
- pytholog
- py2neo
- openai

## Installation
1. Clone the repository to your local machine.
2. Install the required dependencies mentioned in the `requirements.txt` file using pip:
   ```shell
   pip install -r requirements.txt
   ```
3. Set up a Neo4j database and update the connection details in the `graph` object initialization in the `main.py` file.
4. Update the `openai.api_key` variable in the `main.py` file with your OpenAI API key.

## Usage
1. Start the Django server by running the following command in the project root directory:
   ```shell
   python manage.py runserver
   ```
2. Access the application by navigating to `http://localhost:8000` in your web browser.
3. If you are not logged in, you will be redirected to the login page. Log in with your credentials.
4. Once logged in, you will be directed to the chatbot interface on the homepage.
5. Enter your message in the input field and press Enter or click the Send button to get a response from the chatbot.

## AIML and Pytholog Files
- The AIML files for chatbot responses are located in the `files` directory. You can add or modify the AIML files to customize the chatbot's behavior.
- The Pytholog queries are defined in the `kb` object initialization in the `main.py` file. You can add or modify the queries to extend the knowledge base.

## Generating Responses
- The `generate_response` function in the `main.py` file is responsible for generating responses from the chatbot.
- The function utilizes natural language processing techniques from the nltk library to identify commands and expressions in the user's message.
- If a command is detected (e.g., "solve" or "calculate"), the function evaluates the corresponding expression and returns the result.
- If the user's message matches an AIML pattern, the function uses the AIML Kernel to generate a response.
- If the response contains specific words (e.g., "unknown"), the function uses the OpenAI GPT-3.5 model to generate an alternative response.

## Contributing
Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

****
**Special Thanks to [Pemma](https://pemagrg.medium.com/) for chat pattern and aiml files.**
