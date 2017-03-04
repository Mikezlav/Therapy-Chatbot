import re
import random

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "my",
    "you": "me",
    "me": "you",
    "this": "that",
    "did": "have done",
}

conversations = [
    [r'I need (.*)',
     ["Why do you need {0}?",
     "Would it really help you to get {0}",
     "Are you sure you need {0}?"]],

    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
     "Perhaps eventually I will{0}.",
     "Do you really wamt me to {0}?"]],

    [r'I feel (.*)',
     ["Why do you feel {0}.",
     "Can I help you feel better."]],

     [r'My (.*) hurts',
      ["Why does your {0} hurt?",
      "Go to the doctor."]],
]
