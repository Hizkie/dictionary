import re 
import string 

engam = {}
am = []
eng = []
i =0
for word in amharic:
    x  = word

    if word.startswith('1'):
     
        word  = word.translate(str.maketrans('', '', string.punctuation))
        words = re.split(r'\d',word)
        if len(words)>1:
            eng.append(data['English'].loc[i])
            am.append(words[1].strip().replace(" ","_"))
    else:
        if len(word)>1:
            eng.append(data['English'].loc[i])
            am.append(word.strip().replace(" ","_"))
    i=i+1
    
engam['English'] = eng
engam['Amharic'] = am

df = pd.DataFrame(engam)
df.to_csv('amen.csv')
