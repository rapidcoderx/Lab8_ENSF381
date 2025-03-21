import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")
headings_count = sum(len(soup.find_all(f'h{i}')) for i in range(1, 7))
print(f"Number of headings: {headings_count}")

links_count = len(soup.find_all('a'))
print(f"Number of links: {links_count}")

paragraphs_count = len(soup.find_all('p'))
print(f"Number of paragraphs: {paragraphs_count}")
Keyword= input("Enter the keyword you want to search: ")
keyword_count = len(soup.find_all(string=Keyword))
print(f"Number of times the keyword {Keyword} appears: {keyword_count}")
text= soup.get_text()
split_text= text.split()
lowercase_split_text= [word.lower() for word in split_text]
thisdict={}
for word in lowercase_split_text:
    if word in thisdict:
        thisdict[word]+=1
    else:
        thisdict.update({word:1})
values = list(thisdict.values())
keys = list(thisdict.keys())
for i in range (0,5):
    max_value = max(values)
    index_value=values.index(max_value)
    key = keys[index_value]
    print(f'{i+1}.', key, max_value)
    keys.remove(key)
    values.remove(max_value)

paras = soup.find_all('p')
for para in paras:
    if len(para) < 6:
        paras.remove(para)
list_len=[len(para) for para in paras]
max_para=max(list_len)
index_para = list_len.index(max_para)
print(paras[index_para],"is the longest paragraph with",list_len[index_para], "words")
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings_count, links_count, paragraphs_count]
plt.bar(labels, values)
plt.title('19')
plt.ylabel('Count')
plt.show()
    
