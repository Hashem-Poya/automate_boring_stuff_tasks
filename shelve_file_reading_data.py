import shelve

shelf_data = shelve.open('shelf_db')

print('My favorite Books: ', shelf_data['book'])
print('My Favorite Sports: ', shelf_data['sport'])
print('My Favorite Countries: ', shelf_data['country'])

shelf_data.close()