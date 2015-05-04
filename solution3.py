# Q: Create graphs in a spreadsheet of the trend lines (i.e., edits per day over time) for the three most active editors?

from csv import DictReader

# STEP 1: read in the input file and count by day
input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")

edits_by_editor = {}
for row in DictReader(input_file, delimiter="\t"):
    user = row['user']

    if user in edits_by_editor:
        edits_by_editor[user] = edits_by_editor[user] + 1
    else:
        edits_by_editor[user] = 1

input_file.close()


# STEP 2: find the list of the top 3 editor
top_editors = []
for user in sorted(edits_by_editor, key=edits_by_editor.get, reverse=True):
    if len(top_editors) >= 3:
        break
    else:
        top_editors.append(user)

# STEP 3.1: first, create a dictionary of dictionaries, one per user
user_edits_by_day = {}
for user in top_editors:
    user_edits_by_day[user] = {}


# STEP 3.2: now, fill that by doing a version of the first count by
# going back through the original data and this time just count each
# of the three editors

input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")
for row in DictReader(input_file, delimiter="\t"):
    user = row['user']
    
    if user not in top_editors:
        continue

    day = row['timestamp'][0:10]

    if day in user_edits_by_day[user]:
        user_edits_by_day[user][day] = user_edits_by_day[user][day] + 1
    else:
        user_edits_by_day[user][day] = 1


# STEP 4: print it all out
# output the counts by day
output_file = open("hp_edits_by_day_top3_users.tsv", "w", encoding='utf-8')

# write a header
output_file.write("user\tday\tedits\n")

# iterate through every day and print out data into the file
for user in top_editors:
    for day in user_edits_by_day[user]:
        output_file.write("\t".join([user, day, str(user_edits_by_day[user][day])]) + "\n")

output_file.close()

# Example of interactive graph in Google Docs:
# http://mako.cc/go/0g
