def handle_uploaded_file(f):  
    print(f)

    with open('/media/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)