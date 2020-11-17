import tensorflow as tf
import numpy as np
import pickle 

class GruGenerator():
    def __init__(self):

        def loss(labels, logits):
            return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

        vectorizer = tf.keras.models.load_model('models/vectorizer')
        model = tf.keras.models.load_model('models/gru-generator/', custom_objects={'loss': loss})

        with open('assets/inverse_vocab.pkl', 'rb') as f:
            inverse_vocab = pickle.load(f)
        
        self.model = model
        self.vectorizer = vectorizer
        self.inverse_vocab = inverse_vocab
    
    def vectorize(self, input_text):
        '''Pass in a string to get a vectorized representation'''
        return self.vectorizer(input_text)
    
    def generate(self, input_vector):
        '''Pass in a vectorized input for a generated response, returns a vector'''
        return np.concatenate(np.concatenate(self.model.predict(input_vector).astype(int)))

    def to_words(self, word_vector):
        '''Pass in a vector to get a list of words'''
        return [self.inverse_vocab[i] for i in word_vector]

    