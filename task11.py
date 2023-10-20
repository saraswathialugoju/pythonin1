def countUniqueWords(filename):
    wordCount = {}
    
    try:
        file = open(filename, 'r')
        text = file.read()
        words = text.split()
        
        for word in words:
            
            word = word.strip('.,!?()[]{}":;')
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
                
        file.close()
        return wordCount
    except FileNotFoundError:
        return "file not found please try another file"
uniqueword=0
fname=input("enter a file name:")
result = countUniqueWords(fname)
if isinstance(result, dict):
    for word, count in result.items():
        print(f"{word}: {count}")
        if count==1:
            uniqueword=uniqueword+1
else:
    print(result)
print("uniquewords:",uniqueword)