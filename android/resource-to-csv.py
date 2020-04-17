import xml.dom.minidom
from xml.dom.minidom import Node

fileName = 'strings'
projectName = 'my-module'

filename = "path/to/project/" + projectName + "/src/main/res/values/" + fileName + ".xml"
oputputfilename = "path/to/output/output-" + projectName + "-" + fileName + ".csv"
fileout = open(oputputfilename, "w")


def nodeDataToString(node):
	text = node.firstChild.data
	text = text.replace("\n", "\\n")
	return text
    # return text.encode('utf8') // If required

def readItemsArray(node):
	line = ""
	for item in node.getElementsByTagName("item"):
		try:
			if item.hasAttribute("quantity"):
				line = line + "quantity=" + item.getAttribute("quantity") + ";"
			line = line + nodeDataToString(item) + ";"
		except Exception:
			line = line + "error-script;"
			pass
	return line

################
# Start SCRIPT #
################
doc = xml.dom.minidom.parse(filename)

for node in doc.getElementsByTagName("string"):
	name = node.getAttribute("name")
	line =  "string;" + name + ";"
	
	try:
		line = line + nodeDataToString(node)
	except Exception:
		line = line + " "
		pass
	line = line + "\n"
	fileout.write(line)

	
for node in doc.getElementsByTagName("string-array"):
	name = node.getAttribute("name")
	line = "string-array;" + name + ";" + readItemsArray(node) + "\n"
	fileout.write(line)

	
for node in doc.getElementsByTagName("plurals"):
	name = node.getAttribute("name")
	line = "plurals;" + name + ";" + readItemsArray(node) + "\n"
	fileout.write(line)

fileout.close()
