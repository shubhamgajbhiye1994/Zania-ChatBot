"""
__author__ = Shubham Gajbhiye
__date__ = 2/11/2024 (month/date/year)
__project_name__ = Zania-Bot
__project_details__ = pdf based bot
__objective__ = Create a bot or program that leverages the capabilities of a large language model. 
                This bot should be able to extract answers based on the content of a large PDF document. 
                Ideally, you use OpenAI LLMs. You can also use the Langchain or LLama Index framework to 
                implement this functionality.
__input_filetype_support__ = pdf (path : /data/input/handbook.pdf)
__inputs__ = This is argument based -file filename.pdf (which is placed at /data/input/)
             -q_list "q1?" "q2?" "q3?" for each question to be answered
__output_filetype_support__ = json (path : /data/output/output.json)
__outputs__ = Json file having key as questions and answer as values
"""

from src.qa_bot import QAbot
from src.utils import constants as const
from config import config
from src.utils.argument_parser import args
from src.data_processing import build_automerge_index
import json
import os


if __name__ == '__main__':
    """
    It query the input questions and generate answers based on the context provided
    if threshold i.e. >0.5 of relevance match is not greater than then "Data Not Available"
    is answered.
    """
    if args.filename.endswith(".pdf"):
        print("Hello,I am custom QA, your free to ask any questions to me!")
        ## configure service settings
        service = config.configure_service()
        
        ## calling data index builder
        search_index = build_automerge_index()
        query_engine = QAbot(search_index, similarity_top_k=6)
        output = {}
        ## hit query engine with input query and evaluate results
        ## and store output
        for query in args.question_list:
            query_output = query_engine.query(query)
            eval_response = config.evalutor.evaluate_response(query,query_output)
            if eval_response.score >= 0.5:
                output.update({query:query_output.response})
            else:
                output.update({query:"Data Not Available"})
        if output:
            file = open(os.path.join(const.OUTPUT_DIR,"output.json"),"w")
            json.dump(output,file,indent=2)
            print("Output file is generated")  
    else:
        const.logger.error("Invalid File Format , Please try again with valid file format")
        print("Invalid File Format , Please try again with valid file format")
    