from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def books(request, name=''):
    if name == 'stiven_king_mers':
        return render (request, "about_books/stiven_king_mers.html" )
    if name == '11_22_63':
        return render (request, "about_books/stiven_king_11_22_63.html")
    if name == 'gluhovski_metro_2033':
        return render (request, "about_books/gluhovski_metro_2033.html")
    if name == 'gluhovski_metro_2034':
        return render (request,"about_books/gluhovski_metro_2034.html")
    if name == 'gluhovski_metro_2035':
        return render (request , "about_books/gluhovski_metro_2035.html")
    
    return render(request, 'books.html')

def contact(request):
    return render(request, 'contact.html')

def writers(request, name='', book_name=''):
    if name == 'shakespeare':
        return render(request, "about_writer/shakespeare.html")
    if name == 'hemingway':
        if book_name == 'gluhovski_metro_2033':
            return redirect('book_app:books', name='gluhovski_metro_2033')
        
        if book_name == 'gluhovski_metro_2034':
            return redirect('book_app:books', name='gluhovski_metro_2034')
        
        if book_name == 'gluhovski_metro_2035':
            return redirect('book_app:books', name='gluhovski_metro_2035')
        
        return render(request, "about_writer/hemingway.html")
    
    return render (request, 'writers.html')