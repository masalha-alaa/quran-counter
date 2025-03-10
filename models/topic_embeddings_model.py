import os.path
import requests
import numpy as np
import pickle
import pandas as pd
# from sentence_transformers import SentenceTransformer, util
from my_utils.utils import resource_path
from datetime import datetime
from preprocessing import Preprocessor
from enum import Enum
import json
from my_utils.utils import is_cuda_available, is_torch_installed_with_gpu


class EncodingMethods(Enum):
    WEIGHTED_AVERAGE = 0
    AVERAGE = 1
    CONCAT = 2
    SPLITS = 3


class TopicEmbeddingsModel:
    _instance = None

    _initialized = False
    _fp16 = False
    _topic_embeddings = None
    _topic_ids = None
    # _model = None
    _preprocessor = None
    _encoding_method = EncodingMethods.WEIGHTED_AVERAGE

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TopicEmbeddingsModel, cls).__new__(cls)
        return cls._instance

    def initialize(self, fp16=False):
        if not self.is_initialized:
            # model_name = resource_path('embedding_models/topic_sim_model')
            # if not os.path.exists(model_name):
            #     return False

            print(f"{datetime.now()} Initializing topics model...")
            TopicEmbeddingsModel._preprocessor = Preprocessor()
            TopicEmbeddingsModel._load_data()
            TopicEmbeddingsModel._fp16 = False
            if fp16:
                print(f"fp16 is currently not supported.")
            # TODO: Add fp16 support in backend (backend/quran-topics/app.py)

            # print(f"{torch.version.cuda = }")
            # print(f"{torch.cuda.is_available() = }")
            # device = torch.device('cuda') if torch.cuda.is_available() else 'cpu'
            # print(f"{is_cuda_available() = }")
            # print(f"{is_torch_installed_with_gpu() = }")
            # model_name = 'sentence-transformers/xlm-r-bert-base-nli-stsb-mean-tokens'

            # TopicEmbeddingsModel._model = SentenceTransformer(model_name, device=device)
            # allegedly uses best available device between cpu / mps / gpu
            # TopicEmbeddingsModel._model = SentenceTransformer(model_name)
            # if TopicEmbeddingsModel._fp16:
            #     TopicEmbeddingsModel._model.half()  # sync with
            print(f"{datetime.now()} Done initializing topics model")
            TopicEmbeddingsModel._initialized = True

        return True

    @property
    def is_initialized(self):
        return TopicEmbeddingsModel._initialized

    @staticmethod
    def _load_data():
        TopicEmbeddingsModel._topic_embeddings = pickle.load(open(resource_path('embeddings/topics_embeddings.pkl'), 'rb'))
        TopicEmbeddingsModel._topic_ids = json.load(open(resource_path('data/topic_ids.json'), encoding='utf-8'))

    def get_relevant_verses(self, topic, top=5, relaxed=False):
        def _sort_ref(ref):
            s, v = ref.split(":")
            return int(s), int(v)

        topic_scores, sorted_topics_idx = self.get_sorted_topics(topic)
        relevant_topics = []
        scores = []
        verses = []
        if len(topic_scores) > 0 and len(sorted_topics_idx) > 0:
            for i,topic_ in enumerate(self.get_top_topics(topic_scores, sorted_topics_idx, top, relaxed)):
                relevant_topics.append(topic_[0].replace("\n", " - "))
                scores.append(topic_scores[i])
                verses.append(topic_[1])

        df = pd.DataFrame({"relevant_topics": relevant_topics, "score": scores, "verses": verses}).explode('verses')
        return df.drop_duplicates(subset='verses').sort_values(by='verses', key=lambda ser: ser.apply(_sort_ref))

    def get_sorted_topics(self, s):
        s = self.clean_line(s)
        # s_encoding = TopicEmbeddingsModel._model.encode(s)
        s_encoding = self.get_embedding(s)
        if s_encoding is None:
            return [], []
        # TODO: This could be sped up using matrix multiplication
        if TopicEmbeddingsModel._fp16:
            scores = np.array(
                [self.get_sim(s_encoding, topic_embedding.astype(np.float16)) for topic_embedding in TopicEmbeddingsModel._topic_embeddings.values()])
        else:
            scores = np.array(
                [self.get_sim(s_encoding, topic_embedding) for topic_embedding in
                 TopicEmbeddingsModel._topic_embeddings.values()])
        tpoics_sorted_idx_asc = np.argsort(scores)
        return sorted(scores, reverse=True), tpoics_sorted_idx_asc[::-1]

    def get_embedding(self, text):
        API_URL = "https://artificial-cerebrum-quran-topics.hf.space/embed"
        response = requests.post(API_URL, json={"text": text})

        if response.status_code != 200:
            print(f"API Error: {response.status_code}, {response.text}")
            return None

        try:
            data = response.json()
        except ValueError:
            print(f"Response is not valid JSON: {response.text}")
            return None

        if "embedding" not in data or not isinstance(data["embedding"], list):
            print(f"Invalid response: {data}")
            return None

        return response.json()['embedding']

    def get_top_topics(self, sorted_topic_scores, sorted_topics_idx_, top_n, relaxed):
        top_idx = sorted_topics_idx_[:top_n].tolist()
        if relaxed:
            last_score = round(sorted_topic_scores[top_n-1] * 100)
            for i, score in enumerate(sorted_topic_scores[top_n:]):
                if round(score * 100) == last_score:
                    top_idx.append(sorted_topics_idx_[i])
                else:
                    break
        return [TopicEmbeddingsModel._topic_ids[str(idx)] for idx in top_idx]

    def clean_line(self, line):
        return TopicEmbeddingsModel._preprocessor.preprocess_sentence(line)

    # def get_sim_deprecated(self, e1, e2):
    #     if TopicEmbeddingsModel._encoding_method == EncodingMethods.SPLITS:
    #         return max(util.pytorch_cos_sim(e1, e2_i).numpy().flatten()[0] for e2_i in e2)
    #     else:
    #         return util.pytorch_cos_sim(e1, e2).cpu().numpy().flatten()[0]

    def get_sim(self, e1, e2):
        return np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2))
