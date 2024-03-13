import random

def main():
    # Define all possible combinations of quantity and tense
    all_combinations = [
        (1, "past"),
        (1, "present"),
        (1, "future"),
        (2, "past"),
        (2, "present"),
        (2, "future")
    ]

    # Shuffle the combinations to randomize the order
    random.shuffle(all_combinations)

    # Set to store unique sentences
    unique_sentences = set()
    
    # Generate sentences for each combination
    for quantity, tense in all_combinations:
        sentence = make_sentence(quantity, tense)
        unique_sentences.add(sentence)

    # Print unique sentences
    for sentence in unique_sentences:
        print(sentence)


# Functions that generate the componentes needed to make a sentence
def get_determiner(quantity):
    """Return a randomly chosen determiner.

    Parameter:
        quantity: an integer.

    Return: a randomly chosen determiner.
    """
    determiners = {
        1: ["a", "one", "the"],
        2: ["some", "many", "the"]
    }

    # Randomly choose and return a determiner
    return random.choice(determiners[quantity])


def get_noun(quantity):
    """Return a randomly chosen noun.

    Parameter
        quantity: an integer 

    Return: a randomly chosen noun.
    """

    nouns = {
        1: ["bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"],
        2: ["birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"]
    }
    
    # Randomly choose and return a noun
    return random.choice(nouns[quantity])


def get_verb(quantity, tense):
    """Return a randomly chosen verb.

    Parameters
        quantity: an integer 
        tense: a string 

    Return: a randomly chosen verb.
    """

    verbs = {
        "past": ["drank", "ate", "grew", "laughed", "thought",
                "ran", "slept", "talked", "walked", "wrote"],
        "future": ["will drink", "will eat", "will grow", "will laugh",
                "will think", "will run", "will sleep", "will talk",
                "will walk", "will write"],
        "present": {
            1: ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"],
            2: ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"]
        }
    }

    # Randomly choose and return a verb
    if tense == "present":
        return random.choice(verbs[tense][quantity])
    else:
        return random.choice(verbs[tense])


def get_preposition():
    """Return a randomly chosen preposition

    parameters: none

    Return: a randomly chosen preposition.
    """

    prepositional_words = ["about", "above", "across", "after", "along",
                        "around", "at", "before", "behind", "below",
                        "beyond", "by", "despite", "except", "for",
                        "from", "in", "into", "near", "of",
                        "off", "on", "onto", "out", "over",
                        "past", "to", "under", "with", "without"]
    
    # Randomly choose and return a preposition
    return random.choice(prepositional_words)


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer 
        
    Return: a prepositional phrase.
    """

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    # Creates and returns a prepositional phrase
    return f"{preposition} {determiner} {noun}"


# Function to generate a sentence
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. 
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)

    # Creates and returns a finished sentence
    return f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}"


main()

   
# Submission Comment
# For exceeding the requirements I thought it would be fun to have randomize the order in which
# the sentences are given to you. In addition I used the set() function to make ensure all sentences are
# unique. This may seem like a small addition so below I added the progress of my logic. 

# First Attempt
# Tried using a counter to generate six random sentences.
# Could not ensure (single/past, single/present, single/future, plural/past, plural/present, plural/future)

# def main():
#     quantities = [1, 2]
#     tenses = ["past", "present", "future"]
#     sentence_count = 0

#     while sentence_count < 6:
#         quantity = random.choice(quantities)
#         tense = random.choice(tenses)
#         sentence = make_sentence(quantity, tense)
#         print(sentence)
#         sentence_count += 1


# Second Attempt
# Used set function to generate a unique list of 6 sentences
# Still did not ensure (single/past, single/present, single/future, plural/past, plural/present, plural/future)

# def main():
#     quantities = [1, 2]
#     tenses = ["past", "present", "future"]
#     unique_sentences = set()

#     while len(unique_sentences) < 6:
#         quantity = random.choice(quantities)
#         tense = random.choice(tenses)
#         sentence = make_sentence(quantity, tense)
#         unique_sentences.add(sentence)

#     for sentence in unique_sentences:
#         print(sentence)


# Final 
# Made a list of tuples that contained the sentence formats 
# Used the shuffel method to mix up sentence format combinations and kept set() for unique sentences
# Ensures (single/past, single/present, single/future, plural/past, plural/present, plural/future)

# def main():
    # all_combinations = [
    #     (1, "past"),
    #     (1, "present"),
    #     (1, "future"),
    #     (2, "past"),
    #     (2, "present"),
    #     (2, "future")
    # ]

    # random.shuffle(all_combinations)

    # unique_sentences = set()
    # for quantity, tense in all_combinations:
    #     sentence = make_sentence(quantity, tense)
    #     unique_sentences.add(sentence)

    # for sentence in unique_sentences:
    #     print(sentence)