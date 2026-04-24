from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def spider(url):
    # Set up headless Chrome
    options = Options()
    options.add_argument("--headless")          
    options.add_argument("--disable-gpu")       
    options.add_argument("--no-sandbox")        
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/122.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    print(f"Loading {url} ...")
    driver.get(url)

    # Wait a little for JavaScript to load
    time.sleep(3)

    # Get page source *after* JavaScript loads
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Extract links 
    print("\n All Links (cleaned):")
    links = soup.find_all("a", href=True)
    for i, a_tag in enumerate(links, 1):
        text = a_tag.get_text(strip=True)
        href = a_tag["href"]

        if not text or href.startswith("#cite_ref") or href.startswith("#"):
            continue

        print(f"{i}. {text} → {href}")

    # Extract images
    print("\n All Images (cleaned):")
    images = soup.find_all("img", src=True)
    for j, img_tag in enumerate(images, 1):
        alt_text = img_tag.get("alt", "No alt")
        src = img_tag["src"]

        print(f"{j}. {alt_text} → {src}")

    driver.quit()


# Run the scraper
url = input("Enter the URL you want to scrape: ").strip()
spider(url)
