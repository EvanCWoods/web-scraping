from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://www.amazon.ca/Russia-History-Books/b?ie=UTF8&node=928842'


def create_client():
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    return page_html


def scrape():
    page_soup = soup(create_client(), "html.parser")
    containers = page_soup.findAll("li", {"class" : "octopus-pc-item octopus-pc-item-v3"})

    filename = "book_info.csv"
    f = open(filename, "w")
    headers = "title, Price \n"
    f.write(headers)

    for book in containers:
        title_containers = book.find("span", {"class": "a-size-base a-color-base"})
        title = title_containers.text
        price_containers = book.find("span", {"class": "a-price"})
        price = price_containers.text.strip()
        f.write(title.replace(",", "|") + "," + price + "\n")


# Main function to execute the web scraping:
def main():
    scrape()


if __name__ == "__main__":
    main()

