from google.cloud import language_v1

class NLP:

    def __init__(self, text):
        '''
        Initialized NLP class, and stores the response in self.response
        @param      {String}    text:   Text input.
        '''
        self.text       = text
        self.response   = {'sentiment':{}, 'classes':{}}

        self.client     = language_v1.LanguageServiceClient()
        self.type       = language_v1.Document.Type.PLAIN_TEXT
        self.document   = {"content": self.text, "type_": self.type}

        # Get the response during init
        self.get_response()
    
    def classify_text(self):
        """
        Classifying Content in a String
        """

        response = self.client.classify_text(request = {'document': self.document})

        # Loop through classified categories returned from the API
        for category in response.categories:
            # Get the name of the category representing the document.
            # See the predefined taxonomy of categories:
            # https://cloud.google.com/natural-language/docs/categories
            category_name = category.name.split('/')[1:]

            # Get the confidence. Number representing how certain the classifier
            # is that this category represents the provided text.
            category_confidence = category.confidence

            # Store results in self.response attribute.
            self.response['classes']['categories'] = category_name
            self.response['classes']['confidence'] = category_confidence

    def analyze_sentiment(self):
        """
        Analyzing Sentiment in a String
        """

        encoding_type = language_v1.EncodingType.UTF8
        response = self.client.analyze_sentiment(request = {'document': self.document, 'encoding_type': encoding_type})

        # Get overall sentiment of the input text
        self.response['sentiment']['score']         = response.document_sentiment.score
        self.response['sentiment']['magnitude']     = response.document_sentiment.magnitude

    def get_response(self):
        '''
        Returns Google NLP data response
        @return     {dict}      self.response:  Dictionary containing sentence sentiment and classes.
        '''
        # Execute API call to Google NLP context classifier
        self.classify_text()

        # Execute API call to Google NLP sentiment analysis
        self.analyze_sentiment()

        return self.response

if __name__ == '__main__':

    text = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'
    nlp = NLP(text)
    a = nlp.response
    print(a)

