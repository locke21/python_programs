# --- Assignment for Dr. Chuck's Coursera Python Specialization(for beginners) --- #
# --- Original code written first 1-2 weeks of learning Python --- #

name = input("Enter file:")
# file = open("mbox-short.txt")
file = open(name)

email_sender_counts = dict()
for line in file:
    if line.startswith("From:"):
        line = line.rstrip()
        emailer = line.find(":")
        emailer = line[emailer+2:]
        user_count = emailer.split()
        for user in user_count:
            email_sender_counts[user] = email_sender_counts.get(user, 0) + 1

mostsent = -1
topsender = None
for key, value in email_sender_counts.items():
    if value > mostsent:
        mostsent = value
        topsender = key
print(topsender, mostsent)


# --- Code rewritten 3 months later. Finished Dr. Chuck's 5 course specialization --- #
# --- Currently on day 48 of Dr. Angela Wu's 100 Days of Code Python Course --- #

email_sender_list = [line.rstrip().replace("From: ", "") for line in file if line.startswith("From:")]
email_sender_counts = {emailer: email_sender_list.count(emailer) for emailer in email_sender_list}
print(max(email_sender_counts, key=email_sender_counts.get), max(email_sender_counts.values()))
