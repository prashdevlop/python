import re

#Email Finder
def mail_regex(text):
    matches = []
    emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+
                            @
                            [a-zA-Z0-9.-]+
                            (\.[a-zA-Z]{2,4}))''', re.VERBOSE)
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


test='''Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)


Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media

Twitter
Facebook'''

mail_regex(test)
phone_regex(test)
