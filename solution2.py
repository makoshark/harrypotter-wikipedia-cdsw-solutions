# Q: Who are the 5 most active editors on articles in Harry Potter? How may edits have they made?

from csv import DictReader

# read in the input file and count by day
input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")

edits_by_editor = {}
for row in DictReader(input_file, delimiter="\t"):
    user = row['user']

    if user in edits_by_editor:
        edits_by_editor[user] = edits_by_editor[user] + 1
    else:
        edits_by_editor[user] = 1

input_file.close()

# I used this answer here:
# https://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

num_printed = 0
for user in sorted(edits_by_editor, key=edits_by_editor.get, reverse=True):
    print(user + " : " + str(edits_by_editor[user]))
    if num_printed >= 4:
        break
    else:
        num_printed = num_printed + 1
        
