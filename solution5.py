# Q: Instead of "binning" your dataset by day, change to bin it by month for each of the two previous questions.

# This is a modified version of solution4.py. Changing solution3.py
# would be similar.

from csv import DictReader

# STEP 1: read in the input file and count by article
input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")

edits_by_article = {}
for row in DictReader(input_file, delimiter="\t"):
    title = row['title']

    if title in edits_by_article:
        edits_by_article[title] = edits_by_article[title] + 1
    else:
        edits_by_article[title] = 1

input_file.close()


# STEP 2: find the list of the top 3 articles
top_articles = []
for title in sorted(edits_by_article, key=edits_by_article.get, reverse=True):
    if len(top_articles) >= 3:
        break
    else:
        top_articles.append(title)


# STEP 3: now, fill that by doing a version of the first count by
# going back through the original data and this time just count each
# of the three articles

article_edits_by_month = {}

input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")
for row in DictReader(input_file, delimiter="\t"):
    title = row['title']

    if title not in top_articles:
        continue

    # NOTE: this line is the key difference
    month = row['timestamp'][0:7]

    if month in article_edits_by_month:
        article_edits_by_month[month][title] = article_edits_by_month[month][title] + 1
    else:
        article_edits_by_month[month] = {}
        for tmp_title in top_articles:
            if tmp_title == title:
                article_edits_by_month[month][tmp_title] = 1
            else:
                article_edits_by_month[month][tmp_title] = 0


# STEP 4: print it all out
# output the counts by month
output_file = open("hp_edits_by_month_top3_articles.tsv", "w", encoding='utf-8')

# write a header
title_header_string = "\t".join(top_articles)

output_file.write("month\t" + title_header_string + "\n")

# iterate through every month and print out data into the file
for month in article_edits_by_month:
    title_values = []
    for title in top_articles:
        title_values.append(str(article_edits_by_month[month][title]))

    title_values_string = "\t".join(title_values)
    output_file.write("\t".join([month, title_values_string]) + "\n")

output_file.close()

# Example of interactive graph in Google Docs:
# http://mako.cc/go/0i
