import heapq
import nltk
import re
import argparse


def getWeightedFrequency(formatted_text):
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
    summary_sentences = heapq.nlargest(arg, sentence_scores, key=sentence_scores.get)
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
