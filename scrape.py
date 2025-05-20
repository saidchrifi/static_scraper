from bs4 import BeautifulSoup
import requests

# Get the HTML
target = requests.get("https://stripe.com/blog")
soup = BeautifulSoup(target.text, "html.parser")

# Extract all data requested
blogtitle = soup.find_all("a", class_="Link BlogIndexPost__titleLink")
blogauthor = soup.find_all("a", class_="BlogAuthor__link")
blogdate = soup.find_all("a", class_="Link BlogPostDate__link")

# Prepare data for saving later
data_lines = []

# Print results and collect lines
for title, author, date in zip(blogtitle, blogauthor, blogdate):
    block = (
        f"Title: {title.text.strip()}\n"
        f"Author: {author.text.strip()}\n"
        f"Date: {date.text.strip()}\n"
        + "-" * 40
    )
    print(block)
    data_lines.append(block)

# Prompt user to save to a text file
save = input("\nDo you want to save this data to a text file? (y/n): ").lower()

if save == "y":
    with open("stripe_blog_data.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(data_lines))
    print("Data saved to stripe_blog_data.txt")
else:
    print("Data not saved.")
