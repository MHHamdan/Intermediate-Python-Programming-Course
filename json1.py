import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}


#convert to a json object

person_json = json.dumps(person)

print(person_json)

person_json = json.dumps(person, indent=4, sort_keys=True)

print(person_json)

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

#doding deserialize json


person = json.loads(person_json)
print(person)

with open('person.json', 'r') as f:
    pr = json.load(f)
    print(pr)



class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 23)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age':o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serelization')
userJSON = json.dumps(user, default=encode_user )
print(userJSON)


from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder )
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)


#decode custom object from


user = json.loads(userJSON)
print(type(user))

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)