import logging
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


logging.basicConfig(
    # filename='example.log', 
    encoding='utf-8', level=logging.DEBUG)

config = dict()

def load_config(file_name="config.json"):
    """ Returns the config file information 
    NB. NOT IN USE AS YET
    """
    global config
    with open(file_name, "r") as jsonfile:
        data = json.load(jsonfile)
        logging.debug("Config file loaded.")
        config = data
        return data
load_config()

def gen_read_ministry_url(name='./employment links.xlsx') -> tuple:
    """ Open and extract data from excel file. """
    df = pd.read_excel(name)
    for ministry, url, *_ in df.values:
        yield (ministry, url)

def url_response(url) -> str:
    """ Return the http response for a given url """
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    return text

def keyword_included(str1:str, keyword:str)->bool:
    """ Confirms or denys if keyword is in text. """
    index = str1.find(keyword)
    return index != -1

def search_spreadsheet_for_job(keyword):
    """ Returns a nice list of ministries and websites of found jobs of given keyword. """
    ans = []
    for ministry,url in gen_read_ministry_url():
        try:
            text = url_response(url)
            if keyword_included(text, keyword):
                tup = (ministry, url)
                ans.append(tup)
        except HTTPError as err:
        # https://docs.python.org/3/library/urllib.error.html
            print('{} | {} | {}'.format(err.code, url, err.reason))
        except URLError as err:
            print('{} | {}'.format(url, err.reason))
    if len(ans) > 0:
        print("The keyword {} has the following matches.".format(keyword))
        # Return rows of Ministry and url
        for row in ans:
            print("{} | {}".format(ministry, url))
    else:
        print("There were no matches for the keyword '{}'.".format(keyword))