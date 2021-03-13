from django.shortcuts import render
from django import forms
from . import util
import markdown
import random
from .forms import searchForm, newPageForm
from django.contrib import messages
from django.contrib.messages import get_messages

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchForm" : searchForm()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if not entry == None:
        html = markdown.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title, "content": html,
            "searchForm" : searchForm()
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "searchForm" : searchForm()
        })

def search(request):
    if request.method == "POST":
        form = searchForm(request.POST)
        entries = util.list_entries()

        if form.is_valid():
            query = form.cleaned_data.get("form")

            if query in entries:
                entry = util.get_entry(query)
                html = markdown.markdown(entry)
                return render(request, "encyclopedia/entry.html", {
                    "title": query, "content": html,
                    "searchForm" : searchForm()
                })
            else:
                newEntryList = []
                
                for entry in entries:
                    if query.lower() in entry.lower():
                        newEntryList.append(entry)
                
                if newEntryList:
                    return render(request, "encyclopedia/search_results.html", {
                        "query" : query,
                        "entries" : newEntryList,
                        "searchForm" : searchForm()
                    })
                else:
                    return render(request, "encyclopedia/error.html", {
                        "searchForm" : searchForm()
                    })

def randomPage(request):
    entries = util.list_entries()
    entry = entries[random.randint(0, len(entries) - 1)]
    html = markdown.markdown(util.get_entry(entry))
    
    return render(request, "encyclopedia/entry.html", {
        "title": entry, "content": html,
        "searchForm" : searchForm()
    })

def newPage(request):
    return render(request, "encyclopedia/newPage.html", {
        "searchForm" : searchForm(),
        "newPageForm" : newPageForm()
    })

def createNewPage(request):
   if request.method == "POST": 
        form = newPageForm(request.POST)
        entries = util.list_entries()

        if form.is_valid():
            title = form.data['title']
            text = form.data['text']

            if title in entries:
                messages.add_message(request, messages.ERROR, 'This entry name already exist. Pick another one.')
                return render(request, "encyclopedia/newPage.html", {
                    "messages" : get_messages(request),
                    "searchForm" : searchForm(),
                    "newPageForm" : newPageForm()
                })

            else:
                util.save_entry(title, text)
                return render(request, "encyclopedia/entry.html", {
                    "title": title, 
                    "content": markdown.markdown(text),
                    "searchForm" : searchForm()
                })

def edit(request):
    title = request.POST.get("edit")
    content = util.get_entry(title)

    return render(request, "encyclopedia/editPage.html", {
        "searchForm" : searchForm(),
        "newPageForm" : newPageForm(initial={'title': title, 'text':content})
    })

def save(request):
    form = newPageForm(request.POST)

    if form.is_valid():
        title = form.data['title']
        text = form.data['text']
        util.save_entry(title, text)
        return render(request, "encyclopedia/entry.html", {
            "title": title, 
            "content": markdown.markdown(text),
            "searchForm" : searchForm()
        })
            

    