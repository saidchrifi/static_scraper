🕸️ static_scraper
A beginner-friendly Python script that scrapes data from static web pages using requests and BeautifulSoup.

This is my first ever coding project, built for learning and experimenting with web scraping. The script currently scrapes blog data from Stripe as an example, but you can easily adapt it to any other static website.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
How to Use

Change the target URL

Edit the target = requests.get(...) line to the website you want to scrape.

Update HTML tags and class names

Modify the .find_all() lines to match the structure of your new site (you can inspect HTML with your browser's dev tools).

Customize the output

Edit the print and formatting section to match the kind of data you want to display or save.

Run and enjoy your data!

Optionally, save the results to a text file when prompted.




---------------------------------------------------------------------------------------------------------------------------------------------------------------

Dependencies:
-requests
-beautifulsoup4
--pip install requests beautifulsoup4
--
