from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request

BASE_URL = 'http://www.rosettacode.org/wiki/Category:Programming_Tasks'

LANGUAGE_LIST = ['c highlighted_source',
                 'csharp highlighted_source',
                 'lisp highlighted_source',
                 'clojure highlighted_source',
                 'haskell highlighted_source',
                 'java5 highlighted_source',
                 'javascript highlighted_source',
                 'ocaml highlighted_source',
                 'perl highlighted_source',
                 'php highlighted_source',
                 'python highlighted_source',
                 'ruby highlighted_source',
                 'scala highlighted_source',
                 'scheme highlighted_source']


def setup_url(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    url_file = urlopen(req)
    url_html = url_file.read()
    url_file.close()
    soup = BeautifulSoup(url_html, 'lxml')
    return soup


def find_example_urls(soup):
    example_url_list = []
    for link in soup.find_all('a'):
        extension = link.get('href')
        if extension is not None:
            if (extension.startswith('/wiki/') and
                    ':' not in extension and
                    'Rosetta_Code' not in extension):
                extension = BASE_URL + extension
                example_url_list.append(extension)
    return example_url_list


def get_examples(soup):
    for language in LANGUAGE_LIST:
        file_name = language.split()[0] + '_output.txt'
        with open(file_name, 'a') as f:
            example = soup.find_all('pre', class_=language, limit=1)
            for code in example:
                f.write(' '.join(code.text.split()))


def main():
    code_soup = setup_url(BASE_URL)
    code_urls_list = find_example_urls(code_soup)
    for code_url in code_urls_list:
        code_soup = setup_url(code_url)
        get_examples(code_soup)

if __name__ == '__main__':
    main()
