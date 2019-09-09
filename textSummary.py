import heapq
import nltk
import re
import argparse


def getWeightedFrequency(formatted_text):
    ''' 
        Args: formatted_text
        Return: WeightedFrequency
        Word Frequency calculated by if the word is encountered for the first time, it is added to the dictionary as a key and its value is set to 1.
                Otherwise, if the word previously exists in the dictionary, its value is simply updated by 1.
        Word Weighted frequency calculated by divide the number of occurances of all the words by the frequency of the most occurring word.
    '''
    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

    return word_frequencies

def getSentenceScores(word_frequencies, sentences):
    ''' 
        Args: word_frequencies, sentences
        Return: sentence_scores
        check whether the sentence exists in the sentence_scores dictionary or not.
        If the sentence doesn't exist, we add it to the sentence_scores dictionary as a key and assign it the weighted frequency of the first word in the sentence,
        as its value.
    '''
    n_words = 17*arg
    sentence_scores = {}
    for i, sent in enumerate(sentences):
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < n_words:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    return sentence_scores

def getSummary(sentence_scores):
        ''' 
        Args: sentence_scores
        Return: summary
        '''
    summary_sentences = heapq.nlargest(arg, sentence_scores, key=sentence_scores.get) #get the highest number of sentence_scores
    def sort_pos(val):
        return val.split('#')[1]
    summary_sentences.sort(key=sort_pos)
    summary = []
    for sent in summary_sentences:
        s = sent.split('#')[0]
        summary.append(s)
    summary = '\n\t'.join(summary)
    return summary


if __name__ == "__main__":
    import sys
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-l", "--length", required=True, help="Number of Lines")
    #arg = vars(ap.parse_args())
    #arg = int(arg["length"])

    arg = int(sys.argv[2])
    path = sys.argv[1]

    with open(path, 'r') as file:
        text = file.read().replace('\n', '')

    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Removing special characters and digits
    formatted_text = re.sub('[^a-zA-Z]', ' ', text)
    formatted_text = re.sub(r'\s+', ' ', formatted_text)
    sentence_list = nltk.sent_tokenize(text)

    sentences = []
    for i, sent in enumerate(sentence_list):
        temp = list(sent)
        temp.append('#%s' % i)
        sentences.append("".join(temp))

    word_frequencies = getWeightedFrequency(formatted_text)

    sentence_scores = getSentenceScores(word_frequencies, sentences)

    summary = getSummary(sentence_scores)

    print("="*50+"SUMMARY"+"="*50+"\n\n"+"\t", summary)
