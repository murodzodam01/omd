from typing import List
from math import log


class CountVectorizer:
    '''
    This class converts a collection
    of text documents to a matrix of token counts.
    '''

    def __init__(self):
        self.vocabulary = []

    def fit_transform(self, sentences: List[str]) -> List[List[int]]:
        '''
        Get the list of strings and return document-term matrix.

        :param sentences:
        :return: Document-term matrix
        '''

        tokenized_string = [doc.lower().split() for doc in sentences]
        for sentence in tokenized_string:
            for token in sentence:
                if token not in self.vocabulary:
                    self.vocabulary.append(token)
        result = []
        for token in tokenized_string:
            count_words = [token.count(elem) for elem in self.vocabulary]
            result.append(count_words)

        return result

    def get_feature_names(self) -> List[str]:
        '''
        Return all unique words/strings in the text.

        :return
        List[str]: list of unique strings in the sentence(s).
        '''

        return self.vocabulary


class TfidfTransformer:
    def __init__(self):
        pass

    def tf_transform(self, count_matrix):
        tf_matrix = []
        for words_list in count_matrix:
            s = sum(words_list)
            tf_vector = []
            for words_count in words_list:
                tf_vector.append(words_count / s)
            tf_matrix.append(tf_vector)
        return tf_matrix

    def idf_transform(self, count_matrix):
        idf = []
        length_doc = len(count_matrix[0])
        num_docs = len(count_matrix)
        for i in range(length_doc):
            count_docs = 0
            for count_lst in count_matrix:
                if count_lst[i] > 0:
                    count_docs += 1
            idf.append(log((num_docs + 1) / (count_docs + 1)) + 1)
        return idf

    def fit_transform(self, count_matrix):
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        tf_idf = []
        for doc in tf:
            new_row = []
            for i in range(len(doc)):
                new_row.append(round(doc[i] * idf[i], 3))
            tf_idf.append(new_row)
        return tf_idf


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        tfidf_matrix = self.tf_idf_transformer.fit_transform(count_matrix)
        return tfidf_matrix


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print()
    print(tfidf_matrix)
