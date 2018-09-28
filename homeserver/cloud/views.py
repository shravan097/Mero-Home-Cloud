from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseNotFound
from django.core.urlresolvers import reverse
from .models import File,FileForm,PasswordForm
import os
import os.path
import sys
from fnmatch import fnmatch
from django.contrib import messages
import webbrowser
from urllib.request import pathname2url
import subprocess
import requests
import hashlib
import dropbox

# Create your views here.


def index(request):
    all_files = File.objects.all()
    recent_files = File.objects.all()[:5]
    # for file_id in all_files:
    #     filename = file_id.file_name()
    #     fpath = os.path.dirname(__file__)
    #     #print (fpath)
    #     homepath = os.path.join(fpath,'uploads')
    #     #print (homepath)
    #     for dirs in (os.listdir(homepath)):
    #         filepath = os.path.join((os.path.join(homepath,dirs)),filename)
    #         print (filepath)
    #         if (os.path.isfile(filepath)):
    #             print ("File Exists")
    #             return render(request,'cloud/index.html',{'all_files' : all_files, 'recent_files': recent_files})
    #         else:
    #             print ("File doesnt exist")
    #             file_id.delete()

    return render(request,'cloud/index.html',{'all_files' : all_files, 'recent_files': recent_files})



    # Hasing the Password Using SHA-256
    # Needs salt + other stuff
    # Update is require to follow NIST standards
def hash_password(password):
    if password is None:
        return None
    return hashlib.sha256((password).encode('utf-8')).hexdigest()

def upload(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        # Have we provided witha valid form
        if form.is_valid():
            # Don't Save yet ie.Commit = false
            file = form.save(commit=False)
            file.password = hash_password(file.password)
            form.save()

            # Now Call the index() view
            # The user will be show the homepage.
            messages.success(request, "File  successfully uploaded!")
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details
        form = FileForm()

    return render(request, 'cloud/upload.html', {'form': form})

# Download Authentication for Encrypted Files
def authenticate(request, id):
    download = File.objects.get(pk=id)
    # Checking the Download File for Encrypted Files.
    if request.method == 'POST':
        # Getting What the User has inputted.
        form = PasswordForm(request.POST)
        user_hash_pass=None
        if form.is_valid():
            user_pass = form.cleaned_data['client_password']
            user_hash_pass = hash_password(user_pass)
        print(user_hash_pass)
        print(download.get_pass())
        if (user_hash_pass == download.get_pass()):
            return download_file(request,id)
        else:
            return HttpResponseNotFound("Sorry! You have entered Wrong Password!")
    else:
        form = PasswordForm()
    return render(request, 'cloud/authenticate.html', {'form': form,'id':id})




#Download without authentication
def download_wo_authenticate(request,id):
    download = File.objects.get(pk=id)
    if(download.get_pass() is not None):
        return authenticate(request,id)
    return download_file(request,id)



def download_file(request,id):
    download = File.objects.get(pk=id)
    response = HttpResponse(content=download.file, content_type="application/force-download")
    response['Content-Disposition'] = str('attachment; filename = {0}').format(download.file_name())
    return response


def view_file(request):
    all_files = File.objects.all()
    return render(request,'cloud/view.html',{'all_files':all_files})


def delete_file(request,id):
    file_id = File.objects.get(pk=id)
    fname = file_id.file_name()
    print (fname)
    fpath = os.path.dirname(__file__)
    #print (fpath)
    homepath = os.path.join(fpath,'uploads')
    print (homepath)
    for dirs in (os.listdir(homepath)):
        #print (dirs)
        for file in (os.listdir(os.path.join(homepath,dirs))):
            #print (files)
            if file == fname:
                filepath = os.path.join((os.path.join(homepath,dirs)),fname)
                print (filepath)
                os.remove(filepath)
                # remove from db
                file_id.delete()

            # check if the folder is empty or not
            # if the folder is empty, delete the folder
            try:
                os.rmdir(os.path.join((os.path.join(homepath,dirs))))
            except OSError:
                continue


    messages.success(request, "File  successfully deleted!")
    return HttpResponseRedirect(reverse('index'))

# this will be used to render the file online for viewing 
# rather than having to download the file
def display_file(request,id):
    # to be done
    pass


#CALLS DROPBOX API FOR CHROMECAST CALL
def play_music(request,id):
    file = File.objects.get(pk=id)
    file_name=file.file_name()
    TOKEN = 'TOKEN GOES HERE'
    dbx = dropbox.Dropbox(TOKEN)
    dropbox_path = "/"
    file_path = os.getcwd()+"/"+(str(file.file))
    print(file_path)
    with open(file_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path + file_name, mute=True)
    meta_data = dbx.files_get_temporary_link(dropbox_path+file_name)
    download_link = meta_data.link
    return render(request,'cloud/play.html',{'file':file,'link':download_link})
