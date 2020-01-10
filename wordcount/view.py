from django.http import HttpResponse
from django.shortcuts import render
import operator
def myfun(request):
    return render(request,'home.html')

def counts(request):
    texts = request.GET['inputenter']
    splits = texts.split()
    dist = {}
    for i in splits:
        if i in dist:
            dist[i] += 1
        else:
            dist[i]=1
    sorts = sorted(dist.items(),key=operator.itemgetter(1),reverse=False)
    print(operator.itemgetter(1))
    return render(request,'counts.html',{'texts':texts,'length':len(texts),'dists':sorts})

def abouts(request):
    return render(request,'about.html')
