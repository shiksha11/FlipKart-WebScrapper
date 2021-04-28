import requests 
from bs4 import BeautifulSoup
import csv

#Open csv to write the web scrapped data
csv_file = open('flipkart.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product Link","Product Name", "Offered Price", "Original Price"])


target = 'https://www.flipkart.com'
source = requests.get(target).text
soup = BeautifulSoup(source,'lxml')

#we are scrapping information about mobiles
mobiles  = soup.find_all('div' , class_ = "eFQ30H")[2]
link = mobiles.a  # a is the anchor tag

#requesting data for web page with mobiles info
source_fin = requests.get(link["href"]).text  
soup_fin = BeautifulSoup(source_fin,'lxml')
mobiles_list = soup_fin.find('a' , class_ = "_1jJQdf _2Mji8F")


#About 400 pages webpages have mobiles data. Here, I have web scrapped 3. 
for page_num in range(1,4):
    finn = f'{target}{mobiles_list["href"]}&page={page_num}'
    source_mobiles = requests.get(finn).text
    soup_mobiles_fin = BeautifulSoup(source_mobiles,'lxml')
    all_mobiles = soup_mobiles_fin.find_all('div' , class_ = "_2kHMtA")

    for mobiles in all_mobiles:
        Anchor = mobiles.a
        prod_Link = f'{target}{Anchor["href"]}'
        mobile_name = mobiles.find('div' , class_ = "_4rR01T").text
        mobile_price_offered = mobiles.find('div' , class_ = "_30jeq3 _1_WHN1").text
        
        #some products don't have original price mentioned.
        try:
            mobile_price_original = mobiles.find('div' , class_ = "_3I9_wc _27UcVY").text
        except Exception as e:
            mobile_price_original = "Not Available"

        csv_writer.writerow([prod_Link,mobile_name, mobile_price_offered, mobile_price_original])
print("Done! Find the web scrapped data in flipkart.csv file.") 




