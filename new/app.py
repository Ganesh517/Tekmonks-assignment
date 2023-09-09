from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='8b57855bf1f248bf92cbf5571b4e7158')

@app.route('/')
def news():
   top_headlines = newsapi.get_top_headlines(sources='bbc-news')
   top_headlines = top_headlines['articles']
   desc = []
   news = []
   img = []
   link = []
   for i in range(len(top_headlines)):
      myarticles = top_headlines[i]
      news.append(myarticles['title'])
      desc.append(myarticles['description'])
      img.append(myarticles['urlToImage'])
      link.append(myarticles['url'])
        
   mylist = zip(news, desc, img, link)
   return render_template('news.html', context=mylist)

if __name__ == '__main__':
   app.run()