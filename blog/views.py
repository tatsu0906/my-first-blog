from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

from django.shortcuts import render_to_response
from django.template import RequestContext

#404 def
def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


# Main_Site

def render_MainSite_index(request):
    return render(request, 'blog/MainSite/index.html', {})

def render_MainSite_7(request):
    return render(request, 'blog/MainSite/7.html', {})

def render_MainSite_matrix(request):
    return render(request, 'blog/MainSite/matrix.html', {})

def render_MainSite_title(request):
    return render(request, 'blog/MainSite/title.html', {})

def render_MainSite_24(request):
    return render(request, 'blog/MainSite/24.html', {})

def render_MainSite_17(request):
    return render(request, 'blog/MainSite/17.html', {})    

def render_MainSite_coreterm(request):
    return render(request, 'blog/MainSite/coreterm.html', {})

def render_MainSite_suppleterm(request):
    return render(request, 'blog/MainSite/suppleterm.html', {})

def render_MainSite_board(request):
    return render(request, 'blog/MainSite/board.html', {})



def render_MainSite_2020(request):
    return render(request, 'blog/MainSite/2020matrix.html', {})


#########################################################

# SnG

def render_SnG_index(request):
    return render(request, 'blog/SnG/index.html', {})

def render_SnG_7(request):
    return render(request, 'blog/SnG/7.html', {})

def render_SnG_matrix(request):
    return render(request, 'blog/SnG/matrix.html', {})

def render_SnG_title(request):
    return render(request, 'blog/SnG/title.html', {})

def render_SnG_24(request):
    return render(request, 'blog/SnG/24.html', {})

def render_SnG_17(request):
    return render(request, 'blog/SnG/17.html', {})    

def render_SnG_coreterm(request):
    return render(request, 'blog/SnG/coreterm.html', {})    

def render_SnG_suppleterm(request):
    return render(request, 'blog/SnG/suppleterm.html', {})    

def render_SnG_board(request):
    return render(request, 'blog/SnG/board.html', {})    


#########################################################

# Yerim

def render_Yerim_index(request):
    return render(request, 'blog/Yerim/index.html', {})

def render_Yerim_7(request):
    return render(request, 'blog/Yerim/7.html', {})

def render_Yerim_matrix(request):
    return render(request, 'blog/Yerim/matrix.html', {})

def render_Yerim_title(request):
    return render(request, 'blog/Yerim/title.html', {})

def render_Yerim_24(request):
    return render(request, 'blog/Yerim/24.html', {})

def render_Yerim_17(request):
    return render(request, 'blog/Yerim/17.html', {})    

def render_Yerim_coreterm(request):
    return render(request, 'blog/Yerim/coreterm.html', {})    

def render_Yerim_suppleterm(request):
    return render(request, 'blog/Yerim/suppleterm.html', {})    

def render_Yerim_board(request):
    return render(request, 'blog/Yerim/board.html', {})    

#########################################################