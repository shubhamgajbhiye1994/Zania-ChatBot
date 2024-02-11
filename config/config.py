"""
Config file : to configure evaluator,service context,storage context
"""


from llama_index import ServiceContext, StorageContext, set_global_service_context
from src.utils import constants as const
from llama_index.node_parser import HierarchicalNodeParser
from llama_index.evaluation import FaithfulnessEvaluator,RelevancyEvaluator
import os

## configuration of relevancy 
evalutor =  RelevancyEvaluator() #FaithfulnessEvaluator()
node_parser = HierarchicalNodeParser.from_defaults(chunk_sizes = const.CHUNK_SIZE_LIST)

## configure service context
def configure_service(): 
    """
    It configures the Service Context for embedding and llm model

    Returns:
        service_context - object
    """
    service_context = ServiceContext.from_defaults(llm=const.llm,embed_model="local:"+os.path.join(const.MODELS_DIR,"bge-small-en-v1.5"),node_parser=node_parser) #)
    set_global_service_context(service_context)
    return service_context
    
## configuration  of storage service
def storage_config():
    """
    It configures the Storage Context for storing index / embedding of documents
    Returns:
        storage_context : object
    """
    storage_context = StorageContext.from_defaults(persist_dir=const.INDEX_DIR)
    return storage_context

