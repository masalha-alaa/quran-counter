import joblib
import numpy as np
import pickle
import pandas as pd
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, util
from arabic_reformer import remove_diacritics, normalize_alif
from my_utils.my_data_loader import MyDataLoader
from my_utils.utils import resource_path
from models.embedding_resizer import EmbeddingsResizer  # DO NOT REMOVE! NEEDED BY joblib!
from datetime import datetime
from preprocessing import Preprocessor
from enum import Enum
import json


class EncodingMethods(Enum):
    WEIGHTED_AVERAGE = 0
    AVERAGE = 1
    CONCAT = 2
    SPLITS = 3


class TopicEmbeddingsModel:
    _initialized = False
    _topic_embeddings = None
    # _pca_for_embeddings = None
    # _topics_dataframe = None
    _topic_ids = None
    _model = None
    _preprocessor = None
    _encoding_method = EncodingMethods.WEIGHTED_AVERAGE

    def __init__(self):
        super().__init__()

    @property
    def is_initialized(self):
        return TopicEmbeddingsModel._initialized

    def initialize(self):
        if not self.is_initialized:
            print(f"{datetime.now()} Initializing topics model...")
            TopicEmbeddingsModel._preprocessor = Preprocessor()
            TopicEmbeddingsModel._load_data()
            print(f"{torch.version.cuda = }")
            print(f"{torch.cuda.is_available() = }")
            device = torch.device('cuda') if torch.cuda.is_available() else 'cpu'
            # model_name = 'sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens'
            model_name = 'embedding_models/topic_sim_model__2024_01_23__16_57_30'
            TopicEmbeddingsModel._model = SentenceTransformer(model_name, device=device)
            print(f"{datetime.now()} Done initializing topics model")
            TopicEmbeddingsModel._initialized = True

    @staticmethod
    def _load_data():
        TopicEmbeddingsModel._topic_embeddings = pickle.load(open(resource_path('embeddings/topics_embeddings.pkl'), 'rb'))
        TopicEmbeddingsModel._topic_ids = json.load(open(resource_path('data/topic_ids.json'), encoding='utf-8'))
        # TopicEmbeddingsModel._pca_for_embeddings = joblib.load(resource_path('embedding_models/pca_for_embeddings.pkl'))
        # TopicEmbeddingsModel._topics_dataframe = pd.read_pickle(resource_path('data/topics.pickle'))

    def clean_line(self, line):
        return TopicEmbeddingsModel._preprocessor.preprocess_sentence(line)

    def encode(self, topic_name, method=None):
        if method is None:
            method = TopicEmbeddingsModel._encoding_method
        model = TopicEmbeddingsModel._model
        topic_name = self.clean_line(topic_name)
        if method != EncodingMethods.CONCAT:
            encodings = [model.encode(sub_topic) for sub_topic in topic_name.split('\n')]
            
            if method == EncodingMethods.WEIGHTED_AVERAGE:
                encoding = np.float32(np.average(encodings, weights=list(range(len(encodings))), axis=0))
            elif method == EncodingMethods.AVERAGE:
                encoding = np.float32(np.mean(encodings, axis=0))
            elif method == EncodingMethods.SPLITS:
                encoding = encodings
            else:
                raise NotImplementedError(f"Encoding method not implemented: {method}")
        else:  # method == EncodingMethods.CONCAT:
            encoding = model.encode(topic_name.replace("\n", " - "))

        return encoding

    def get_sim(self, e1, e2):
        if TopicEmbeddingsModel._encoding_method == EncodingMethods.SPLITS:
            return max(util.pytorch_cos_sim(e1, e2_i).numpy().flatten()[0] for e2_i in e2)
        else:
            return util.pytorch_cos_sim(e1, e2).cpu().numpy().flatten()[0]

    def sort_topics(self, s):
        s = self.clean_line(s)
        s_encoding = TopicEmbeddingsModel._model.encode(s)
        scores = np.array(
            [self.get_sim(s_encoding, topic_embedding) for topic_embedding in TopicEmbeddingsModel._topic_embeddings.values()])
        tpoics_sorted_idx_asc = np.argsort(scores)
        return sorted(scores, reverse=True), tpoics_sorted_idx_asc[::-1]

    def get_top_topics(self, sorted_topics_idx_, top_n=5):
        top_idx = sorted_topics_idx_[:top_n]
        return [TopicEmbeddingsModel._topic_ids[str(idx)] for idx in top_idx]

    def get_relevant_verses(self, topic, top):
        def _sort_ref(ref):
            s, v = ref.split(":")
            return int(s), int(v)

        topic_scores, sorted_topics_idx = self.sort_topics(topic)
        relevant_topics = []
        scores = []
        verses = []
        for i,topic_ in enumerate(self.get_top_topics(sorted_topics_idx, top)):
            # topic_[1][0]
            relevant_topics.append(topic_[0].replace("\n", " - "))
            scores.append(topic_scores[i])
            verses.append(topic_[1])

        df = pd.DataFrame({"relevant_topics": relevant_topics, "score": scores, "verses": verses}).explode('verses')
        return df.drop_duplicates(subset='verses').sort_values(by='verses', key=lambda ser: ser.apply(_sort_ref))
