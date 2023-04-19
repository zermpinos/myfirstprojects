# Web Scrapper
import urllib.request
import urllib.error
from bs4 import BeautifulSoup


def extract_links_and_text(input_url_inner):
    with urllib.request.urlopen(input_url_inner) as response:
        html_content = response.read()
        text_content_inner = html_content.decode()
        soup = BeautifulSoup(html_content, 'html.parser')
        tags = soup('a')
        extracted_links_inner = [tag.get('href', None) for tag in tags]
    return extracted_links_inner, text_content_inner


input_url = input('Please give a valid url to scrape: ')

try:
    extracted_links, text_content = extract_links_and_text(input_url)
except urllib.error.URLError:
    print("Invalid URL")
else:
    print("\nThe links within are:")
    for link in extracted_links:
        print(link)
    print(f'\n\nThe text within is: {text_content}')
