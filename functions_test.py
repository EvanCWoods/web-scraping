# Create an empty array to be populated by URLS:
url_list = []


# Function to get URLS from user input:
def get_urls():
    url = input("Paste a url: ")
    url_list.append(url)
    print(len(url_list))
    print(url_list)
    another_url()


# Function to continue accepting URLS or end the loop:
def another_url():
    run_again = input("add another URL? (y/n)")

    if run_again == "y":
        get_urls()
    elif run_again == "n":
        print("ending loop")


# Function to isolate the URLS to be used to scrape at each URL:
def isolate_url():
    for url in url_list:
        print(url)


# Main function to execute the code:
def main():
    get_urls()
    isolate_url()


if __name__ == "__main__":
    main()
