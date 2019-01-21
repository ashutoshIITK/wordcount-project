from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
import operator

def homepage(request):
    return render (request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    count_of_words = Counter(word_list)
    worddictionary = {}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)


    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(word_list), 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')
