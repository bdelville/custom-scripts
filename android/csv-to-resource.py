filename = "./output.csv"
oputputfilename = "./output.xml"
fileout = open(oputputfilename, "w")
file = open(filename, "r")

fileout.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n")

for line in file.readlines():
	col = line.split(";")
	length = len(col)
	
	if length == 2:
		fileout.write("\t<string name=\"" + col[0]+"\">" + col[1].split("\n")[0]+"</string>\n")
	elif length > 2:
		text = "\t<string-array name=\"" + col[0] +"\">\n"
		for i in range(1,length-1):
			text  = text + "\t\t<item>" + col[i] +"</item>\n"
		text = text + "\t</string-array>\n";
		fileout.write(text)

fileout.write("</resources>")
		
fileout.close();
file.close();
