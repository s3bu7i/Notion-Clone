import sqlite3

secim = input("Film, Book or Note ? (f/b/n): ")

if secim == 'f':
    db_name = 'film.db'
    table_name = 'Film List'
elif secim == 'b':
    db_name = 'book.db'
    table_name = 'Book List'
elif secim == 'n':
    db_name = 'note.db'
    table_name = 'Note List'
else:
    print("This choosen is wrong, please try again :D")
    exit()

conn = sqlite3.connect(db_name)

if db_name == 'film.db':
    conn.execute('''CREATE TABLE IF NOT EXISTS film
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,
                    IMDB FLOAT);''')
    film_name = input("Film's name: ")
    film_IMDB = input("Your IMDB rating for the movie(-/10): ")
    conn.execute("INSERT INTO film (NAME, IMDB) VALUES (?, ?)", (film_name, film_IMDB))
elif db_name == 'book.db':
    conn.execute('''CREATE TABLE IF NOT EXISTS book
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME TEXT,
                 AUTHOR TEXT,
                 RATING FLOAT);''')
    book_name = input("Book's name: ")
    book_writer = input("The author of the book: ")
    book_rating = input("Your rating for the book(-/10): ")
    conn.execute("INSERT INTO book (NAME, AUTHOR, RATING) VALUES(?, ?, ?)", (book_name, book_writer, book_rating))

elif db_name == 'note.db':
    conn.execute('''CREATE TABLE IF NOT EXISTS note
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 TITLE TEXT,
                 NOTE TEXT,
                 DATE TEXT);''')
    note_title = input("The title of note: ")
    note_note = input("Write note: ")
    note_date = input("Date: ")
    conn.execute("INSERT INTO note(TITLE, NOTE, DATE) VALUES(?, ?, ?)", (note_title, note_note, note_date))


conn.commit()
conn.close()

