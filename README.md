# Tekmonks-assignment{% block content %}
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

#index.html
```python


```
