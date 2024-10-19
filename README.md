: Restaurant Data Scraper
This project is a web scraping tool built with Python, Selenium, and BeautifulSoup to extract restaurant data from an HTML file. The extracted data is then stored in a CSV file for further analysis or usage.

🚀 Features
Automated Web Scraping: Uses Selenium WebDriver to automate interaction with the HTML file and extract restaurant details.
BeautifulSoup Integration: Parses the HTML content to scrape specific data such as restaurant names, ratings, descriptions, and addresses.
CSV Export: Saves the scraped data to a CSV file, making it easy to work with in other tools or share with collaborators.
UTF-8 Encoding: Handles special characters like stars (★) in restaurant ratings seamlessly.
🛠️ Technologies Used
Python: The core language used for scripting.
Selenium: To automate the interaction with the web page and retrieve dynamic content.
BeautifulSoup: For parsing and navigating the HTML structure.
CSV Module: To store the extracted data in a structured format (CSV).
HTML: Basic HTML structure of the website containing restaurant listings.
📂 Project Structure
bash
Copy code
├── restaurants.csv         # Output file where the scraped data is stored
├── scraper.py              # Python script to scrape and store restaurant data
├── index.html              # Sample HTML file containing restaurant listings
├── README.md               # Project documentation (you're here!)

⚙️ Setup Instructions
Prerequisites
Python 3.x: Ensure you have Python installed. You can download it here.
Google Chrome: Selenium works with the Chrome browser. Download it here.
ChromeDriver: Ensure the ChromeDriver is installed and accessible in your PATH. You can download it here.
Installation
git clone https://github.com/your-username/restaurant-scraper.git
cd restaurant-scraper
Install the required Python libraries:

pip install selenium beautifulsoup4
Ensure that ChromeDriver is installed and added to your system's PATH.

Place the index.html file in the project directory. This is the file that contains the restaurant listings.

Usage
Run the scraper:

To run the scrapper in your terminal
python scraper.py
The script will open the HTML file, scrape restaurant data, and store the details in a restaurants.csv file.

Output: The CSV file will include columns for:

Restaurant Name
Rating
Description
Address
Example Output
Restaurant Name	Rating	Description	Address
The Zomato Kitchen	4.5 ★	A fine dining experience with gourmet dishes.	No. 1-06, I resident, Persiaran Surian...
Pasta Paradise	4.7 ★	Authentic Italian pasta made fresh daily.	456 Elm St, Cityville
🐞 Troubleshooting
Encoding Issues: If you encounter encoding errors, ensure that the CSV is written using UTF-8 encoding, which is already handled in this project.
WebDriverException: Make sure your ChromeDriver is compatible with your version of Chrome and that it’s correctly installed.
🤝 Contributing
Feel free to fork this repository and submit pull requests. If you find any issues, you can open a new issue on the GitHub repository.

📄 License
This project is open-source and available under the MIT License.

