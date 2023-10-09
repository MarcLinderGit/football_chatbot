# Importing regular expression (regex) and random libraries
import re
import random

class MultiTopicBot:
  # Potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # Keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # Random starter questions for different topics
  random_questions = {
    'football': (
        "Who's your favorite football team? ",
        "What do you think about the latest football match? ",
        "Do you play football yourself? ",
        "Who's the best football player in the world? ",
        "What's your favorite football stadium? ",
        "Tell me about your most memorable football moment. ",
        "Do you follow international football tournaments? "
    ),
    'movies': (
        "What's your favorite movie genre? ",
        "Have you watched any good movies lately? ",
        "Who's your favorite actor or actress? ",
        "What's the last movie that made you cry? ",
        "Do you prefer classic movies or modern ones? ",
        "Tell me about a movie you could watch over and over again. ",
        "Do you like going to the cinema? "
    ),
    'music': (
        "What's your favorite music genre? ",
        "Have you been to any live music concerts recently? ",
        "Who's your all-time favorite musician or band? ",
        "What's your go-to song when you're feeling down? ",
        "Do you play any musical instruments? ",
        "Tell me about a song that brings back fond memories. ",
        "Do you enjoy dancing to music? "
    )
  }

  def __init__(self):
    # Define regular expressions for different intents
    self.topic_intents = {
      'football': r'.*\s*(football|soccer).*',
      'movies': r'.*\s*(movie|film).*',
      'music': r'.*\s*(music|song|musician).*'
    }

  # Define the greeting method
  def greet(self):
    self.name = input("Hey there, what's your name? ")
    self.topic_choice = self.choose_topic()
    self.chat()

  # Define the method for checking if an exit command is present
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
        if exit_command in reply:
            return True
    return False

  # Define the method for choosing a topic
  def choose_topic(self):
    while True:
      topic_choice = input(f"Hi {self.name}, I'm a Multi-Topic Bot. Choose a topic to talk about: football, movies, or music. ").lower()
      if topic_choice in self.topic_intents:
        return topic_choice
      else:
        print("Please choose a valid topic: football, movies, or music.")

  # Define the main conversation method
  def chat(self):
    while True:  # Use an infinite loop to keep the conversation going
        topic_questions = self.random_questions[self.topic_choice]
        reply = input(random.choice(topic_questions)).lower()
        if self.make_exit(reply):
            break  # Exit the loop if an exit command is detected
        reply = self.match_reply(reply)
    print(f"Okay, it was nice talking about {self.topic_choice} with you. Farewell!")

  # Define the method for matching user input with topic-related intents
  def match_reply(self, reply):
    for intent, regex_pattern in self.topic_intents.items():
      found_match = re.match(regex_pattern, reply)
      if found_match:
        return self.topic_response(intent)

    return self.no_match_intent(reply)

  # Define responses for different topics
  def topic_response(self, intent):
    responses = {
      'football': "That's interesting! Let's talk more about football. ",
      'movies': "Great choice! Movies are a fantastic topic. ",
      'music': "Music is a wonderful topic. What would you like to discuss about music? "
    }
    return responses.get(intent, "I'm not sure what you want to talk about, but let's keep the conversation going!")

  # Define a method for responding when there's no intent match
  def no_match_intent(self, reply):
    responses = ("I'm here to chat about various topics. Feel free to ask me anything. ", "I didn't quite catch that. Let's continue the conversation. ")
    
    # Check if the user's input matches any exit commands
    if any(exit_command in reply for exit_command in self.exit_commands):
        return ""

    return random.choice(responses)

# Create an instance of MultiTopicBot below:
MultiTopicChatBot = MultiTopicBot()
MultiTopicChatBot.greet()
