import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('Hello How are YOU ... hahaha HaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('Hello How are YOU ... hahaha HaHaHaHaHa')
print(mo2.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())


