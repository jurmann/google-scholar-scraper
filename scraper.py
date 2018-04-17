import urllib2
from bs4 import BeautifulSoup

# specify the url
def get_data(urls=None):


    # test urls
    quote_page = "https://link.springer.com/article/10.1007/s00253-017-8124-9"
    quote_page_2 = "https://link.springer.com/article/10.1007/s00253-005-0263-8"
    # query the website and return the html to the variable
    page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, "html.parser")

    # get article title
    title = soup.find("h1", attrs={"class": "ArticleTitle"})
    article_title = title.text

    date = soup.find("span", attrs={"class": "ArticleCitation_Year"})
    article_date = date.text[:-2]

    authors_list = []
    authors = soup.find_all("span", attrs={"class": "authors__name"})
    for author in authors:
        authors_list.append(author.text.replace(u'\xa0', u' '))

    # Take out the <div> of name and get its value
    name_box = soup.find("ul", attrs={"class": "test-contributor-names"})

    name = name_box.text # strip() is used to remove starting and trailing
    # print name

    # get the index price
    price_box = soup.find("a", attrs={"class":"gtm-email-author"})
    contact_author = price_box.parent.parent.parent.text[:-12]
    contact_email = price_box.get('title')


    article_keywords = []
    keywords = soup.find_all("span", attrs={"class": "Keyword"})
    for keyword in keywords:
        article_keywords.append(keyword.text.replace(u'\xa0', u' '))

    print article_title
    print article_date
    print authors_list
    print contact_author
    print contact_email
    print article_keywords



def output_to_csv(data):
    pass

if __name__ == "__main__":
    # pages = int(sys.argv[1])
    get_data()
