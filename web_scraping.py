import re
import requests
import bs4

#Email Finder
def mail_regex(text):
    matches = []
    emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+
                            @
                            [a-zA-Z0-9.-]+
                            (\.[a-zA-Z][^jpg]{2,4}))''', re.VERBOSE)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])
    print(matches)

#Phone no. Finder
def phone_regex(text):
    phoneNum=[]
    phoneRegex = re.compile(r'''((\d{3}|\(\d{3}\))?
                            (\s|-|\.)?
                            (\d{3})
                            (\s|-|\.)
                            (\d{4})
                            (\s*(ext|x|ext.)\s*(\d{2,5}))?
                            )''', re.VERBOSE)
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
    print(phoneNum)

print("Enter URL  from which you want to fetch email and phone number")
x=str(input())
r = requests.get(x)
soup = bs4.BeautifulSoup(r.text)
s=str(soup)
#print(soup)
print("Emails are : ")
mail_regex(s)
print("Phone numbers are")
phone_regex(s)
