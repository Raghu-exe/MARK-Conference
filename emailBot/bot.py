import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'themarkconference@gmail.com'
EMAIL_PASSWORD = 'afhb zfga yfdo ymej'

def send_email(to_email, subject, image_path):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the image as an inline image
        with open(image_path, 'rb') as image_file:
            img = MIMEImage(image_file.read(), name=os.path.basename(image_path))
            img.add_header('Content-ID', '<pdfimage>')
            msg.attach(img)

        
        html_content = f'''
        <html>
        <body>
            <p>
            Dear Rutgers Students, <br>
                <br>
                Exciting news! Applications are now open to join the SWAT team for the upcoming MARK Conference! <br>
                <br>
                The MARK Conference is a prestigious event that brings together thought leaders, innovators, and professionals from various industries to share insights, inspire change, and of course encourage others to make their "MARK." As we prepare for this year's conference, we are looking for enthusiastic and dedicated individuals to join our SWAT team and play a crucial role in making the event a resounding success.<br>
                <br>
                SWAT team members will have the unique opportunity to contribute their skills, creativity, and passion to ensure that the MARK Conference exceeds expectations. This is a chance to be at the heart of an exciting event that promotes learning, networking, and personal growth. We are looking for team players who are committed, reliable, and ready to embrace the challenge. Your dedication will be a key factor in the success of the MARK Conference.<br>
                <br>
                <a href = "https://rutgers.campuslabs.com/engage/submitter/form/start/609592"> Click here to apply!! </a>
                <br
                If you have any questions or require further information, please do not hesitate to contact us.<br>
                <br>
                Thank you for considering this exciting opportunity. We look forward to receiving your applications and working together to make the MARK Conference an unforgettable experience. Be sure to stay updated through following emails, and follow our Instagram @markconference<br>
                <br>
            Best regards,<br>
            The MARK Conference Team<br>
            </p>
            <img src="cid:pdfimage" width="400" height="500">
        </body>
        </html>
        '''
        msg.attach(MIMEText(html_content, 'html'))

        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {str(e)}")

recipient_list = []
with open('cleanedSwatNames.txt', 'r') as file:
    for line in file:
        recipient_list.append(line.strip())


# Save the first page of the PDF as an image
image_path = 'swatInvite.png'

for recipient in recipient_list:
    subject = 'MARK Conference SWAT team applications are out!!'
    send_email(recipient, subject, image_path)

print("Script Ran!")