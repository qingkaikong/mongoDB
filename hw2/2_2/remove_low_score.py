import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
users = db.grades


def find_and_remove():

    print "find, reporting for duty"

    query = {'type':'homework'}

    try:
        iter = users.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0 
    old_student_id = 0
    remove_id = []
    for doc in iter:
        #print doc['student_id'] 
        if (doc['student_id'] != old_student_id):
            remove_id.append(_id)
            #print doc['student_id']
        sanity += 1
        if (sanity > 1000):
            break
        old_student_id = doc['student_id']
        _id = doc['_id']
        
    #add the last _id of the document 
    remove_id.append(_id)
    
    users.remove({'_id':{'$in':remove_id}})
    
find_and_remove()