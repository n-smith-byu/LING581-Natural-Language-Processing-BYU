import re

import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize


contraction_mapping = {
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "hadn't": "had not",
    "don't": "do not",
    "doesn't": "does not",
    "didn't": "did not",
    "can't": "cannot",
    "couldn't": "could not",
    "shouldn't": "should not",
    "wouldn't": "would not",
    "mustn't": "must not",
    "mightn't": "might not",
    "needn't": "need not",
    "shan't": "shall not",
    "won't": "will not",
    "I'm": "I am",
    "you're": "you are",
    "he's": "he is",
    "she's": "she is",
    "it's": "it is",
    "we're": "we are",
    "they're": "they are",
    "that's": "that is",
    "who's": "who is",
    "there's": "there is",
    "here's": "here is",
    "what's": "what is",
    "how's": "how is",
    "where's": "where is",
    "he'd": "he would",
    "she'd": "she would",
    "I'd": "I would",
    "they'd": "they would",
    "I've": "I have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",
    "who've": "who have",
    "should've": "should have",
    "would've": "would have",
    "could've": "could have",
    "must've": "must have"
}

nltk_to_wordnet = {
    'NN':   ('n', 'singular', 'common'),     # Noun
    'NNS':  ('n', 'plural', 'common'),       # Noun, plural
    'NNP':  ('n', 'singular', 'proper'),     # Proper noun, singular
    'NNPS': ('n', 'plural', 'proper'),       # Proper noun, plural
    'VB':   ('v', 'base'),                    # Verb, base form
    'VBD':  ('v', 'past'),                    # Verb, past tense
    'VBG':  ('v', 'present', 'participle'),   # Verb, gerund/present participle
    'VBN':  ('v', 'past', 'participle'),      # Verb, past participle
    'VBP':  ('v', 'present', 'non-3rd-person', 'singular'),   # Verb, non-3rd person singular present
    'VBZ':  ('v', 'present', '3rd-person', 'singular'),       # Verb, 3rd person singular present
    'JJ':   ('a',),                                            # Adjective
    'JJR':  ('a', 'comparative'),             # Adjective, comparative
    'JJS':  ('a', 'superlative'),            # Adjective, superlative
    'RB':   ('r',),                            # Adverb
    'RBR':  ('r', 'comparative'),             # Adverb, comparative
    'RBS':  ('r', 'superlative')             # Adverb, superlative
}

wordnet_pos = {
    ('n', 'c'): ('n', 'singular', 'common'),
    ('n', 'p'): ('n', 'singular', 'proper'),
    'n': ('n',),
    'v': ('v', 'base'),
    'a': ('a',),
    's': ('a',),
    'r': ('r',)
}

def replace_match(match):
    return match.group(1) + contraction_mapping[match.group(2)] + match.group(3)

def replace_contractions(corpus):
    contractions = "|".join(contraction_mapping.keys())
    pattern = r'(^|\W)(' + contractions + ')($|\W)'
    return re.sub(pattern, replace_match, corpus)
    

def tokenize_1(text, max_len=9):
    text_expanded = replace_contractions(text)
    tokenized_sentence = word_tokenize(text_expanded)
    i = 0
    my_tokens = []
    while i < len(tokenized_sentence):
        best_cand = None
        best_j = i + 1
        for j in range(i + 1, min(len(tokenized_sentence) + 1, i + max_len + 1)):
            candidate = "_".join(tokenized_sentence[i:j])
            # print(candidate, len(wn.synsets(candidate)) > 0)
            if len(wn.synsets(candidate)) > 0:
                best_cand = candidate
                best_j = j
            # elif len(candidate.lower() in word_list:
            #     best_cand - candidate.lower()
            #     best_j = j

        if best_cand is not None:
            my_tokens.append(best_cand)
            i = best_j
        else:
            my_tokens.append(tokenized_sentence[i])
            i +=1
            
    return my_tokens


def get_correct_pos_tag(word, synset_pos_key=None):
    nltk_pos_tag = nltk.pos_tag([word])[0][1]
        
    pos = None
    if nltk_pos_tag in nltk_to_wordnet:
        pos = nltk_to_wordnet[nltk_pos_tag]
        if pos[0] == synset_pos_key and len(wn.synsets(word, pos=pos[0])) > 0:
            return pos
            
    if synset_pos_key == 'n':
        if word.lower() == word:
            pos = wordnet_pos[('n', 'c')]
        else:
            pos = wordnet_pos[('n', 'p')]
    else:
        pos = wordnet_pos[synset_pos_key]
        
    return pos

