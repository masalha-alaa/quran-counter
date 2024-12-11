from sklearn.decomposition import PCA


class EmbeddingsResizer:
    def __init__(self, out_features):
        self._out_features = out_features
        self.pca = PCA(n_components=out_features)

    def fit(self, X):
        if X.shape[1] != self._out_features:
            self.pca.fit(X)

    def transform(self, X):
        if X.shape[1] != self._out_features:
            return self.pca.transform(X)
        return X

    def fit_transform(self, X):
        if X.shape[1] != self._out_features:
            return self.pca.fit_transform(X)
        return X
