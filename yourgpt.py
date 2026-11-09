import random
import string
import re
import json
import os

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "memory.json"
)

def clean_text(user_input):
    lower_text = user_input.lower()

    cleaned_text = "".join(
        char for char in lower_text
        if char not in string.punctuation
    )

    return cleaned_text

greetings = [
    "Hey! How can I help you?",
    "Hello there! Nice to see you!",
    "Heyyy! What's going on?"
]

how_are_you_responses = [
    "I'm doing great! Thanks for asking!",
    "I'm good! How about you?",
    "Doing awesome! What about you?"
]

goodbye_responses = [
    "Bye! Have a great day!",
    "See you soon!",
    "Take care! Come back anytime!"
]

thanks_responses = [
    "You're always welcome!",
    "Happy to help!",
    "Anytime! That's what I'm here for!"
]

smalltalk_responses = [
    "Not much! Just here chatting with you!",
    "I'm just hanging out here!",
    "Waiting for our next conversation!"
]

capability_responses = [
    "I can chat with you, answer simple questions and keep you company!",
    "I'm here to help you with simple questions and conversations!",
    "I can talk, respond and make your day a little better!"
]

progress_responses = [
    "Everything is going great! How about you?",
    "Pretty good! What about you?",
    "All good here! How's your day going?"
]

def get_response(cleaned_input):
    global user_name,fav_color
    words = cleaned_input.split()

    if not words:
        return "Please say something!", False

    elif "how are you" in cleaned_input:
        return random.choice(how_are_you_responses), False

    elif "what is your name" in cleaned_input or "whats your name" in cleaned_input or "who are you" in cleaned_input:
        return "I am YourGPT, your personal AI assistant!", False
    
    elif "thanks" in words or "thank" in words:
        return random.choice(thanks_responses), False

    elif "bye" in words or "goodbye" in words:
        return random.choice(goodbye_responses), True

    elif "what can you do" in cleaned_input or "what do you do" in cleaned_input:
        return random.choice(capability_responses), False

    elif "whats" in words and "up" in words:
        return random.choice(smalltalk_responses), False

    elif "how is it going" in cleaned_input:
        return random.choice(progress_responses), False
    

    elif "my name is" in cleaned_input:
        name = cleaned_input.split("my name is", 1)[1].strip().title()
        if name:
            user_name = name
            save_memory()
            return f"Nice to meet you, {user_name}!", False
        else:
            return "Please tell me your name.", False

    elif "what is my name" in cleaned_input or "whats my name" in cleaned_input or "do you remember my name" in cleaned_input:
        if user_name:
            return f"Your name is {user_name}!", False
        else:
            return "I don't know your name yet. Tell me your name!", False
    
    elif "my favourite colour is" in cleaned_input or "my favorite color is" in cleaned_input:
        if "my favourite colour is" in cleaned_input:
            color = cleaned_input.split("my favourite colour is")[-1].strip().title()
        else:
            color = cleaned_input.split("my favorite color is")[-1].strip().title()

        if color:
            fav_color = color
            save_memory()
            return f"I'll remember that your favourite colour is {fav_color}!", False

        else:
            return "Which colour do you like?", False
    
    elif "what is my favourite colour" in cleaned_input or "whats my favourite colour" in cleaned_input or "what is my favorite color" in cleaned_input or "whats my favorite color" in cleaned_input:

        if fav_color:
            return f"Your favourite colour is {fav_color}!", False

        else:
            return "You haven't told me your favourite colour yet!", False

    elif any(re.fullmatch(r"h+i+|he+y+|hel+o+", word) for word in words):
        return random.choice(greetings), False
    
    else:
        return "Sorry, I don't understand that yet. Can you rephrase?", False

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            memory = json.load(file)

            return (
                memory.get("user_name"),
                memory.get("fav_color")
            )

    except (FileNotFoundError, json.JSONDecodeError):
        return None, None

user_name, fav_color = load_memory()

def save_memory():
    memory = {
        "user_name": user_name,
        "fav_color": fav_color
    }

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)