import nltk
from nltk.chat.util import Chat, reflections

from reflections import custom_reflections
from dataset import data 

reflections.update(custom_reflections)

chat = Chat(data, reflections)
chat.converse()
