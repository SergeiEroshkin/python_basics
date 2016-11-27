import smtplib
smtp_object = smtplib.SMTP('smtp.mail.ru', 587)
smtp_object.ehlo()
# Enable encryption for SMTP connection:
smtp_object.starttls()
smtp_object.login('monty.python2017@mail.ru', 'MP1234567!')
smtp_object.sendmail('monty.python2017@mail.ru', 'applause+1.serg@gmail.com', 'Subject: Test SMTP')
smtp_object.quit()