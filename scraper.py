from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time

try:
    driver = webdriver.Chrome()  
except Exception as e:
    print(f"Error initializing the WebDriver: {e}")
    exit(1)

url = "http://127.0.0.1:5500/index.html"  

def fetch_data(url):
    driver.get(url)
    time.sleep(5) 
    return driver.page_source

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    restaurants = soup.find_all('div', class_='restaurant-class')  
    cleaned_data = []

    print(f"Found {len(restaurants)} restaurants.")  

    for restaurant in restaurants:
        
        name = restaurant.find('h2', class_='restaurant-name')  
        name = name.text.strip() if name else "N/A"
        
        
        rating = restaurant.find('div', class_='restaurant-rating') 
        rating = rating.text.strip() if rating else "N/A"
        
        
        description = restaurant.find('p', class_='restaurant-description')  
        description = description.text.strip() if description else "N/A"
        
        
        address = restaurant.find('a', class_='restaurant-address') 
        address = address.text.strip() if address else "N/A"
        
        cleaned_data.append({"Restaurant Name": name, "Rating": rating, "Description": description, "Address": address})
    
    return cleaned_data

def store_data(cleaned_data):
    try:
        with open('restaurants.csv', mode='w', newline='', encoding='utf-8') as file:  
            writer = csv.writer(file)
            writer.writerow(['Restaurant Name', 'Rating', 'Description', 'Address'])
            for data in cleaned_data:
                writer.writerow([data['Restaurant Name'], data['Rating'], data['Description'], data['Address']])
        print("Data stored successfully in 'restaurants.csv'.")
    except Exception as e:
        print(f"Failed to store data: {e}")

def main():
    html = fetch_data(url)
    cleaned_data = extract_data(html)
    
    
    print(f"Extracted data: {cleaned_data}")

    if cleaned_data:
        for data in cleaned_data:
            print(f"{data['Restaurant Name']}: {data['Rating']} ★")
            print(f"Description: {data['Description']}")
            print(f"Address: {data['Address']}")
        store_data(cleaned_data)
    else:
        print("No data to store.")

if __name__ == "__main__":
    main()
    driver.quit() 
