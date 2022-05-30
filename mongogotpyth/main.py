import pymongo
import dns
connectionstring = 'mongodb+srv://Dwarikadhish:vn12345678@cluster0.fhjd4.mongodb.net/test'


def indertdata(name, presentage, Rollno):
    studentdata = {
        "student_name": f"{name}",
        "Persentage": f"{presentage}%",
        'Rollno': Rollno
    }
    stu_id = collection.insert_one(studentdata).inserted_id
    print(stu_id)


def findata(Rollno):
    data = collection.find({'Rollno': Rollno})
    for objects in data:
        print(objects)
    dataall = collection.find_one({'Rollno': Rollno})
    for objected in dataall:
        print(objected)
def updatedata(Rollno):
    #Update value any one then we use $set
    collection.update_many({},{'$set':{'Rollno':45}})
    #Update incrase value any one then we use $inc
    # collection.update_many({},{'$inc': {'Rollno':45}})
    # data=collection.update_one({'Rollno':Rollno},{'$inc': {'Rollno':45}})
def deleteone():
    # collection.delete_one({'Rollno':45})
    collection.delete_many({'Rollno':45})
    collection.delete_one({})
if __name__ == '__main__':
    client = pymongo.MongoClient(connectionstring)
    db = client['Studentdata']
    collection = db['Student_collection']
    # TODO:Insert data
    # name = input('Enter syudent name')
    # presentage = float(input('Enter Student presentage'))
    # Rollno = int(input('Enter student Rollno'))
    # indertdata(name=name, presentage=presentage, Rollno=Rollno)
    # TODO:Find data
    # Rollno = int(input('Enter Student roll no'))
    # findata(Rollno=Rollno)
    #TODO:Update data
    # updatedata(Rollno=23)
    #TODO:Delete data
    deleteone()