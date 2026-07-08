import csv

def load_words():
    
    with open("/home/charan/telegram-word-bot/words/vocabulary_words.csv","r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        words = list(reader)

    return words