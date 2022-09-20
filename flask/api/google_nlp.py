from logging import raiseExceptions
from google.cloud import language_v1
import datetime

class NLP:

    def __init__(self, data):
        '''
        Initialized NLP class, and stores the response in self.response
        @param      {dict}    datat:   Response from tweepy.
        '''
        self.data       = data
        self.tweet_ids  = list(data['tweets'].keys())
        self.tweets     = [self.data['tweets'][id]['text'] for id in self.tweet_ids]
        self.response   =   {str(tweet_id):
                                        {
                                            'classify'  :   {'categories': [], 'confidence': None},
                                            'sentiment' :   {'score': None, 'magnitude' :None}
                                        } 
                                        for tweet_id in self.tweet_ids
                            }

        self.client     = language_v1.LanguageServiceClient()
        self.type       = language_v1.Document.Type.PLAIN_TEXT
        self.documents  = [{'content': text, "type_": self.type} for text in self.tweets]
    
    def classify_text(self):
        """
        Classifying Content in a String
        """
        
        for i, document in enumerate(self.documents):
            tweet_id = str(self.tweet_ids[i])
            try:
                response = self.client.classify_text(request = {'document': document})
            except:
                raise Exception('Invalid text content: too few words')

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
                self.response[tweet_id]['classify']['categories'] = category_name
                self.response[tweet_id]['classify']['confidence'] = category_confidence

    def analyze_sentiment(self):
        """
        Analyzing Sentiment in a String
        """

        encoding_type = language_v1.EncodingType.UTF8
        for i, document in enumerate(self.documents):
            tweet_id = str(self.tweet_ids[i])
            try:
                response = self.client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
            except:
                raise Exception('Invalid text content: too few words')

            # Get overall sentiment of the input text
            self.response[tweet_id]['sentiment']['score']         = response.document_sentiment.score
            self.response[tweet_id]['sentiment']['magnitude']     = response.document_sentiment.magnitude


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

    data = {'tweets': {'1571983721024086018': {'text': '@chazman @aelluswamy Car will move on tighter gaps as we enhance NN velocity predictions for crossing traffic. 10.69.3 next month has some step-change improvements.', 'time': datetime.datetime(2022, 9, 19, 22, 4, 59), 'language': 'en'}, '1571935414448963586': {'text': '@Erdayastronaut @NASASpaceflight Booster 7 now returns to high bay for robustness upgrades &amp; booster 8 moves to pad for testing.\n\nNext big test is probably full stack wet dress rehearsal, then 33 engine firing in a few weeks.', 'time': datetime.datetime(2022, 9, 19, 18, 53, 2), 'language': 'en'}, '1571910415801516033': {'text': '@RonMadison11 @CathieDWood @federalreserve There is too much latency in Fed decisions. Problematic in a fast-changing world.', 'time': datetime.datetime(2022, 9, 19, 17, 13, 42), 'language': 'en'}, '1571540353978859526': {'text': '@NewsfromScience @ScienceVisuals Starship will be an incredible enabler for science. Full reusability &amp; high production rate drive several orders of magnitude improvement in $/kg to orbit &amp; beyond.\n\nNext gen Starlink constellation is primary user of this rocket, so science doesn’t need to cover fixed cost.', 'time': datetime.datetime(2022, 9, 18, 16, 43, 12), 'language': 'en'}, '1571261750640525313': {'text': '@erikbryn @ericschmidt @CondoleezzaRice @scsp_ai @Ukraine Hyperloop could do that trip in less than half an hour', 'time': datetime.datetime(2022, 9, 17, 22, 16, 8), 'language': 'en'}}, 'pinned': '', 'image': 'https://pbs.twimg.com/profile_images/1569943778198437888/iy7_UX5j_normal.jpg', 'banner': 'https://abs.twimg.com/images/themes/theme1/bg.png'}
    nlp = NLP(data)
    a = nlp.get_response()
    print(a)

