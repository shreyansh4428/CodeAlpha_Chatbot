import random
import re
from datetime import datetime

BOT_NAME = "Chatty"

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache!",
    "I told my computer I needed a break, and it said: 'No problem, I'll go to sleep.'",
    "Why was the computer cold? It left its Windows open!",
    "There are 10 types of people: those who understand binary and those who don't.",
]

FACTS = [
    "Python was named after the comedy group Monty Python, not the snake.",
    "The first computer bug was a real moth found in a Harvard computer in 1947.",
    "The first website ever made is still online at info.cern.ch.",
    "Honey never spoils; edible honey has been found in ancient Egyptian tombs.",
    "A day on Venus is longer than a year on Venus.",
]

QUOTES = [
    "The only way to do great work is to love what you do.",
    "Success is the sum of small efforts repeated day in and day out.",
    "Don't watch the clock; do what it does. Keep going.",
    "It always seems impossible until it's done.",
]


def clean(text):
    """Lowercase the text and remove punctuation (except math symbols)."""
    text = text.lower().strip()
    return re.sub(r"[^a-z0-9+\-*/%. ]", "", text)


def has(text, *keywords):
    """True if any keyword/phrase appears as whole word(s) in the text."""
    padded = f" {text} "
    return any(f" {k} " in padded for k in keywords)


def calculate(text):
    """Solve simple math like '5 + 3' or 'calculate 12 * 4'. Returns None if no math found."""
    match = re.search(r"(-?\d+\.?\d*)\s*([+\-*/%])\s*(-?\d+\.?\d*)", text)
    if not match:
        return None
    a, op, b = float(match.group(1)), match.group(2), float(match.group(3))
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            return "I can't divide by zero!"
        result = a / b
    else:
        if b == 0:
            return "I can't divide by zero!"
        result = a % b
    result = int(result) if result == int(result) else round(result, 4)
    return f"The answer is {result}."


def get_response(user_input):
    """Return the bot's reply for the given user message."""
    text = clean(user_input)

    if text == "":
        return "Please type something so I can reply."

    # ---- Math ----
    math_answer = calculate(text)
    if math_answer:
        return math_answer

    # ---- Greetings and small talk ----
    if has(text, "hello", "hi", "hey", "hii", "hola", "namaste"):
        return random.choice(["Hi!", "Hello there!", "Hey! Nice to see you."])
    elif has(text, "good morning"):
        return "Good morning! Hope you have a great day."
    elif has(text, "good afternoon"):
        return "Good afternoon! How is your day going?"
    elif has(text, "good evening"):
        return "Good evening! How was your day?"
    elif has(text, "good night"):
        return "Good night! Sleep well."
    elif has(text, "how are you", "how r u", "how are you doing", "whats up", "sup"):
        return "I'm fine, thanks! How about you?"
    elif has(text, "i am fine", "im fine", "i am good", "im good", "i am great", "im great"):
        return "That's great to hear!"
    elif has(text, "i am sad", "im sad", "i am tired", "im tired", "i am bored", "im bored"):
        return "Sorry to hear that. Maybe a joke or a fun fact will help. Just ask!"

    # ---- About the bot ----
    elif has(text, "your name", "who are you", "what are you"):
        return f"I'm {BOT_NAME}, a simple rule-based chatbot written in Python."
    elif has(text, "who made you", "who created you", "who built you", "your creator"):
        return "I was created by a Python student as a programming project."
    elif has(text, "how old are you", "your age"):
        return "I'm brand new! I was born the moment this program started."
    elif has(text, "where do you live", "where are you from"):
        return "I live inside your computer, in a Python file."
    elif has(text, "are you a robot", "are you human", "are you real"):
        return "I'm a program, not a human, but I'm happy to chat."
    elif has(text, "what can you do", "help", "commands", "options"):
        return ("I can chat, tell jokes, share facts and quotes, tell the time and date, "
                "do simple math (try 12 * 4), and answer basic questions about Python, "
                "programming and general topics. Type 'bye' to exit.")

    # ---- Time and date ----
    elif has(text, "time", "what time is it"):
        return "The current time is " + datetime.now().strftime("%I:%M %p") + "."
    elif has(text, "date", "today", "what day is it"):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
    elif has(text, "year"):
        return "The year is " + str(datetime.now().year) + "."

    # ---- Fun ----
    elif has(text, "joke", "make me laugh", "funny"):
        return random.choice(JOKES)
    elif has(text, "fact", "tell me something", "interesting"):
        return random.choice(FACTS)
    elif has(text, "quote", "motivate", "motivation", "inspire", "inspiration"):
        return random.choice(QUOTES)
    elif has(text, "flip a coin", "coin"):
        return "It's " + random.choice(["heads", "tails"]) + "!"
    elif has(text, "roll a dice", "roll dice", "dice"):
        return "You rolled a " + str(random.randint(1, 6)) + "."
    elif has(text, "favorite color", "favourite colour", "favourite color", "favorite colour"):
        return "I like blue, the color of a terminal cursor!"
    elif has(text, "favorite food", "favourite food", "what do you eat"):
        return "I run on electricity, but pizza sounds great!"
    elif has(text, "favorite movie", "favourite movie", "favorite song", "favourite song"):
        return "I enjoy anything with a good plot, just like a good algorithm."
    elif has(text, "weather"):
        return "I can't check live weather, but a weather app or website will tell you."
    elif has(text, "love you", "i like you"):
        return "Aww, thank you! You're awesome."
    elif has(text, "i hate you", "you are stupid", "stupid", "idiot"):
        return "That's not very nice, but I'll keep trying to help."
    elif has(text, "are you smart", "are you intelligent"):
        return "I only know what my code tells me, but I try my best."

    # ---- Python and programming ----
    elif has(text, "what is python", "about python", "python"):
        return ("Python is a popular, beginner-friendly programming language used for web "
                "development, data science, automation and AI.")
    elif has(text, "what is programming", "what is coding", "what is code"):
        return "Programming is writing instructions that tell a computer what to do."
    elif has(text, "what is a variable", "variable"):
        return "A variable is a named container that stores a value, like age = 18."
    elif has(text, "what is a loop", "loop", "for loop", "while loop"):
        return ("A loop repeats code. A 'for' loop goes through a sequence, and a "
                "'while' loop repeats as long as a condition is true.")
    elif has(text, "what is a function", "function", "def"):
        return "A function is a reusable block of code. In Python you define one with 'def'."
    elif has(text, "what is a list", "list"):
        return "A list is an ordered, changeable collection of items, like [1, 2, 3]."
    elif has(text, "what is a string", "string"):
        return "A string is text inside quotes, like 'hello'."
    elif has(text, "what is a dictionary", "dictionary", "dict"):
        return "A dictionary stores key-value pairs, like {'name': 'Sam', 'age': 20}."
    elif has(text, "if else", "if elif", "condition", "conditional"):
        return "if/elif/else lets your program choose between different actions based on conditions."
    elif has(text, "what is an algorithm", "algorithm"):
        return "An algorithm is a step-by-step set of instructions for solving a problem."
    elif has(text, "what is a bug", "bug", "debug", "debugging"):
        return "A bug is an error in code. Debugging means finding and fixing it."
    elif has(text, "what is ai", "artificial intelligence", "machine learning"):
        return "AI is when machines do tasks that normally need human intelligence, such as learning or understanding language."
    elif has(text, "what is a chatbot", "chatbot"):
        return "A chatbot is a program that talks with users. I'm a simple rule-based one that replies using if-elif rules."
    elif has(text, "what is html", "html"):
        return "HTML is the markup language that structures web pages."
    elif has(text, "what is java", "java"):
        return "Java is a widely used, object-oriented programming language."
    elif has(text, "how to learn programming", "learn coding", "learn python"):
        return "Practice daily, build small projects, read other people's code, and don't fear errors."

    # ---- General knowledge ----
    elif has(text, "capital of india"):
        return "The capital of India is New Delhi."
    elif has(text, "capital of france"):
        return "The capital of France is Paris."
    elif has(text, "capital of japan"):
        return "The capital of Japan is Tokyo."
    elif has(text, "capital of usa", "capital of america"):
        return "The capital of the USA is Washington, D.C."
    elif has(text, "prime minister of india"):
        return "I may be out of date on that. Please check a news source for the current answer."
    elif has(text, "national animal of india"):
        return "The national animal of India is the Bengal tiger."
    elif has(text, "national bird of india"):
        return "The national bird of India is the Indian peacock."
    elif has(text, "largest planet"):
        return "Jupiter is the largest planet in our solar system."
    elif has(text, "largest ocean"):
        return "The Pacific Ocean is the largest ocean."
    elif has(text, "tallest mountain"):
        return "Mount Everest is the tallest mountain above sea level."
    elif has(text, "how many days in a year"):
        return "A year has 365 days, or 366 in a leap year."
    elif has(text, "how many continents"):
        return "There are 7 continents."
    elif has(text, "speed of light"):
        return "The speed of light is about 299,792 kilometers per second."
    elif has(text, "boiling point of water"):
        return "Water boils at 100 degrees Celsius (212 F) at sea level."
    elif has(text, "who invented the telephone"):
        return "Alexander Graham Bell is credited with inventing the telephone."
    elif has(text, "who invented the computer"):
        return "Charles Babbage is called the 'father of the computer' for his Analytical Engine."
    elif has(text, "who is the father of python", "who created python"):
        return "Python was created by Guido van Rossum."

    # ---- Study and life ----
    elif has(text, "study tips", "how to study", "exam", "exams"):
        return "Study in short focused sessions, revise regularly, sleep well, and test yourself with practice questions."
    elif has(text, "how to focus", "concentrate", "procrastination"):
        return "Remove distractions, work in 25-minute blocks, and take short breaks."
    elif has(text, "career", "job"):
        return "Pick a skill you enjoy, build projects, and keep learning. Opportunities follow."
    elif has(text, "friend", "friends"):
        return "Good friends are valuable. Be kind and they'll be there for you."
    elif has(text, "music", "song", "songs"):
        return "Music is great for focus. Try instrumental playlists while coding."
    elif has(text, "game", "games"):
        return "I like games! You might enjoy making your own, like Hangman."

    # ---- Thanks and goodbye ----
    elif has(text, "thanks", "thank you", "thx", "ty"):
        return "You're welcome!"
    elif has(text, "sorry"):
        return "No problem at all!"
    elif has(text, "ok", "okay", "cool", "nice", "great", "awesome"):
        return "Glad you think so!"
    elif has(text, "yes", "yeah", "yep"):
        return "Great!"
    elif has(text, "no", "nope"):
        return "Alright, no worries."
    elif has(text, "bye", "goodbye", "see you", "exit", "quit", "good bye"):
        return "Goodbye!"

    # ---- Fallback ----
    else:
        return random.choice([
            "I'm not sure I understand. Try rephrasing, or type 'help' to see what I can do.",
            "Hmm, I don't know that one yet. Ask me about Python, math, jokes or the time.",
            "Sorry, I don't have an answer for that. Type 'help' for ideas.",
        ])


def chat():
    """Main chat loop."""
    print("=" * 50)
    print(f"  {BOT_NAME} - A Simple Rule-Based Chatbot")
    print("  Type 'help' to see what I can do, 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print(f"{BOT_NAME}: {reply}")

        if clean(user_input) in ("bye", "goodbye", "good bye", "exit", "quit", "see you"):
            break


if __name__ == "__main__":
    chat()