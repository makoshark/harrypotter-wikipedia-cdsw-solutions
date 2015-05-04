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

# output the counts by day
output_file = open("hp_edits_by_user.tsv", "w", encoding='utf-8')

# write a header
output_file.write("user\tedits\n")

# iterate through every day and print out data into the file
for user in edits_by_editor:
    output_file.write("\t".join([user, str(edits_by_editor[user])]) + "\n")

output_file.close()

