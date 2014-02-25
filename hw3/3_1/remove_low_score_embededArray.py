import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school
users = db.students


def find_and_remove():

    print "find, reporting for duty"

    query = {"scores.type":"homework"}
    projection = {'scores':1, '_id':0}

    try:
        #iter = users.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])
        iter = users.find(query)
        
    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0 
    remove_item = {}
    update_score = []
    for doc in iter:
        minmum_score = 100.0
        for item in range(len(doc['scores'])): 
            if doc['scores'][item]['type'] == 'homework':
                if doc['scores'][item]['score'] < minmum_score:
                    minmum_score = doc['scores'][item]['score']
                    #print minmum_score
                    remove_item = doc['scores'][item]
        #remove the lowest score from the array
        update_score = [d for d in doc['scores'] if d.get('score') != minmum_score]
        
        #update the score array
        users.update({'_id':doc['_id']},{'$set':{"scores" : update_score}}) 

    
find_and_remove()