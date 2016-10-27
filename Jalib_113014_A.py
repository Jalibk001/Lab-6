import os
rootin={}
dirsin={}
filesin={}
directory="C:\\"
def crawl():
        for root,dirs,files in os.walk(directory):
            for file in files 
                mypath= os.path.join(root,file)
                if(os.path.splittext(file)[1]=='.txt'):
                   with open(mypath,r) as myfiletxt:
                       for l in myfiletxt:
                           for w in line.split():
                               if w not in filesin:
                                   filesin[w]=[]
                               if mypath not in filesin[w]:
                                   filesin[w].appent(mypath)
                           
                   
        wordList=os.path.splitext(file)[0]
		wordList=wordList.split(' ')
		    for word in wordList:
			    if word not in rootin:
				    root[word]=[]
				root[word].append(mypath)

		#stroing directiory 
		for subdir in dirs:
			wordList=subdir.split(' ')
			for word in wordList:
				if word not in dirIndex:
					dirsin[word]=[]
				dirsin[word].append(mypath)

input= 1				
while(input):
    word = raw_input("enter keyword")

    if word in rootin:
		temp=rootin[word]
		print("In readable files: ")
		for path in temp:
			print (path)
	if word in dirsin:
		temp=dirsin[word]
		print("In files names: ")
		for path in temp:
			print (path)
	if word in filesin:
		temp=filesin[word]
		print("In Directory names: ")
		for path in temp:
			print (path)
