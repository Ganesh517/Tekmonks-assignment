# Tekmonks-assignment
# index.html
```html
{% block content %}
<div style="display: flex;
justify-self: center;
align-items: center;
border: 2px rgb(15, 3, 3);
height: 50px;">

   <h1 style="color: red;">TIMES</h1>
</div>
<h1 style="display: block;">LATEST STORIES</h1>
{% for title, description, image, url in context %}
<div style="display: inline;">
<div class="article">
   <h2>{{ title }}</h2>
   {% if image %}
   <img src="{{ image }}" alt="{{ title }}" width="100" height="100">
   {% endif %}
   <p>{{ description }}</p>
   <a href="{{ url }}">{{ url }}</a>

</div>

</div>
{% endfor %}
{% endblock %}
```

# app.py
```python
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

```

# OUTPUT
![Screenshot 2023-09-09 133906](https://github.com/Ganesh517/Tekmonks-assignment/assets/75235006/109ab113-c175-4b70-9b16-999cfa145212)

