# !/usr/bin/python
# coding=utf-8

import random
import json
import requests
import os


class Word:
    def __init__(self, id, text):
        self.id = id
        self.text = text


def readDbFile():
    logfile = open('db.txt', 'r')
    dbList = logfile.readlines()
    logfile.close()
    return dict(zip(dbList, range(len(dbList))))


def getNewWord():
    while True:
        randomWord = getRandomWord()
        try:
            wordId = str(randomWord['id']) + '\n'
            newWord = dbMap[wordId]
        except KeyError:
            return Word(randomWord['id'], randomWord['Words']['Word'])


def sendWordToSlack(wordText):
    webhook_url = os.environ.get('SLACK')
    slack_data = {'text': wordText}

    response = requests.post(webhook_url, data=json.dumps(slack_data),
                             headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )


def getRandomWord():
    return random.choice(words)


def loadWordsFromJson():
    f = open('words.json', )
    wordsList = json.load(f)
    f.close()
    return wordsList


def isDbFull():
    return len(dbMap) is len(words)


def writeWordIdIntoDb(wordId):
    logfile = open('db.txt', 'a')
    logfile.write(str(wordId) + "\n")
    logfile.close()


if __name__ == "__main__":

    words = loadWordsFromJson()
    dbMap = readDbFile()

    if isDbFull():
        print('DB is full')
    else:
        word = getNewWord()
        writeWordIdIntoDb(word.id)
        sendWordToSlack(word.text)
