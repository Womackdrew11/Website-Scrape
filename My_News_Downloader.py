import sys
import requests
from bs4 import BeautifulSoup

def Download_Art(url, fileName):
        response = requests.get(url)

        if response.status_code == 200:
            bs = BeautifulSoup(response.text, 'html.parser')
            content = bs.find('div', class_='KonaBody')
            if content:
                with open(fileName, 'w', encoding='utf-8') as f:
                    for paragraph in content.find_all('p'):
                        f.write(paragraph.get_text() + '\n')
                    print(f"Downloaded {fileName}")
            else:
                print(f"Unable to find article content in {url}")
        else: 
            print(f"Failed to download {url}")
            print(response.text)


def From_File(fileName):
    try:
        with open(fileName, 'r') as f:
            urls = f.readlines()
            for i, url in enumerate(urls):
                url = url.strip()
                fileName = f"article_{i+1}.txt"
                Download_Art(url, fileName)
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    websites = sys.argv[1]
    From_File(websites)
