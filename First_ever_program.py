# --- First Assignment from Dr. Chuck's "Python for Everybody" Specialization. First day learning Python --- #
# --- Objective: Load text file and count how many unique words in the file --- #
# --- The file works off the auto-grader from Coursera so the outputs/Variables makes more sense there --- #

# name = "words.txt"
name = input('enter file:')
file = open(name)

all_words = dict()
for line in file:
    for word in line.split():
        all_words[word] = all_words.get(word, 0) + 1

times_word_used = None
most_used_word = None
for key, value in all_words.items():
    if times_word_used is None or value > times_word_used:
        most_used_word = key
        times_word_used = value

print(f'The word "{most_used_word}" was used {times_word_used} times, '
      f'making it the most used word out of {len(all_words)} unique words. ')
