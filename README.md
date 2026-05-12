[![Python Version](https://img.shields.io/badge/python-3.12+-blue)](https://www.python.org/downloads/)

# Graph-based Method for Unbiased Word Embeddings

This Project was my Final Project for my Natural Language Processing class (LING 581) in Fall 2023 at BYU.
The code has been cleaned up to make it easier to run. 

There is a project write-up in `LING581_FinalProject_NLP.pdf`, just note that my original code had some bugs, and what I said I did in the paper is not quite aligned, in particular, the Node2Vec variant I used. 

The original code is in the `original-code` branch. The `updated-code`branch has cleaned up, more efficient code, and additional plots. However, it also does not strictly adhere to what is described in the paper.

## Running the Code

1. First, run all the cells in `MakeGraph.ipynb`
2. Next run cells in `EmbeddingGeneration.ipynb`. This runs Node2Vec and generates embeddings. It also pulls in Google's pretrained embeddings.
3. Finally, run the cells in `GraphAndModelEvaluation.ipynb`. This performs analogy tests and creates visualizations to check for bias. 

## References

* Tolga Bolukbasi, Kai-Wei Chang, James Zou,
Venkatesh Saligrama, and Adam Kalai. 2016. Man is
to computer programmer as woman is to homemaker?
debiasing word embeddings.

* Google. 2013. word2vec-google-news-300. Word em-
beddings. December 18, 2023.

* Aditya Grover and Jure Leskovec. 2016. node2vec:
Scalable feature learning for networks.
Nicholas Léonard. 2013. questions-words.txt.
https://github.com/nicholas-leonard/
word2vec/blob/master/questions-words.txt.
Accessed: December 18, 2023.

* Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey
Dean. 2013. Efficient estimation of word representa-
tions in vector space.

* Princeton University. 2010. Wordnet: A lexi-
cal database for the english language. https:
//wordnet.princeton.edu/. Accessed: [Insert
Date].

* Various. 2009. Webster’s unabridged dictionary. https:
//www.gutenberg.org/ebooks/29765.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Or-
donez, and Kai-Wei Chang. 2018. Gender bias in
coreference resolution: Evaluation and debiasing
methods.
