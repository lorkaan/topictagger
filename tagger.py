from .textAnalysis import getSignificant, getFreqDistFromLemmaPosTags

def getSignificantWords(text, threshold):
    wf = getFreqDistFromLemmaPosTags(text)
    return getSignificant(wf, threshold)

def createDocument(wordFreqDict):
    pass
