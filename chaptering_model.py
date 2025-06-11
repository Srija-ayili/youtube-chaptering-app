import nltk
from nltk.tokenize import sent_tokenize
import os

# Point to bundled nltk_data folder
nltk_data_path = os.path.join(os.path.dirname(__file__), "nltk_data")
nltk.data.path.append(nltk_data_path)

def split_text_into_chapters(text, max_words=100):
    sentences = sent_tokenize(text)
    chapters = []
    current = ""
    count = 0

    for sentence in sentences:
        words = sentence.split()
        if count + len(words) > max_words:
            chapters.append(current.strip())
            current = sentence + " "
            count = len(words)
        else:
            current += sentence + " "
            count += len(words)

    if current:
        chapters.append(current.strip())

    return [sent_tokenize(chap)[0] for chap in chapters]
