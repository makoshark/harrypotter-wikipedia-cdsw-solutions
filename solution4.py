# Q: Create graphs in a spreadsheet of the trend lines (i.e., edits per day over time) for the three most popular articles?

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

article_edits_by_day = {}

input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")
for row in DictReader(input_file, delimiter="\t"):
    title = row['title']

    if title not in top_articles:
        continue
    
    day = row['timestamp'][0:10]

    if day in article_edits_by_day:
        article_edits_by_day[day][title] = article_edits_by_day[day][title] + 1
    else:
        article_edits_by_day[day] = {}
        for tmp_title in top_articles:
            if tmp_title == title:
                article_edits_by_day[day][tmp_title] = 1
            else:
                article_edits_by_day[day][tmp_title] = 0


# STEP 4: print it all out
# output the counts by day
output_file = open("hp_edits_by_day_top3_articles.tsv", "w", encoding='utf-8')

# write a header
title_header_string = "\t".join(top_articles)

output_file.write("day\t" + title_header_string + "\n")

# iterate through every day and print out data into the file
for day in article_edits_by_day:
    title_values = []
    for title in top_articles:
        title_values.append(str(article_edits_by_day[day][title]))

    title_values_string = "\t".join(title_values)
    output_file.write("\t".join([day, title_values_string]) + "\n")

output_file.close()

# Example of interactive graph in Google Docs:
# http://mako.cc/go/0h
