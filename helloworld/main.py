def helloworld(request):
    request_args = request.args
    request_json = request.get_json(silent=True)
    
            #Pasar parametros directamente en la URL
    if request_args and 'name' in request.args and 'lastname' in  request_args:
            name = request_args['name']
            lastname = request_args['lastname']
            
            # Pasar parámetros por un json
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']        
        
            # Parametros por defecto
    else:
            name = 'World'
            lastname = ''
    return(f'Hello {name} {lastname}!')