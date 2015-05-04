# Q: What are the most edited articles on Harry Potter on Wikipedia?

from csv import DictReader

# read in the input file and count by day
input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")

edits_by_article = {}
for row in DictReader(input_file, delimiter="\t"):
    title = row['title']

    if title in edits_by_article:
        edits_by_article[title] = edits_by_article[title] + 1
    else:
        edits_by_article[title] = 1

input_file.close()

# I used this answer here:
# https://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value

for title in sorted(edits_by_article, key=edits_by_article.get, reverse=True):
    print(title)
