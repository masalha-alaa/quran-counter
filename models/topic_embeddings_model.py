import joblib
import pickle
import pandas as pd
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer
from arabic_reformer import remove_diacritics, normalize_alif
from my_utils.my_data_loader import MyDataLoader
from my_utils.utils import resource_path
from models.embedding_resizer import EmbeddingsResizer  # DO NOT REMOVE! NEEDED BY joblib!
from datetime import datetime


class TopicEmbeddingsModel:
    _initialized = False
    _topic_embeddings = None
    _pca_for_embeddings = None
    _topics_dataframe = None
    _model = None

    def __init__(self):
        super().__init__()

    @property
    def is_initialized(self):
        return TopicEmbeddingsModel._initialized

    def initialize(self):
        if not self.is_initialized:
            print(f"{datetime.now()} Initializing topics model...")
            TopicEmbeddingsModel._load_data()
            print(f"{torch.version.cuda = }")
            print(f"{torch.cuda.is_available() = }")
            device = torch.device('cuda') if torch.cuda.is_available() else 'cpu'
            model_name = 'sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens'
            TopicEmbeddingsModel._model = SentenceTransformer(model_name, device=device)
            print(f"{datetime.now()} Done initializing topics model")
            TopicEmbeddingsModel._initialized = True

    @staticmethod
    def _load_data():
        TopicEmbeddingsModel._topic_embeddings = pickle.load(open(resource_path('embedding_models/topic_embeddings.pkl'), 'rb'))
        TopicEmbeddingsModel._pca_for_embeddings = joblib.load(resource_path('embedding_models/pca_for_embeddings.pkl'))
        TopicEmbeddingsModel._topics_dataframe = pd.read_pickle(resource_path('data/topics.pickle'))

    def encode(self, t):
        cleaned_topic = remove_diacritics(t)
        cleaned_topic = normalize_alif(cleaned_topic)
        # enc = F.normalize(torch.tensor(TopicEmbeddingsModel._pca_for_embeddings.transform(TopicEmbeddingsModel._model.encode(cleaned_topic, convert_to_tensor=True).cpu().reshape(1, -1)), dtype=torch.float32))
        enc = F.normalize(TopicEmbeddingsModel._model.encode(cleaned_topic, convert_to_tensor=True).cpu().reshape(1, -1))
        return enc

    def get_relevant_verses(self, topic, threshold=0.70):
        def _sort_ref(ref):
            s, v = ref.split(":")
            return int(s), int(v)

        topic_embedding = self.encode(topic)
        similarities = torch.matmul(TopicEmbeddingsModel._topic_embeddings, topic_embedding.T).squeeze()
        # similarities = F.cosine_similarity(embeddings_resized, topic_embedding, dim=1).squeeze()
        relevant_mask = (similarities > threshold).numpy()
        if relevant_mask.sum():
            relevant_topics = TopicEmbeddingsModel._topics_dataframe.iloc[relevant_mask]
            merged_topics = relevant_topics.apply(lambda row: ' - '.join([row[i] if row[i] else '' for i in range(6)]).strip("- "), axis=1)
            verses = relevant_topics['verses']
            df = pd.DataFrame({"relevant_topics": merged_topics, "score": similarities[relevant_mask], "verses": verses})
            df = df.explode('verses').drop_duplicates(subset='verses').sort_values(by='verses', key=lambda ser: ser.apply(_sort_ref))
            return df
        return pd.DataFrame({"relevant_topics": [], "score": [], "verses": []})
