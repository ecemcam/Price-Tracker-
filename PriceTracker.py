#In this project I scraped the Amazon website for a price of a shirt which i wanted to tarck its price if it's under 15$,
#I'm going to get notified by an email. 

#Importing necessary modules
from bs4 import BeautifulSoup
import requests
import time
import datetime 
import random
import smtplib 
import csv
import pandas as pd 

#Main Function which does everything 

def check_price():

    #The site I will scrape

    url = r"https://www.amazon.com/Data-Analyst-Gift-Analysis-Scientist/dp/B093DNRPJW/ref=sr_1_7?crid=YN8PENUMN0NH&dib=eyJ2IjoiMSJ9.K-5Pp6gJVOBwEEHxOoHfEu4JqUEoMNOPK_j0QM7cDmPk4QiLiupj20qcIEMx4rfuVzox8YBFJoJuFIyUSzWVrOaDd2tNx9rwNCIOirFJqt8B5OlfMjASbZkDAj5nm4IQXwtr8UFiMP2JtIpQ9BRVSKm66kZb1TETZll08TcwLM4iMDNeazKXHTuP6u2ncQJpCBZKWyAJGS6M64Z1BZknK-j2xlwYiScA2PvTFiyj8rD7XrPMXW8o7RfjhfT9pzRmrFP2IokZsyQYGVpfudDC5HLnOXyT-6bFYSoHAtQVcGPczLjPrN5YKItht9dHOs-onIMrlWlfmq3vEYEuP4qr1mLQfOiJqW2zzhB4K4vsMmAut-3ybnwxIvfsDttKVTB7aNCPP9doR9Mw_Dy-Dz1NOcQipGWFCxR9yQU25AULA_nXMT-E-6Ixe6YjgjQTJOEh.KGMYoSi1y2ufSGASPBLD9s1PZDLeH-A3cyznbt-hmF4&dib_tag=se&keywords=data%2Banalyst%2Bshirt&qid=1742399962&sr=8-7&th=1&psc=1"


     #Using Headers and time.sleep() in order to bypass bot detection on Amazon Website.

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
        }

    #Pause the program for random seconds between 3-7

    time.sleep(random.uniform(3, 11))

    #Making request to the url.

    resp = requests.get(url, headers=headers)


    #Parsing the response object into the html content.

    resp_html = BeautifulSoup(resp.content, "html.parser")

    #Finding the title of the product 

    title = resp_html.find('span', id='productTitle').text.strip()
    print(title)


    #Finding the Price of the product
    #just getting the numeric value and converting into float data type

    price_tag = resp_html.find('span', class_= 'aok-offscreen')                  
    Size_Small_Price = float(price_tag.text.strip()[1:])                        
    print(Size_Small_Price)

    #to know at which date i did the scraping
    today = datetime.date.today()

    headers = ['Title', 'Price', 'date']
    data = [title, Size_Small_Price, today]

    #once i created my csv file and saved, the next time is just gonna open it and append data into it ("a+")
    with open(r"C:\Users\user\Desktop\amazonScarper.csv", "a+", encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            #writer.writerow(headers )    #I don't want to append the headers again.
            writer.writerow( data)

    #Now, I'm going to read my latest data from the csv file
    df= pd.read_csv(r"C:\Users\user\Desktop\amazonScarper.csv")

    #get the last value of the Price column
    latest_price= df['Price'].iloc[-1]

    #I'm checking if the price is lower than  or equal to 15$ if it is then send the email to me.
    if latest_price <= 15:
        
        import smtplib
        def send_mail():
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)    #Create an ecrypted connection with the Gmail server.
            server.ehlo()
            
            # Use an App Password instead of real password
            server.login('senderEmail@gmail.com', 'XXXX XXXX XXXX XXXX')

            subject = "The Shirt you want is below $15! Now is your chance to buy!"
            body = "Hey, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams.  Link here: https://www.amazon.com/Data-Analyst-Gift-Analysis-Scientist/dp/B093DNRPJW/ref=sr_1_7?crid=YN8PENUMN0NH&dib=eyJ2IjoiMSJ9.K-5Pp6gJVOBwEEHxOoHfEu4JqUEoMNOPK_j0QM7cDmPk4QiLiupj20qcIEMx4rfuVzox8YBFJoJuFIyUSzWVrOaDd2tNx9rwNCIOirFJqt8B5OlfMjASbZkDAj5nm4IQXwtr8UFiMP2JtIpQ9BRVSKm66kZb1TETZll08TcwLM4iMDNeazKXHTuP6u2ncQJpCBZKWyAJGS6M64Z1BZknK-j2xlwYiScA2PvTFiyj8rD7XrPMXW8o7RfjhfT9pzRmrFP2IokZsyQYGVpfudDC5HLnOXyT-6bFYSoHAtQVcGPczLjPrN5YKItht9dHOs-onIMrlWlfmq3vEYEuP4qr1mLQfOiJqW2zzhB4K4vsMmAut-3ybnwxIvfsDttKVTB7aNCPP9doR9Mw_Dy-Dz1NOcQipGWFCxR9yQU25AULA_nXMT-E-6Ixe6YjgjQTJOEh.KGMYoSi1y2ufSGASPBLD9s1PZDLeH-A3cyznbt-hmF4&dib_tag=se&keywords=data%2Banalyst%2Bshirt&qid=1742399962&sr=8-7&th=1&psc=1 "

            msg = f"Subject: {subject} \n\n {body}"

            #Add recipient email address
            server.sendmail('senderEmail@gmail.com', 'recieverEmail@gmail.com', msg)

            # Properly close the connection
            server.quit()

        send_mail()

#This going to call the function above every day.
while(True):
      check_price()
      time.sleep(86,400)


