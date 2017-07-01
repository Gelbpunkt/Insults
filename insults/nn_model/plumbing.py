import pandas as pd
import numpy as np

from insults.nn_model.util import binarize, binarize_outshape, striphtml, clean

def load_data(data_fp,  delimiter="\t"):
    return pd.read_csv(data_fp, header=0, delimiter=delimiter, quoting=3)


def dataset_preprocess(dataset):
    pass


def extract_documents_with_their_sentiments(dataset):
    docs, sentences, sentiments = [], [], []

    for cont, sentiment in zip(dataset.review, dataset.sentiment):
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', clean(striphtml(cont)))
        sentences = [sent.lower() for sent in sentences]
        docs.append(sentences)
        sentiments.append(sentiment)

    return docs, sentiments


def sentence_count_per_doc(docs):
    num_sent = []
    for doc in docs:
        num_sent.append(len(doc))

    return num_sent


def charset(docs):
    txt = ''
    for doc in docs:
        for s in doc:
            txt += s

    return set(txt)


def chars_to_indices_vec(docs, char_indices, max_sent, max_len):
    X = np.ones((len(docs), max_sent, max_len), dtype=np.int64) * -1

    for i, doc in enumerate(docs):
        for j, sentence in enumerate(doc):
            if j < MAX_SENTENCES:
                for t, char in enumerate(sentence[-max_len:]):
                    X[i, j, (MAXLEN - 1 - t)] = char_indices[char]

    return X


def shuffle_dataset(X, y):
    ids = np.arange(len(X))
    np.random.shuffle(ids)

    return X[ids], y[ids]


def dataset_split(X, y, train_end=20000, test_start=22500):
    X_train = X[:train_end]
    X_test = X[test_start:]

    y_train = y[:train_end]
    y_test = y[test_start:]

    return X_train, X_test, y_train, y_test