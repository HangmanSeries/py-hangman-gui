import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client ()


# data = {
#     u'name': u'Los Angeles',
#     u'state': u'CA',
#     u'country': u'USA'
# }

# Add a new doc in collection 'cities' with ID 'LA'
#db.collection(u'cities').document(u'LA').set(data)

# city_ref = db.collection(u'cities').document(u'BJ')

# city_ref.set({
#     u'capital': 'Rhandy'
# }, merge = True)

# data = {
#     u'stringExample': u'Hello, World!',
#     u'booleanExample': True,
#     u'numberExample': 3.14159265,
#     u'dateExample': datetime.datetime.now(tz=datetime.timezone.utc),
#     u'arrayExample': [5, True, u'hello'],
#     u'nullExample': None,
#     u'objectExample': {
#         u'a': 5,
#         u'b': True
#     }
# }

# db.collection(u'data').document(u'one').set(data)

# class City(object):
#     def __init__(self, name, state, country, capital=False, population=0,
#                  regions=[]):
#         self.name = name
#         self.state = state
#         self.country = country
#         self.capital = capital
#         self.population = population
#         self.regions = regions

#     @staticmethod
#     def from_dict(source):
#         pass

#     def to_dict(self):
#         s = self.__dict__
#         return s

#     def __repr__(self):
#         return(
#             f'City(\
#                 name={self.name}, \
#                 country={self.country}, \
#                 population={self.population}, \
#                 capital={self.capital}, \
#                 regions={self.regions}\
#             )'
#         )

# city = City(name=u'Manila', state=u'NCR', country=u'Philippines')
# db.collection(u'cities').document(u'MMMMMM').set(city.to_dict())

# transaction = db.transaction()
# city_ref = db.collection(u'cities').document(u'LA')

# @firestore.transactional
# def update_in_transaction(transaction, city_ref):
#     snapshot = city_ref.get(transaction=transaction)
#     transaction.update(city_ref, {
#         u'population': snapshot.get(u'population') + 1
#     })

# update_in_transaction(transaction, city_ref)

# transaction = db.transaction()
# city_ref = db.collection(u'cities').document(u'MM')

# @firestore.transactional
# def update_in_transaction(transaction, city_ref):
#     snapshot = city_ref.get(transaction=transaction)
#     new_population = snapshot.get(u'population') + 1

#     if new_population < 3:
#         transaction.update(city_ref, {
#             u'population': new_population
#         })
#         return True
#     else:
#         return False

# result = update_in_transaction(transaction, city_ref)
# if result:
#     print(u'Population updated')
# else:
#     print(u'Sorry! Population is too big.')

batch = db.batch()

# Set the data for NYC
nyc_ref = db.collection(u'cities').document(u'NYC')
batch.set(nyc_ref, {u'name': u'New York City'})

# Update the population for SF
sf_ref = db.collection(u'cities').document(u'LA')
batch.update(sf_ref, {u'population': 1000000})

# Delete DEN
den_ref = db.collection(u'cities').document(u'DEN')
batch.delete(den_ref)

# Commit the batch
batch.commit()