from django.shortcuts import render
import requests

# Create your views here.
def newsapp(request):
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=020108075f8f4c129f42a278841884e0')
    res = r.json()
    data = res['articles']
    author = []
    title = []
    description = []
    url = []
    content = []
    for x in data:
        author.append(x['author'])
        title.append(x['title'])
        description.append(x['description'])
        url.append(x['url'])
        content.append(x['content'])
    news = zip(author,title,description,url,content)
    return render(request,'index.html',{'news':news})