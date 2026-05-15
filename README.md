[![Python Version](https://img.shields.io/badge/python-3.12+-blue)](https://www.python.org/downloads/)

# Graph-based Method for Unbiased Word Embeddings

This Project was my Final Project for my Natural Language Processing class (LING 581) in Fall 2023 at BYU.
The code has been cleaned up to make it easier to run. 

There is a project write-up in `LING581_FinalProject_NLP_revised.pdf`. The paper has been revised to correct grammar and improve clarity, although the original can be found in the `backup/` directory. Just note that my original notebooks also had some bugs. What I said I did in the paper is not quite aligned with what I actually did in the code; in particular, the Node2Vec variant I used is slightly different. I was also using the wrong equation for analogy tests. The revised paper does not correct for these bugs, only grammatical errors. However, I am working on an updated version of the paper that will correct for these and will be labeled `v2.0`.

The original (albeit somewhat cleaned up) code I used is in the `original-code` branch. The `updated-code` branch has further cleaned and more efficient code, uses the standard `node2vec` package for the unweighted graph as well as the wrighted, corrects the bug in the analogy tests, and has additional experiments/plots. This will be where `v2.0` of the paper gets placed. 

## Project Write-Ups:

Latest (Updated Code):

- [In Progress]

Original (Revised):
- [`LING581_FinalProject_NLP_revised.pdf`](https://n-smith-byu.github.io/LING581-Natural-Language-Processing-BYU/backup/LING581_Final_Project_NLP_original.pdf)

Original:
*This is thew raw original version. Contains Bugs, Grammatical Errors, etc. This was simply the version I originally wrote for my class.*
- [`LING581_FinalProject_NLP_original.pdf`](https://n-smith-byu.github.io/LING581-Natural-Language-Processing-BYU/backup/LING581_Final_Project_NLP_original.pdf)

## Running the Code

1. First, run all the cells in `MakeGraph.ipynb`
2. Next run selected cells in `EmbeddingGeneration.ipynb`. This runs Node2Vec and generates embeddings for selected hyperparameters.
3. Finally, run cells for selected hyperparameters in `GraphAndModelEvaluation.ipynb`. This performs analogy tests, creates visualizations to check for bias, and compares to Google's Pretrained Word2Vec embeddings. 

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
