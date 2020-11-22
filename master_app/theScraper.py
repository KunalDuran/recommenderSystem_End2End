from bs4 import BeautifulSoup
import requests
import json



def get_book_list():
        
    r = requests.get('https://www.goodreads.com/list/show/9440.100_Best_Books_of_All_Time_The_World_Library_List').text
    # r = requests.get('https://www.goodreads.com/book/show/7144.Crime_and_Punishment').text


    soup = BeautifulSoup(r, 'lxml')

    book_tags = soup.findAll('a', {'class': 'bookTitle'})




    book_titles = [book.text for book in book_tags]


    # print(soup.find_all('a', {'class': 'actionLinkLite bookPageGenreLink'}))
    # ass = soup.find_all('a', {'class': 'actionLinkLite bookPageGenreLink'})[0]
    # print(book_titles)
    BOOK_LIST_FILE = 'all_books.txt'

    with open(BOOK_LIST_FILE, 'w') as f:
        for book in book_tags:
            book = book['href'].replace('/book/show/', '')
            f.write(book+'\n')




def extract_book_data(BOOK_LIST_FILE='all_books.txt'):
    '''
    Info that we need:
    1. Book Title
    2. Ratings
    3. Author
    4. Genre
    '''
    with open(BOOK_LIST_FILE, 'r') as f:
        books = f.readlines() # names stored in a list
        print(len(books), books[0])


    complete_data = []
    BASE_URL = 'https://www.goodreads.com/book/show/'
    for count, book in enumerate(books):
        r = requests.get(BASE_URL+book).text

        soup = BeautifulSoup(r, 'lxml')
        print(f'Extracting data for Book {count+1}')
        data = {'author': soup.find('a', class_='authorName').span.text,
                  'book_title': soup.find('h1', {'id': 'bookTitle'}).text,
                  'ratings': soup.find('span', {'itemprop': 'ratingValue'}).text,
                  'genre': soup.find('a', class_="actionLinkLite bookPageGenreLink" ).text}
        print(data)
        complete_data.append(data)
    return complete_data    

data = extract_book_data()
# print(json.dumps(data))
# # print(data)
with open('final_data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data))