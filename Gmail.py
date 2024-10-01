import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import sys
import pause
import os
from datetime import datetime
from colorama import init, Fore, Style
import requests

#you NEED PYTHON AND INSTALL THIS FRIST BEFORE RUNNING python3 Gmail.py

#Steps on Running this Clown show

#pip3 install pause
#pip3 install requests
#pip3 install python-dotenv
#pip3 install colorama
#python3 Gmail.py


load_dotenv()
init(autoreset=True)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
UserLastName = "Sanchez"
rank = "Seaman Recurit"
Full_title = rank + " " + UserLastName
os.system('clear') #Remove this Later this is for Looks in case I need to show it.
print(f"{Fore.RED}-Saul Sanchez{Fore.MAGENTA} I Love you StackoverFlow and the random people from {Style.BRIGHT}8+ year ago")

def check_password(url, password):
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"{Fore.RED}Failed to fetch content. Status code: {response.status_code}{Style.RESET_ALL}")
            return False
        
        content = response.text
        return password in content
    
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}An error occurred while checking password: {str(e)}{Style.RESET_ALL}")
        return False

class EmailBot:
    def __init__(self):
        self.image_path = None
        self.sender_email = "njrotcparlier@gmail.com" 
        self.password = os.getenv("Password")  #U Need 2-Step thing and make it a var in .env
        self.recipients = ["18001269@parlierusd.org" , "18000644@parlierusd.org"] #change the 18000644@parlierusd.org to User's email or something idk
        self.subject = "This was sent by a Bot"
        self.body_text = "hey"
        self.body_html = "<html><body><h1>Hello is Is " +Full_title+ "'s Receipt on " + current_time + "</h1><p>This is a <strong>test</strong> email.</p></body></html>"
        self.attachments = [] 
        #I hate this Send me Help, Why Can't we Just Use Gmail on the PreMade Slopp that companies made

    def setup_smtp(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, self.password)
        
    def send_email(self):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(self.recipients)
            msg['Subject'] = self.subject
            
            msg.attach(MIMEText(self.body_text, 'plain'))
            msg.attach(MIMEText(self.body_html, 'html'))

            if self.image_path:
                with open(self.image_path, 'rb') as image_file:
                    part = MIMEBase('image', 'png') 
                    part.set_payload(image_file.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename= {os.path.basename(self.image_path)}'
                    )
                    msg.attach(part)

            if self.attachments:
                for attachment in self.attachments:
                    with open(attachment, 'rb') as file:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(file.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment)}')
                        msg.attach(part)

            self.setup_smtp()
            self.server.send_message(msg)
            url = "https://raw.githubusercontent.com/Parlier-NJROTC/parlier-njrotc.github.io/f05d0d371a27cdf85665833003cea09d7470f13c/src/pages/Credits/secit/text.astro"

            result = check_password(url, os.getenv("BootPaswod"))
            print(f"{Fore.GREEN}Checking {Fore.BLUE}BootPaswod{Style.RESET_ALL}")
            pause.seconds(2)
            
            
            if result:
                os.system('clear')
                print(f"{Fore.RED}-Saul Sanchez{Fore.MAGENTA} I Love you StackoverFlow and the random people from {Style.BRIGHT}8+ year ago")
                print(f"{Fore.BLUE}BootPaswod {Fore.GREEN}matches{Style.RESET_ALL}")
            else:
                os.system('clear') 
                print(f"{Fore.RED}-Saul Sanchez{Fore.MAGENTA} I Love you StackoverFlow and the random people from {Style.BRIGHT}8+ year ago")
                print(f"{Fore.BLUE}BootPaswod {Fore.RED}does not match{Style.RESET_ALL}")
                exit()

            print(f"{Fore.GREEN}Email sent successfully to {', '.join(self.recipients)}{Style.RESET_ALL}")
            print(f"{Fore.BLUE}Current Time:{Fore.GREEN} {current_time}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}")

            

if __name__ == "__main__":
    email_bot = EmailBot()
    email_bot.image_path = "download (5).jpg"  
    email_bot.send_email()
