Without regular expression
def isPhoneNumber(text):
if len(text) != 12:
 return False
for i in range(0, 3):
 if not text[i].isdecimal():
 return False
 if text[3] != '-':
 return False
 for i in range(4, 7):
 if not text[i].isdecimal():
 return False
 if text[7] != '-':
 return False
 for i in range(8, 12):
 if not text[i].isdecimal():
 return False
 return True
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))


######################33



import pyperclip, re # Importing the libraries(this case: regex and pyperclip)
# Create phone regex.
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)
# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.
# Create email regex.
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-] + #username
 @ # @symbole
 [a-zA-Z0-9.-] + # domain
 (\.[a-zA-Z]{2,4}) # dot-something
 )''', re.VERBOSE)
# Find matches in the clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
 phoneNum = '-'.join([groups[1], groups[3], groups[5]])
 if groups[8] != '':
 phoneNum += ' x' + groups[8]
 matches.append(phoneNum)
for groups in emailRegex.findall(text):
 matches.append(groups[0])
if len(matches) > 0:
 pyperclip.copy('\n'.join(matches))
 print('Copied to clipboard: ')
 print('\n'.join(matches))
# TODO: Pasting the content --> txt file.
 s = pyperclip.paste() 
 with open('phone&emailfinder.txt','w') as g:
 g.write(s)
 g.close()
else:
 print('No phone numbers or email addresses found.')