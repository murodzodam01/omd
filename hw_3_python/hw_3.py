from typing import List


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

        text = ' '.join(sentences)
        list_tokens = list(text.lower().split(' '))
        for token in list_tokens:
            if token not in self.vocabulary:
                self.vocabulary.append(token)
        tokenized_string = [doc.lower().split() for doc in sentences]
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


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
