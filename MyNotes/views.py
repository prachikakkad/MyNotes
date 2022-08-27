from django.shortcuts import render
import os
import mimetypes
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper

def Home(request):
    return render(request, "Home.html")

def C(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'My C Notes.pdf'
    filepath = base_dir + '/Templates/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile , 'rb') , chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment ; filename = %s" % filename
    return response

def HTML(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'My HTML Notes.pdf'
    filepath = base_dir + '/Templates/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile , 'rb') , chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment ; filename = %s" % filename
    return response
