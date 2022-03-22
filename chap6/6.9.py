emailData = "From stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008"

slicedEmailData = emailData.find("@")
print(emailData[slicedEmailData + 1:].strip())
