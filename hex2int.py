hex_file=open("hexnumber.txt","r")#windows
hex_number=(hex_file.read()).split(",")
print hex_number
print "---------covert hex to int------------"
dec_number=[]#首先要创建一个空的list
for i in hex_number:
     dec_number.append(int(i,16))#才能追加
print dec_number
print "----------------End-------------------"
hex_file.close()

print int("\n0x30",16)#换行不影响转换

#split()是string方法，但是生成的是list
#strip(rm)是string方法，删除的是string开头或者结尾的rm
#本例应该使用replace('/n',"")，来把所有的换行去掉
#可以在print后面加，来使其不换行
