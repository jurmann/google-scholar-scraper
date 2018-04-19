import os
import sys
import csv
import urllib2
import requests

from time import sleep
from random import randint
from bs4 import BeautifulSoup


def get_data(urls=None):

    for url in urls:

        # query the website and return the html to the variable
        page = urllib2.urlopen(url)

        try:
            # parse the html using beautiful soup and store in variable `soup`
            soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")

            # get article title
            title = soup.find("h1", attrs={"class": "ArticleTitle"})
            article_title = title.text

            # get article date
            date = soup.find("span", attrs={"class": "ArticleCitation_Year"})
            article_date = date.text[:-2]

            # get list of authors
            authors_list = []
            authors = soup.find_all("span", attrs={"class": "authors__name"})
            for author in authors:
                authors_list.append(author.text)

            # convert the list to a string to write to csv
            authors_string = ', '.join(authors_list)
            print authors_string

            # get the contact email
            contact = soup.find("a", attrs={"class":"gtm-email-author"})
            contact_author = contact.parent.parent.parent.text[:-12]
            contact_email = contact.get('title')

            # get article keywords
            article_keywords = []
            keywords = soup.find_all("span", attrs={"class": "Keyword"})
            for keyword in keywords:
                article_keywords.append(keyword.text)
            keywords_string = ', '.join(article_keywords)

            output = [article_title, article_date, authors_string, contact_author, contact_email, keywords_string, url]

        # if anything goes wrong above, don't write to csv
        except:
            continue

        output_to_csv(output)


def get_urls(url, pages=1):

    urls = []

    n = 1
    while n <= pages:

        text = "&start="
        number = str((n - 1) * 10)
        google_results = str(url + text + number)

        # query the website and return the html to the variable
        response = requests.get(google_results)

        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.find_all('h3', attrs={'class' : 'gs_rt'}):
            urls.append(item.a['href'])
        n += 1

        # sleeping to not break google's policy
        sleep(randint(4, 8))
    get_data(urls)


def output_to_csv(data):
    # location where data is output in csv format (this is the location in the container)
    filename = './test_google_scholar_scaper.csv'
    file_exists = os.path.exists(filename)
    headers = ["article_title", "article_date", "authors_list", "contact_author", "contact_email", "article_keywords", "url"]

    # outputting data to csv file
    # NOTE: Excel does not show utf-8 characters
    with open(filename, 'a') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow([unicode(dat).encode("utf-8") for dat in data])


if __name__ == "__main__":
    URL = sys.argv[1]
    try:
        PAGES = int(sys.argv[2])
    except IndexError:
        PAGES = 1
    get_urls(URL, PAGES)
