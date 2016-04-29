from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def import_url():
    req = Request('http://rosettacode.org/wiki/Factorial',
                  headers={'User-Agent': 'Mozilla/5.0'})
    rosettaFile = urlopen(req)
    rosettaHtml = rosettaFile.read()
    rosettaFile.close()
    soup = BeautifulSoup(rosettaHtml, 'html.parser')
    return soup.get_text()


def print_text():
    req = Request('http://rosettacode.org/wiki/Factorial',
                  headers={'User-Agent': 'Mozilla/5.0'})
    rosettaFile = urlopen(req)
    for line in rosettaFile:
        print(line)

    # rosettaHtml = rosettaFile.read()
    # rosettaFile.close()
    # soup = BeautifulSoup(rosettaHtml, 'html.parser')
    # return soup.get_text()
