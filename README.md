# google-scholar-scraper

Retrieves email addresses in google scholar results.

Currently, this will only work for the Google Scholar (or Google) search results for the site Springer.com in html (not pdfs since they don't contain emails). More sites will be added in the future.

### Install Code  

1) Clone the repository: `git clone https://github.com/jurmann/google-scholar-scraper.git`  
2) Create a virtual environment: `virtualenv env`  
    - if you don't have virtualenv run `pip install virtualenv`  
    - if you don't have pip run `sudo easy_install pip`  
3) Enter virtual environment `source env/bin/activate`
4) Run `pip install -r requirements.txt`

### Run Code  
1) In your browser, perform a google scholar search with whatever parameters you choose (one of your parameters should be `site:springer.com` to limit results to that site.  
   - e.g. `site:springer.com heart transplant`  
2) copy the url of the search results  
3) Enter your terminal, go to the correct directory and enter the virtual environment
4) Run `python scraper.py "[google search url]" [number of google pages to parse through]`  
** make sure the google search url is in quotes  

### Limitations
- code only works for articles in html on springer.com  

