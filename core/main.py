import nltk
from nltk.chat.util import Chat

from dataset import data 


chat = Chat(data)
chat.converse()
