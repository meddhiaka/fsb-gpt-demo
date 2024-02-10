import sys

import nltk
from nltk.chat.util import Chat

from dataset import data 

input_v = sys.argv[1]

chat = Chat(data)

result = chat.respond(input_v)

print(result)