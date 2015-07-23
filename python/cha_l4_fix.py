import urllib.request as req
import re, time

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing_rep = "and the next nothing is (\d+)"
nothing = "12345" # You'll later be asked to change this
                  # to "46059" and re-run the script.
# print (uri % nothing)


# with req.urlopen(uri % nothing) as f:
# 	res = f.read()
# 	print (res)

while True:
    try:
    	with req.urlopen(uri % nothing) as res:
    		source = res.read()
    		nothing = re.search(nothing_rep, source).group(1)
    except:
    	break

    print (nothing)
