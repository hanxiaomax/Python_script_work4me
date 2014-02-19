#coding: utf-8 #解决中文注释问题

"""----------------------------------------
十六进制和二进制转换函数,可以控制界面的进出
-----------------------------------------"""
def hexNbin():
	choice=raw_input("1.hex2bin\n2.bin2hex\nR.return\n")#raw_input得到字符串
	if choice.lower()=="r":
		return  #利用return跳出函数，退回MENU
	while(choice.lower()!="x"):
		while(choice=="1"):
			temp=raw_input("Please input a hex number(x to exit):")
			if temp=="x":
				break #跳出循环，进入上级菜单
			print bin(int(temp,16)).replace("0b","")#int接受的是字符串而bin接受的是数
		while(choice=="2"):
			temp=raw_input("Please input a int number(x to exit):")
			if temp=="x":
				break
			print hex(int(temp,2))

		choice=raw_input("1.hex2bin\n2.bin2hex\nR.return\n")
		if choice.lower()=="r":
			return

bi_code=["11101110","11011110","10111110","01111110",
		"11101101","11011101","10111101","01111101",
		"11101011","11011011","10111011","01111011",
		"11100111","11010111","10110111","01110111",]


"""----------------------------------------
打印键盘模型和对应编码
-----------------------------------------"""
def matrix_key_code():
	for line in range(0,4):
		print
		print "".join("   x   "*4)

def show_keyboard_code():
	for line in range(0,16):
		if line%4==0:
			print
		print "  "+str(hex(int(bi_code[line],2))),
	print
	print
	
		

print "-------------------MENU-----------------------------"
fun_choice=raw_input("1.hex<--->bin\n2.show keyboard code\n (x to exit)\n")
while(fun_choice.lower()!="x"):
	while(fun_choice=="1"):
		hexNbin()
		print "-------------------MENU-----------------------------"
		fun_choice=raw_input("1.hex<--->bin\n2.matrix_key_code\n (x to exit)\n")
	while(fun_choice=="2") :
		print	
		matrix_key_code()
		show_keyboard_code()
		print "-------------------MENU-----------------------------"
		fun_choice=raw_input("1.hex<--->bin\n2.matrix_key_code\n (x to exit)\n")



"""--------------------------------------
1.是否可以加入GUI，通过按键控制X的分布
----------------------------------------"""