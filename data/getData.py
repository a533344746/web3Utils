import random
import pandas as pd

def getSY(url):
    df = pd.read_csv(url)
    data = df.values.tolist()
    return data
def saveData(list):
    name = ['私钥', '时间', '是否成功']
    data = pd.DataFrame(columns=name, data=list)
    data.to_csv('data.csv', encoding='utf-16', index=False)
    return True
def saveFalData(list):
    name = ['私钥']
    data = pd.DataFrame(columns=name,data=list)
    data.to_csv('falData.csv', encoding='utf-16', index=False)
def getWord():

    df = pd.read_csv('word.csv')
    data = df.values.tolist()
    random_elements = random.sample(data, 3)
    data = ''
    for word in random_elements:
        data += " ".join(word)+" "
    return data
