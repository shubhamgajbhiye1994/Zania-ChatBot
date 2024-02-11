"""
Constant file 
"""


from llama_index import OpenAIEmbedding
from llama_index.llms import OpenAI
from dotenv import load_dotenv
import logging
import os
load_dotenv()

BASE_DIR = os.getcwd()
LOGS_DIR = os.path.join(BASE_DIR,"logs/")
DATA_DIR = os.path.join(BASE_DIR,"data/")
INDEX_DIR = os.path.join(DATA_DIR,"index/")
INPUT_DIR = os.path.join(DATA_DIR,"input/")
OUTPUT_DIR = os.path.join(DATA_DIR,"output/")
MODELS_DIR = os.path.join(BASE_DIR,"models/")
CHUNK_SIZE = 1024
CHUNK_SIZE_LIST = [2048,512,128]
CHUNK_OVERLAP = 20
CONTEXT_WINDOW = 4096
NUM_OUTPUT = 256
CHUNK_OVERLAP_RATIO = 0.1
CHUNK_SIZE_LIMIT = None
llm = OpenAI(model = os.getenv('OPENAI_MODEL'), temperature=0, max_tokens=256,\
                api_key = os.getenv('OPENAI_API_KEY'))
embed_model = OpenAIEmbedding()


 
# Create and configure logger
logging.basicConfig(filename=os.join(LOGS_DIR,"QA_BOT.log"))
logger = logging.getLogger()
logger.setLevel(logging.INFO)

        