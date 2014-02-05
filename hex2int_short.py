hex_file=open("hexnumber","r")#linux
hex_number=((hex_file.read()).replace('\n',"")).split(",")
print "--------------------------------------"
print hex_number
print "---------covert hex to int------------"
for i in hex_number:
      print (int(i,16)),#逗号，print不换行
hex_file.close()
print int("\n0x30",16)