import re 
import string 

engam = {} #eng-am dictionary
am = [] #list of amharic words
eng = [] #list of english words
i =0  #counter
for word in amharic:
    if word.startswith('1'):  #if a word start with a number remove the punctuation and the number. 
     
        word  = word.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
        words = re.split(r'\d',word) 
        if len(words)>1:
            eng.append(data['English'].loc[i]) # add the corresponding english word to the list
            am.append(words[1].strip().replace(" ","_")) # add the modified amharic word to the list by replacing space in multiwords with "_" 
    else:
        if len(word)>1:
            eng.append(data['English'].loc[i]) # add the corresponding english word to the list
            am.append(word.strip().replace(" ","_")) #Replace space in multiwords with "_" and add it to amharic list
    i=i+1
    
engam['English'] = eng # add english list of words to the dictionary    
engam['Amharic'] = am #add amharic list of words to the dictionary

df = pd.DataFrame(engam) #create pandas from the dictionary
df.to_csv('amen.csv') #create csv file


