# anyisalin@gmail.com 2017-06-26
import requests
from bs4 import BeautifulSoup


def to_bs(page_content, parser='html.parser'):
    return BeautifulSoup(page_content, parser)


def get_bs(url, encoding='utf-8', parser='html.parser', *args, **kwargs):
    res = requests.get(url, *args, **kwargs)
    res.encoding = encoding
    return to_bs(res.text, parser)
