import textAnalysis as ta

def getSignificantWords(text, threshold):
    wf = ta.getFreqDistFromLemmaPosTags(text)
    return ta.getSignificant(wf, threshold)

def createDocument(wordFreqDict):
    pass