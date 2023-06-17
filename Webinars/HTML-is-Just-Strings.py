myContainer = ("peanut butter", "bread","milk","cheese puffs")
myHTMLString = "<ul>\n"
for item in myContainer:
	myHTMLString += "<li>{}</li>\n".format(item)
myHTMLString += "</ul>"
print(myHTMLString)