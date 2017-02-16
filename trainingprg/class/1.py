import sys
inp=sys.argv
def text1(inp):
 fr=file(inp[1],'r')
#for line in fr:
 text=fr.readlines()
 print text
 for x in text:
    y=x.split(" ")
    print y[1]
    fr.close()
text1(inp)
