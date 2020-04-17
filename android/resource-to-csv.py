import xml.dom.minidom
from xml.dom.minidom import Node

filename = "C:/Users/bdelville/Desktop/android/script/python/strings.xml"
oputputfilename = "C:/Users/bdelville/Desktop/android/script/python/output.csv"
fileout = open(oputputfilename, "w")

doc = xml.dom.minidom.parse(filename)

for node in doc.getElementsByTagName("string"):
	name = node.getAttribute("name")
	line = name+";"
	
	try:
		line = line+node.firstChild.data
	except Exception:
		line = line+" "
		pass
	line = line + "\n"
	fileout.write(line)

	
for node in doc.getElementsByTagName("string-array"):
	name = node.getAttribute("name")
	line = name
	
	for item in node.getElementsByTagName("item"):
		line = line + ";"
		try:
			line = line+item.firstChild.data
		except Exception:
			line = line+" "
			pass
	line = line + "\n"
	fileout.write(line)
	
fileout.close();
