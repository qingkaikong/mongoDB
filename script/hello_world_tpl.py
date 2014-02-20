import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple', 'orange', 'banana', 'peach']
    return bottle.template('hello_world', username='Qingkai', things=mythings)
#    return bottle.template('hello_world',{'username':"Fan", 'things':mythings})
 
    
bottle.debug(True)
bottle.run(host='localhost', port=8080)