from chatterbot import ChatBot
import nltk
from chatterbot.trainers import  ListTrainer


my_bot = ChatBot(name= 'BlackBot',
              logic_adapters=[
                  'chatterbot.logic.MathematicalEvaluation',
                              'chatterbot.logic.BestMatch'])
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?']
list_trainer = ListTrainer(my_bot)
for item in (small_talk):
    list_trainer.train(item)

print(my_bot.get_response("hi"))
