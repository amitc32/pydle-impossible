import random

def load_word_list(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]
    return words

def filter_word_list(word_list, length):
    return [word for word in word_list if len(word) == length]

def choose_random_word(word_list):
    randnum = random.randint(0, len(word_list) - 1)
    return word_list[randnum]

def filter_word_list_for_guess(word_list, known_letters, not_in_word):
    filtered_words = []
    for word in word_list:
        if all(letter not in word for letter in not_in_word):
            if all(known_letters[i] is None or word[i] == known_letters[i] for i in range(len(known_letters))):
                filtered_words.append(word)
    return filtered_words

def choose_best_word(word_list, guess, known_letters):
    min_common_letters = float('inf')
    best_word = None
    
    for word in word_list:
        if word == guess:
            continue  # Avoid choosing the same word as the user's guess
        common_letters = sum(1 for letter in word if letter in guess and letter not in known_letters)
        if common_letters < min_common_letters:
            min_common_letters = common_letters
            best_word = word
            
    return best_word if best_word is not None else random.choice(word_list)  # Ensure a word is always returned

def get_user_guess():
    return input("Enter your guess: ").strip().lower()

def compare_words(chosen_word, guess):
    result = []
    known_letters = [None] * len(chosen_word)
    not_in_word = set()
    for i in range(len(chosen_word)):
        if guess[i] == chosen_word[i]:
            result.append(f"{guess[i].upper()}")  # Correct letter in the correct position
            known_letters[i] = guess[i]  # Retain correct letter in known letters
        elif guess[i] in chosen_word:
            result.append(f"{guess[i].lower()}")  # Correct letter but in the wrong position
        else:
            result.append("_")  # Incorrect letter
            # Add to not_in_word only if the letter is not anywhere in chosen_word
            if guess[i] not in chosen_word:
                not_in_word.add(guess[i])
    return "".join(result), known_letters, not_in_word