"""
Data Processing:
    It creates embedding and nodes and store it at local directory
"""
import os
import json
from config.config import configure_service, storage_config,node_parser
from src.utils.argument_parser import args
from llama_index.storage.docstore import SimpleDocumentStore
from src.utils import constants as const
from llama_index import Document, SimpleDirectoryReader, StorageContext, VectorStoreIndex,load_index_from_storage
from llama_index.node_parser import get_leaf_nodes


def build_automerge_index():
    """
    It build indexes,embedding and store at local data directory
    It converts documents into embedding and its nodes and store it to local database

    Returns:
        automerge_index : index_search_object
    """
    const.logger.info("build_automerge_index started...")
    documents = SimpleDirectoryReader(input_files = [os.path.join(const.INPUT_DIR,args.filename)]).load_data()
    documents = Document(text="\n\n".join([doc.text for doc in documents]))
    nodes = node_parser.get_nodes_from_documents([documents])
    leaf_nodes = get_leaf_nodes(nodes)
    
    
    if args.index_overwrite:
        docstore = SimpleDocumentStore()
        docstore.add_documents(nodes)
        storage_context = StorageContext.from_defaults(persist_dir=const.INDEX_DIR,docstore=docstore)
        storage_context.docstore.add_documents(nodes)
        automerge_index = VectorStoreIndex(leaf_nodes,storage_context=storage_context)
        automerge_index.storage_context.persist(persist_dir = const.INDEX_DIR)
    else:
        ## get lates index id if multiple indexes found
        with open(os.path.join(const.INDEX_DIR,"index_store.json"),'r') as f:
            file = json.load(f)
        for i,j in file.items():
            for k,_ in j.items():
                index_id = k
            
        automerge_index = load_index_from_storage(storage_context = storage_config(),\
                                                service_context = configure_service(),\
                                                index_id = index_id)
    const.logger.info("build_automerge_index ends...")   
    return automerge_index

    
