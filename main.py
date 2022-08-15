import bs4 as bs
import urllib.request

url =
sauce = urllib.request.urlopen(url)
soup =bs.BeautifulSoup(sauce, 'lxml')

print(soup)
#print(soup.find_all('saga'))
