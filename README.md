# Multi-Topic Chat Bot

The Multi-Topic Chat Bot is a simple Python program that engages in conversations with users on various topics, including football, movies, and music. The bot initiates conversations, responds to user queries, and provides information related to the selected topic.

## Features

- **Multiple Topics**: The bot supports discussions on three topics: football, movies, and music. Users can choose their preferred topic to chat about.

- **Random Questions**: The bot starts conversations with randomly selected questions specific to the chosen topic, making the conversation more engaging.

- **Intent Detection**: The bot uses regular expressions to detect user intents related to the selected topic.

- **Exit Commands**: Users can exit the conversation at any time using predefined exit commands.

## Usage

1. **Initialization**: When you run the program, the bot will greet you and ask for your name.

2. **Topic Selection**: You can choose one of the three topics (football, movies, or music) to start a conversation.

3. **Conversation**: The bot will initiate the conversation with a random question related to the chosen topic. You can respond to the questions, and the bot will continue the conversation accordingly.

4. **Exiting**: You can exit the conversation at any time by typing one of the exit commands (e.g., "quit," "bye," "exit").

## Code Structure

The code consists of a single Python script, `multi_topic_bot.py`, which contains the following components:

- **Class `MultiTopicBot`**: Defines the behavior of the chat bot and includes methods for greeting, topic selection, conversation, and intent detection.

- **Topic-Specific Regular Expressions**: Regular expressions are used to detect user intents related to football, movies, or music.

- **Random Questions**: A dictionary of random questions for each topic to initiate conversations.

## Prerequisites

- Python 3.x

## Running the Bot

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing `multi_topic_bot.py`.

3. Run the following command to start the chat bot:

   ```
   python multi_topic_bot.py
   ```

4. Follow the on-screen instructions to chat with the bot.

## Example Conversation

Here's an example of a conversation with the Multi-Topic Chat Bot:

```
Hey there, what's your name? Alice
Hi Alice, I'm a Multi-Topic Bot. Choose a topic to talk about: football, movies, or music. music
Music is a wonderful topic. What would you like to discuss about music? Tell me about your favorite music genre.
I love rock music.
Great choice! Movies are a fantastic topic. Do you prefer classic movies or modern ones?
I prefer classic movies.
That's interesting! Let's talk more about music. What's your all-time favorite musician or band?
I'm a big fan of The Beatles.
Music is a wonderful topic. What would you like to discuss about music? Have you been to any live music concerts recently?
No, I haven't been to any concerts lately.
I'm here to chat about various topics. Feel free to ask me anything.
exit
Okay, it was nice talking about music with you. Farewell!
```
