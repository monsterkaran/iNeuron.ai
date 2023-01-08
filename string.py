s="ineuron"
print(type(s))
print(s[0])
print(s[5])
s1='sudh'
print(s1[-1])
s2="this is my very first programming class's"
print(s2)
print(s2[1:5])
print(s2[6:30])
print(s2[6:30:2])
s3="sudhanshu"
print(s3[0:9:2])
print(s3[0:8:-1])
print(s3[8:0:-1])
print(s3[8:0:-2])
print(s3[:-3])
print(s3[-2:])
print(s3[::1])
print(s3[0:50:1])
print(s3[::-1])
print(s2[::-1])
s4="ineuron"
print(s4)
print(s4[-2:-7:1])
print(s4[-7:-1:1])
print(s4[5:0:1]) #contradiction - jump in +ve direction
print(s4[5:0:-1])
print(s4[-7:0:1]) # 0 & -7 is the same position
print(s4[:-1:-1]) #blank
#print(s4+1) #we have to convert the data type to a string
print(s4+'1') #these are called string concatination
print(s4+"1")
print(s4+str(1))
print(s4)
print(len(s4))
print(len(s3))
print(s3*2)
print(s3.count('sudhanshu'))
print(s3.split('u'))
print("12345")
print(type(s3.split('u')))
sw="Since 1990, Samsung has increasingly globalised its activities and electronics; in particular, its mobile phones and semiconductors have become its most important source of income. It was in this period that Samsung started to rise as an international corporation in the 1990s. Samsung's construction branch was awarded contracts to build one of the two Petronas Towers in Malaysia, Taipei 101 in Taiwan and the Burj Khalifa in United Arab Emirates.[26] In 1993, Lee Kun-hee sold off ten of Samsung Group's subsidiaries, downsized the company, and merged other operations to concentrate on three industries: electronics, engineering and chemicals. In 1996, the Samsung Group reacquired the Sungkyunkwan University foundation.[citation needed]"
print(sw.split(' '))
print(sw.count('Samsung'))
print(sw.upper())
print(sw.lower())
s="sudhanshu kumar"
print(s.title())
print(s.capitalize())
s="Sudhanshu kuMAR"
print(s.swapcase())
print(''.join(reversed(s)))
print(s[::-1])
s="   su   dh   "
print(s.strip()) #print without before and after space of the string
print(s)
print(s.lstrip())
print(s.rstrip())
print("a".join("sudhanshu"))
s="sudhhanshu"
print(s.center(20,'$'))
print(s.isupper())
s="SUDH"
print(s.isupper())
print(s.islower())
print(s.isspace())
s4="   "
print(s4.isspace())
s5="2323"
print(s5.isdigit())
s6="sdf123"
print(s6.isdigit())
s="Sudhanshu"
print(s)
print(s.isalnum())
s7="123444dfjhvj"
print(s7.isalpha())
print("777")
print(s)
print(s.startswith('i'))
print(s.startswith('s'))
print(s.startswith('S'))
print(s.endswith('u'))
print(s7)
print(s)
print(s.isdigit())
print(s.isnumeric())
print(s.startswith(""))
print(s.isascii())
s="sudhanshu\tkumar\tineuron"
print(s.expandtabs())
s="this is my first python programming class and i am learNING python string and its function"
#1.Try to extract data from index one to index 300 with a jump of 3
print(s[0:300:3])
#2.Try to reverse a string without using reverse function
print(len(s))
print(s[::-1])
#3.Try to split a string after conversion of entire string in uppercase
print(s.upper().split(' '))
#4.Try to convert the whole string into lowercase
print(s.lower())
#5.Try to capitalize the whole string
print(s.capitalize())
print(s.title())
#6.write a difference b/w isalnum() and isalpha()
# ans:- isalnum()/isalpha() is a string method that returns true/false. where isalnum() returns true if sting is completely either numeric/alphabet else false. and isalpha() returns true if string consist of only alphabets other than tis it returns false
#7.Try to give an example of expand tab
#8.Give an example of strip , lstrip and rstrip
# ans:- strip-print without before and after space of the string , lstrip-print without left space of the string , rstrip-print without right space of the string
#9.replace a string character by another character by taking
#  your own example "sudhanshu"
s="sudhanshu"
print(s.replace("s", "z"))
#10.Try to give a defination of string center function with an example
# ans:-Python center() is a string class function that is used to position a string by padding it with a specified character.
#11.Write your own defination of compiler and interpretor without copy
#   paste from internet in your own language
# ans:-compiler is a computer program that transforms source code written in a programming language into another computer language
#      Interpreters reads the source code of the program, line by line, passes the source code, and interprets the instruction.
#12.Python is a interpreted or compiled language give a clear answer with your understanding
# ans:-Python is an interpreted language, which means the source code of a python program is converted into bytecode that is then executed by the python virtual machine
#13.Try to write a usecase of python with your understanding
# ans:-Data science implementation and artificial intelligence.
