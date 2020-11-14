from django.views.generic import TemplateView
from django.shortcuts import render

from bs4 import BeautifulSoup
import requests

class ConvalidationsView(TemplateView):

    template_name = "convalidations.html"

class SubjectsView(TemplateView):

    template_name = "subjects_and_assistantships.html"

def news_view(request):
    
    #OAI, Oficina de Asuntos Internacionales
    
    oai = { 'links' : [],
            'titles': [],
            'dates' : [],
    }

    results = requests.get("https://oai.usm.cl/noticias/")
    src = results.content
    soup = BeautifulSoup(src, features="html.parser")

    noticias = soup.find_all("a", class_= "c6")

    for noticia in noticias:
        oai['links'] += [ noticia["href"] ]
        oai['titles'] += [ noticia.figure.figcaption.h4.string ]
        oai['dates'] += [ noticia.figure.figcaption.span.string ]

    #INFO, departamento de informática

    info = { 'links' : [],
             'titles': [],
             'dates' : [],
    }

    results = requests.get("https://www.inf.utfsm.cl/noticias")
    src = results.content
    soup = BeautifulSoup(src, features="html.parser")
        
    noticias = soup.find_all("div", class_= "item column-1")

    for noticia in noticias:
        info['links'] += [ "https://www.inf.utfsm.cl" + noticia.find("h2").a["href"] ]
        info['titles'] += [ noticia.find("h2").a.string[7:] ]
        info['dates'] += [ noticia.find("time").string[15:] ]

    #USM, eventos usm

    usm = { 'links' : [],
            'titles': [],
            'dates' : [],
    }

    results = requests.get("https://eventos.usm.cl/eventos/?tem=3")
    src = results.content
    soup = BeautifulSoup(src, features="html.parser")
        
    noticias = soup.find_all("div", class_="evento")

    for noticia in noticias:
        usm['links'] += [ noticia.a["href"] ]
        usm['titles'] += [ noticia.a.h4.string ]
        usm['dates'] += [ noticia.a.span.string ]

    #######################

    rango = [0,1,2] 

    data = {'oai' : oai,
            'info': info,
            'usm' : usm,
    }
    return render(request,'news.html', data)
