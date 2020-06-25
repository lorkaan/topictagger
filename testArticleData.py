import pandas as pd
import tagger

def createDataFrameFromCSV(filepath, cols):
    return pd.read_csv(filepath, usecols=cols)

'''
Shows an example of how to run the tagger interface.

Also used for testing over some Kaggle Data on News Articles.
found at: https://www.kaggle.com/snapcrack/all-the-news

Current threshold uses word count instead of percentage.

'''

if __name__ == '__main__':
    headerArray = ["id", "content"]
    fileArray = []
    for i in range(1,4):
        fileArray.append(f"data/articles{i}.csv")
    df = createDataFrameFromCSV(fileArray[0], headerArray)
    words = tagger.getSignificantWords(df["content"][0], 5)
    print(words)
    
