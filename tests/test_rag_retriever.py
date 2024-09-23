#%%
import pytest
import pandas as pd
import sys
import os

# Add parent directory to sys path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Import the RAGRetriever class from the component
from src.component.rag_retriever import RAGRetriever

# Get directories
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
grandparent_dir = os.path.dirname(parent_dir)

print(base_dir)
print(parent_dir)   
print(grandparent_dir)
print()
print(sys.path)
#%%




#%%

from src.component.rag_retriever import RAGRetriever

# Mock TextProcessor to avoid dependency issues during testing
class MockTextProcessor:
    def preprocess_and_split(self, text):
        # Mock splitting the text into chunks
        return [text[i:i+10] for i in range(0, len(text), 10)]

@pytest.fixture
def retriever():
    # Inject the MockTextProcessor
    retriever = RAGRetriever(model_name='mpnet')
    retriever.text_processor = MockTextProcessor()  # Use the mock processor
    return retriever

@pytest.fixture
def sample_dataframe():
    # Create a simple DataFrame for testing
    data = {
        'text': [
            "This is a sample text for testing purposes.",
            "Another piece of text to be used in tests.",
        ]
    }
    return pd.DataFrame(data)

def test_initialization(retriever):
    assert retriever.model is not None
    assert retriever.chunk_size == 1000
    assert retriever.chunk_overlap == 200

def test_load_data(retriever, sample_dataframe):
    retriever.load_data(sample_dataframe)
    assert retriever.df is not None
    assert len(retriever.df) == 2

def test_generate_embeddings(retriever, sample_dataframe):
    retriever.load_data(sample_dataframe)
    retriever.generate_embeddings()
    assert retriever.index is not None
    assert len(retriever.all_chunks) > 0
    assert len(retriever.chunk_to_doc_mapping) == len(retriever.all_chunks)

def test_search_vector_store(retriever, sample_dataframe):
    retriever.load_data(sample_dataframe)
    retriever.generate_embeddings()
    chunks, indices = retriever.search_vector_store("sample")
    assert len(chunks) > 0
    assert len(indices) > 0
