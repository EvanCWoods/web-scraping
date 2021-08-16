from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://www.amazon.ca/s?i=electronics&bbn=677246011&rh=n%3A677246011%2Cp_72%3A11192170011&s=popularity-rank&dc&page=2&pf_rd_i=677246011&pf_rd_p=b58db8d3-f665-5c65-8d3c-1c6bcceaf315&pf_rd_r=YYWHWYB5MRQZJKBFDMYF&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&qid=1628816609&ref=sr_pg_2'

titles = []
prices = []


def create_client():
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    return page_html


def scrape():
    page_soup = soup(create_client(), "html.parser")
    containers = page_soup.findAll("div", {"class" : "a-section a-spacing-none"})
    print(len(containers))

    filename = "book_info.csv"
    f = open(filename, "w")
    headers = "title, Price \n"
    f.write(headers)

    for book in containers:
        try:
            title_containers = book.find("h2", {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-4"})
            title = title_containers.a.span.text
            titles.append(title)
        except:
            title = "No title"
            print(title)

        try:
            price_containers = book.find("div", {"class": "a-row a-size-base a-color-base"})
            price = price_containers.a.span.span.text
            prices.append(price)
        except:
            price = "no price"
            print(price)
        f.write(title.replace(",", "|") + "," + price + "\n")


# Main function to execute the web scraping:
def main():
    scrape()
    print("titles: ", len(titles))
    print("prices: ", len(prices))


if __name__ == "__main__":
    main()

