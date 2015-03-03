#-----------------------------------------------------------------------------
# Name:        
# Purpose:     
#
# Author:      Sudheer
#
# Created:     02/08/2014
# Copyright:   (c) 2014 Sudheer <sudheerk@mit.edu>
# Licence:     MIT
#-----------------------------------------------------------------------------
#!/usr/bin/env python
import os
import re
import string
import sys
import codecs

def l2pconvert(l2pmaplines,textlines,outfile):
 #l2pmaplines = codecs.open('%s.map'%(lang),'r',encoding = 'utf-8').readlines()
 pat = []
 for l in l2pmaplines:
	fields = l.strip('\n').split('\t')
	p = re.compile("%s"%(fields[0]))
	pat.append((p,fields[1].strip()))	
 for t in textlines:
 	for x in pat:
		#fields = l.strip('\n').split('\t')
		#pat = re.compile("%s"%(fields[0]), re.IGNORECASE)
		if x[1] == 'Null': 
			t = re.sub(x[0],' ',t)
		else:
			t = re.sub(x[0],"%s"%(x[1]),t)
	#print t,
	outfile.write(t,)
 	
 return

def main():
 if len(sys.argv) != 4:
        print 'Usage:python fontconverter.py <mapfile> <filetoconvert> <outputfile>'
        sys.exit()
 
 #lang = sys.argv[1].lower()[0:3]
 maplines = codecs.open(sys.argv[1],'r',encoding = 'utf-8').readlines()
 texttoconvert = codecs.open(sys.argv[2],'r',encoding = 'utf-8').readlines()
 outfile = codecs.open(sys.argv[3],'w',encoding = 'utf-8')
 
 #l2pconvert(lang,texttoconvert,outfile)
 l2pconvert(maplines,texttoconvert,outfile)
 
 return 
  
if __name__ == '__main__':
    main()

