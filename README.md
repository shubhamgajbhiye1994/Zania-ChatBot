
# Zania-QA-BOT

Zania-QA-BOT is a pdf based chatbot using openai and llamaindex.


## Objective
Create a bot or program that leverages the capabilities of a large language model. This bot should be able to extract answers based on the content of a large PDF document. Ideally, you use OpenAI LLMs. You can also use the Langchain or LLama Index framework to implement this functionality.

## Input/Output Requirement
Output Format :
    The output should be a structured JSON blob that pairs each question with its corresponding answer.
    Answers should be word to word match if the question is a word to word match
    If the answer is low confidence, reply with “Data Not Available”

Input format:
    A list of questions.
    A PDF file containing the document over which the  questions will be answered.



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

'OPENAI_API_KEY' : Add OPENAI api API_KEY
'OPENAI_MODEL' : "gpt-3.5-turbo"


## Project Setup

Please follow below instruction for project Setup 

a) for Linux Machine installation

    1.clone github repo:
        git clone <github_link>
    2.cd Zania-Chatbot and run sh setup.sh
       

b) for Windows Machine
    
    1. open git bash and clone repo using
        git clone <github_link>
    2. install python3.9 and create virtual env using
        python3.9 -m venv search_env
    3. change directory to Zania-ChatBot/
       and below command one by one

        virtual_env -m pip install -r requirements.txt
        git lfs install
        cd /root/Zania-ChatBot/models
        git clone https://huggingface.co/BAAI/bge-reranker-base
        git clone https://huggingface.co/BAAI/bge-small-en-v1.5

This will set project env.
## Sample Input Output

input : file = filename.pdf
output : output.json

## Follow below instruction to run project
        1. cd Zania-ChatBot
        2. python_env -u main.py -f "handbook.pdf" -q_lst "q1" "q2" "q3" .. "qn"
        3. check /data/output/output.json folder for output


Note : If you want to change input file then place pdf file in /data/input/ and then run main.py script with addition argument of -io True

