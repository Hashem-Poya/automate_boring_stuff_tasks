import shelve

shelfFile = shelve.open('shelf_db')

my_favorite_books = [
    '1984',
    'The paying guests',
    'A tale of two cities',
    'Jane Eyre',
    'A town like alice',
    'Watership down'
]



my_favorites_sports = [
    'Football',
    'Runing',
    'Walking',
]

my_favorite_countries = [
    'US',
    'Turkey',
    'Sweden'
]

shelfFile['book'] = my_favorite_books
shelfFile['sport'] = my_favorites_sports
shelfFile['country'] = my_favorite_countries


shelfFile.close()