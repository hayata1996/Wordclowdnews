import requests 
from bs4 import BeautifulSoup 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import datetime



url = 'https://www.bbc.com/news'
#url = 'https://news.google.com/home?hl=en-US&gl=US&ceid=US:en'
response = requests.get(url) 
text = []
  
soup = BeautifulSoup(response.text, 'html.parser') 
headlines = soup.find('body').find_all('h3') 
for x in headlines: 
#    print(x.text.strip()) 
    text.append(x.text.strip())

text2 =' '.join(text)
print(text2)

#    print(x)

wc = WordCloud(width=1600, height=800)
img = wc.generate(text2)
plt.figure(figsize=(20,10))
plt.title(datetime.date.today())
plt.axis('off')
plt.imshow(img)
plt.show()

