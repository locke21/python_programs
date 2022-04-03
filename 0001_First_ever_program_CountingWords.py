# --- Assignment from Dr. Chuck's "Python for Everybody" Specialization. Code written during first week(?) learning Python --- #
# --- Objective: Load text file and count how many unique words in the file --- #

# name = "words.txt"
name = input('enter file:')
file = open(name)

unique_words = dict()
for line in file:
    for word in line.split():
        unique_words[word] = unique_words.get(word, 0) + 1

times_word_used = None
most_used_word = None
for key, value in unique_words.items():
    if times_word_used is None or value > times_word_used:
        most_used_word = key
        times_word_used = value

print(most_used_word, times_word_used)


# --- This is my code remade after 3 months of Python Learning. --- #
# --- (Completed Dr. Chuck's 5 course Specialization, currently on Day 48 of Dr. Angela Wu's 100 Python Class) --- #

all_words = [word for word in file.read().split()]
unique_words = {word: all_words.count(word) for word in all_words}
most_used_word = max(unique_words, key=unique_words.get)

print(f'The word "{most_used_word}" was used {unique_words[most_used_word]} times, '
      f'making it the most used word out of {len(unique_words)} unique words. ')
