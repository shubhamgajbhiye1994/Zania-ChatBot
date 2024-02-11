"""
qa_bot : 
    It configure retriver and reranker to return top results
"""
from llama_index.retrievers import AutoMergingRetriever
from llama_index.indices.postprocessor import SentenceTransformerRerank
from llama_index.query_engine import RetrieverQueryEngine
from src.utils import constants as const
import os

def QAbot(search_index , similarity_top_k = 10, rerank_top_n = 5):
    """
    QAbot:
        It configure retriver and reranker to return top results. 
    Args:
        search_index (object): documents search index
        similarity_top_k (int, optional): value to N similar doc. Defaults to 10.
        rerank_top_n (int, optional): value to rank N doc. Defaults to 5.
    Returns:
        search_engine (object): documents search index object with retriver
    """
    const.logger.info("QAbot retrever started...")
    base_retriever = search_index.as_retriever(similarity_top_k = similarity_top_k)
    retriever = AutoMergingRetriever(base_retriever, search_index.storage_context, verbose = True)
    rerank = SentenceTransformerRerank(top_n = rerank_top_n,\
                                        model = os.path.join(const.MODELS_DIR,"bge-reranker-base"))
    search_engine = RetrieverQueryEngine.from_args(retriever, node_postprocessors = [rerank])
    const.logger.info("QAbot retrever ends...")
    return search_engine

    