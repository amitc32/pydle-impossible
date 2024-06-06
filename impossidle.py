#pydle-impossible
##############################
#     By Aidan Mitchell      #
##############################
#I don't know why anyone would play this, but if you're wanting a challenge, then here's a pretty good one
# Wordle, however then word will change based on what the available words are.
from logic import *

def main():
    word_list = load_word_list('words.txt')
    word_length = 5
    original_filtered_word_list = filter_word_list(word_list, word_length)
    
    if not original_filtered_word_list:
        print(f"No valid {word_length}-letter words available in the word list.")
        return

    known_letters = [None] * word_length
    not_in_word = set()
    chosen_word = choose_random_word(original_filtered_word_list)
    attempts = 8  # Number of attempts the user has

    print("Welcome to Wordle!")
    print(f"You have {attempts} attempts to guess the word.")

    while attempts > 0:
        guess = get_user_guess()
        
        filtered_word_list = filter_word_list_for_guess(original_filtered_word_list, known_letters, not_in_word)
        if not filtered_word_list:
            print("No words available with the current constraints. Resetting list.")
            available_letters = set("abcdefghijklmnopqrstuvwxyz") - not_in_word
            filtered_word_list = [word for word in original_filtered_word_list if all(letter in available_letters for letter in word)]
        
        if filtered_word_list:
            print("Choosing best word:")
            chosen_word = choose_best_word(filtered_word_list, guess, known_letters)
        
        if len(guess) != word_length:
            print(f"Your guess must be {word_length} letters long.")
            continue
        
        if guess not in word_list:
            print("Your guess is not in the word list.")
            continue
        result, new_known_letters, new_not_in_word = compare_words(chosen_word, guess)
        known_letters = [new_known_letters[i] if new_known_letters[i] is not None else known_letters[i] for i in range(len(known_letters))]
        not_in_word.update(new_not_in_word)
        print("Result:", result)

        if guess == chosen_word:
            print("Congratulations! You guessed the word!")
            break
        avail_letters = set("abcdefghijklmnopqrstuvwxyz") - not_in_word
        print("Available letters: ", avail_letters)
        attempts -= 1
        print(f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(f"Sorry, you are out of attempts. The word was: {chosen_word}")

if __name__ == "__main__":
    main()