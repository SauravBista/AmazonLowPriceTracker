import requests
from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

BASE_PRICE = 1200
AMAZON_PRODUCT_URL = "https://www.amazon.com/Celestron-NexStar-6-SE-Telescope/dp/B000GUKTDM/ref=sr_1_11?crid=3TEZ471VJMKPV&dib=eyJ2IjoiMSJ9.oitv7gaWDHb1Mb5RQaHgcHe0j4DT37PdVPrn5208HrtTY06IOzLlZv16699f7mwq-kSRhVSjNnWU2HZrhMD9HqGvjYQbYTz1mNbZQMZ6xPt8anUg0XLPRI0qloKzo2HlLiWlkRNeLluo4UIk0kU93R4FGTMhfExsfu1b20ew3Q2DdGtilsaBHzwaRyoqGlgnbFz2nwWXICTek81tKeV5lJLnjBXGXdYAjpll56vbLNA.Q0Q636O38T_qLx5O4nOtoFO3Qb4YlVbBTnVY8loFrZo&dib_tag=se&keywords=telescope&qid=1722761685&sprefix=teles%2Caps%2C343&sr=8-11"
PRODUCT_DESCRIPTION = "Celestron - NexStar 6SE Telescope - Computerized Telescope for Beginners and Advanced Users - Fully-Automated GoTo Mount - SkyAlign Technology - 40,000 Plus Celestial Objects - 6-Inch Primary Mirror "
header = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"

}
response = requests.get(url=AMAZON_PRODUCT_URL, headers=header)
website = response.text

# Extracting the price
soup = BeautifulSoup(website, "lxml")
price = soup.find(name="span", class_="a-price-whole").text
final_price = price.split(".")[0]
final_price = final_price.replace(",", "")
float_price = float(final_price)

# Building the message
msg = MIMEMultipart()
msg_body = f"{PRODUCT_DESCRIPTION} is now available now at only {float_price}, grab it now at {AMAZON_PRODUCT_URL}"
msg.attach(MIMEText(msg_body, 'plain'))

# Sending the mail
if float_price < BASE_PRICE:
    my_email = os.environ.get('my_email')  # Your email here
    password = os.environ.get('my_password')  # Your Password here
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=os.environ.get('my_email'), msg=msg.as_string())  # destination email in to_addrs
