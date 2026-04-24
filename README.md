#  Web Scraper (Selenium + BeautifulSoup)

##  Description

This project is a Python-based web scraper designed to extract links and images from web pages, including those that rely on JavaScript rendering. It uses Selenium to load dynamic content and BeautifulSoup to parse the HTML structure.

---

##  Objective

To demonstrate how to scrape modern websites that require JavaScript execution, and to extract structured data such as hyperlinks and images.

---

##  Features

* Headless browser scraping using Selenium
* Handles JavaScript-rendered pages
* Extracts all valid links (`<a>` tags)
* Extracts all images (`<img>` tags)
* Cleans and filters irrelevant or empty data
* Custom user-agent to reduce bot detection

---

##  Technologies Used

* Python
* Selenium
* BeautifulSoup (bs4)
* Chrome WebDriver

---

##  How to Run

### 1. Clone the repository

```
git clone https://github.com/yourusername/web-scraper.git
cd web-scraper
```

### 2. Install dependencies

```
pip install selenium beautifulsoup4
```

### 3. Download ChromeDriver

* Ensure your ChromeDriver version matches your Chrome browser
* Add it to your system PATH

---

### 4. Run the script

```
python scraper.py
```

Then enter a URL when prompted:

```
Enter the URL you want to scrape: https://example.com
```

---

##  Example Output

### Links:

```
1. Example Link → https://example.com/page
2. Another Link → https://example.com/about
```

### Images:

```
1. Logo → https://example.com/logo.png
2. Banner → https://example.com/banner.jpg
```

---

##  Security & Ethical Considerations

* Always respect a website’s **robots.txt** and terms of service
* Avoid scraping sensitive or private data
* Do not overload servers with repeated requests
* Use scraping responsibly and legally

---

##  What I Learned

* How to use Selenium for dynamic content scraping
* Parsing HTML using BeautifulSoup
* Handling headless browsers
* Filtering and cleaning extracted data
* Basic anti-detection techniques (user-agent customization)

---

##  Limitations

* Uses `time.sleep()` instead of dynamic waits (can be improved)
* Does not handle pagination or login-protected pages
* May still be detected by advanced anti-bot systems

---

## Future Improvements

* Implement `WebDriverWait` for better performance
* Add support for scraping specific elements (tables, APIs)
* Export data to CSV or JSON
* Add proxy and rotation support

---

##  Author

Joseph Okeke

##  Contact

* LinkedIn: (add your link)
