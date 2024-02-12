from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import cv2
import time
import matplotlib.image
import numpy as np
import requests
# Define these once; use them twice!
def mail():
    print("sending mail")
    strFrom = 'email'
    strTo = ' email '

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>Got something on your door</b> and an image.<br><img src="cid:image1"><br>', 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open('t2.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    import smtplib
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.gmail.com')
    # smtp.login(strFrom, "kyfnzgnexcrusczr")
    # smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    # smtp.quit()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(strFrom, "your pass")
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())

cap = cv2.VideoCapture(1)
# temp=np.array([])
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
flag = 0
def wait(a):
    time.sleep(a)
while cap.isOpened():
    if flag == 1:
        flag = 0
        print('Something moved')
        wait(5)
        ret, frame = cap.read()
        matplotlib.image.imsave('t3.jpg', frame)
        url = 'http://127.0.0.1:5000'
        r = requests.post(url, files={'image': open('t3.jpg', 'rb')})
        matplotlib.image.imsave('t2.jpg', np.array(r.json()['result'])/255)
        if len(r.json()['output'])>0:
            mail()
            wait(10)
        continue
    ret, frame = cap.read()
    (humans, _) = hog.detectMultiScale(frame, winStride=(10, 10),
padding=(32, 32), scale=1.1)
    c = np.copy(frame)
    for (x, y, w, h) in humans:
        flag = 1
        
    
    cv2.imshow('Preview', c)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
