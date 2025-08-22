from scholarly import scholarly
import re

AUTHOR_ID = "lyQ8qi8AAAAJ"
MY_NAME = ["Micah Oevermann", "Micah J Oevermann", "Micah James Oevermann"]

MINOR_TITLE_WORDS = ["A", "The"]

# Fetch author profile
author = scholarly.search_author_id(AUTHOR_ID)
author = scholarly.fill(author, sections=["basics", "publications"])

articles = []
conferences = []

def clean_key(s):
    """Return alphanumeric only for bibtex key parts"""
    return re.sub(r'\W+', '', s)

for i, pub in enumerate(author['publications']):
    pub_filled = scholarly.fill(pub)   # get full metadata
    bib = pub_filled['bib']

    title = bib.get("title", "Untitled")
    year = bib.get("pub_year", "n.d.")
    authors = bib.get("author", "Unknown").split(" and ")

    # Format key: FirstAuthorLastName + Year + FirstWordOfTitle
    first_author_lastname = clean_key(authors[0].split()[-1])

    first_word = clean_key(title.split()[0])
    if first_word in MINOR_TITLE_WORDS:
        first_word = clean_key(title.split()[1]) # take the second word

    key = f"{first_author_lastname}{year}{first_word}"

    # Bold your name in author list
    formatted_authors = []
    for a in authors:
        if  a in MY_NAME:
            formatted_authors.append(f"\\textbf{{{a}}}")
        else:
            formatted_authors.append(a)
    authors_str = " and ".join(formatted_authors)

    # Decide entry type based on venue
    venue = bib.get("venue", "").lower()
    if "conference" in list(bib.keys()):
        entry_type = "inproceedings"
        collection = conferences
    elif "journal" in list(bib.keys()):
        entry_type = "article"
        collection = articles
    else: 
        print(f"couldnt find a conference or journal in dict keys for")
        print(bib['title'])
        print("adding it to conferences")
        collection = conferences

    # Build BibTeX entry
    entry = f"@{entry_type}{{{key},\n"
    entry += f"  title = {{{title}}},\n"
    entry += f"  author = {{{authors_str}}},\n"
    if "venue" in bib:
        entry += f"  journal = {{{bib['venue']}}},\n"
    if "pub_year" in bib:
        entry += f"  year = {{{bib['pub_year']}}},\n"
    if "volume" in bib:
        entry += f"  volume = {{{bib['volume']}}},\n"
    if "number" in bib:
        entry += f"  number = {{{bib['number']}}},\n"
    if "pages" in bib:
        entry += f"  pages = {{{bib['pages']}}},\n"
    if "publisher" in bib:
        entry += f"  publisher = {{{bib['publisher']}}},\n"
    entry += "}\n\n"

    collection.append(entry)

# Write outputs
with open("./publications/journal_articles.bib", "w", encoding="utf-8") as f:
    f.writelines(articles)

with open("./publications/conference_papers.bib", "w", encoding="utf-8") as f:
    f.writelines(conferences)

print(f"Wrote {len(articles)} journal articles to journal_articles.bib")
print(f"Wrote {len(conferences)} conference papers to conference_papers.bib")
