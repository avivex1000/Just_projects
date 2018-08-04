import os
import re
import urllib
import urllib2
from bs4 import BeautifulSoup

#connect to a URL
website = urllib2.urlopen('http://proceedings.esri.com/library/userconf/proc17/tech-workshops.html')

#read html code
soup = BeautifulSoup(website.read(), "html.parser")

#use re.findall to get all the links
#links = re.findall('"((http|ftp)s?://.*?)"', html)

links = soup.findAll(href=re.compile("\.pdf$"))
lables = soup.findAll('td')
count = 1
for Z in lables:
    z = str(Z)
    T = z.split('\"')
    for F in T:    
        F = str(F)
        if F.find('pdf')!= -1:
            i = lables.index(Z)
            start = 'href="'
            end = '" target'
            X = re.search('%s(.*)%s' % (start, end), str(Z).group(1))
            X = 'http://proceedings.esri.com/library/userconf/proc17/' + X
            print X
            start = '>'
            end = '<'
            Y = re.search('%s(.*)%s' % (start, end), str(lables[i-1])).group(1)
            fullfilename = os.path.join(r'C:\Users\aviv\Downloads\ESRI_DOCS',str(Y)+'.pdf')
            urllib.urlretrieve(X, fullfilename)
            
            print " "
    count = count + 1
##start = 'href="'
##end = '" target'
##count = 0
##for X in links:
##    X = str(X)
##    X = re.search('%s(.*)%s' % (start, end), X).group(1)
##    X = 'http://proceedings.esri.com/library/userconf/proc17/' + X
##    print X
##    count = count + 1
##    fullfilename = os.path.join(r'C:\Users\aviv\Downloads\ESRI_DOCS',str(count)+'test.pdf')
##    
