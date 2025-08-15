# #Question 2: Film Library Management System Project
# Project Description: This project aims to create an application that w
# ill help the user manage their movie collection. 
# Users can add, edit, delete movies and view their collection.//مشروع نظام ادارة مكتبة الافلام

# Data Structures Used: Dictionaries (to store movies and related information), lists (to display movie collection)

# Basic Functions:

# 1-Create a movie data by taking information such as movie name, director, release year and genre from the 
# user and store it in a dictionary.

# 2-Give the user the option to edit or delete a movie. (For this, a suitable function must be written for
# whatever data they want to change about the movie.)

# 3-Allow the user to view their collection. List all movies or filter by criteria such as genre or year of release.

# 4-Save the movie data in a file and restore this data when you start the program.
import json
import os
data_file="movie.json"
def load_data():
    if not os.path.exists(data_file):
        return{}
    try:
        with open(data_file,"r",encoding="utf-8")as f:
            data=json.load(f)
        return{int(k):v for k,v in data.items()}
    except Exception as e:
        print("ERROR  READING", e)
        return{}
def save_movies(movies):
    try:
        with open(data_file,"w",encoding="utf-8")as f:
            json.dump({str(k):v for k,v in movies.items()},f,ensure_ascii=False,indent=2)
    except Exception as e:
        print("error",e)
def next_id(movies):
    """return ID new (bigger number + 1)"""
    if not movies:
        return 1
    return max(movies.keys()) + 1

def input_nonempty(prompt):
    """input not empty"""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("the field must not be empty")

def add_movie(movies):
    print("enter a new film")
    title=input(" film's name")
    director=input("director's name")
    year=int(input("year's appear "))
    genre=input("film's genre ")
    movie={
        "title":title,
        "director" :director,
        "year" :year,
        "genre":genre 
    }
    mid=next_id(movies)
    movies[mid]=movie
    print(f"film is added with id{mid}")
def print_movie(mid,movie):
    print(f"ID: {mid} | title: {movie.get('title')}  | director: {movie.get('director')} | year: {movie.get('year')} | genre: {movie.get('genre')}")
def view_all(movies):
    """view all films  """
    print("\n--- view all films   ---")
    if not movies:
        print("there are not films actually   .")
        return
    for mid in sorted(movies.keys()):
        print_movie(mid, movies[mid])
def find_movie_by_id(movies):
    """id request and check it back"""
    if not movies:
        print("there are no films")
        return None
    try:
        mid = int(input(" enter ID: ").strip())
    except ValueError:
        print(" ID must be number ")
        return None
    if mid not in movies:
        print("there is not founf film with this ID.")
        return None
    return mid

def edit_movie(movies):
    """تعديل بيانات فيلم"""
    print("\n---  film edit ---")
    mid = find_movie_by_id(movies)
    if mid is None:
        return
    movie = movies[mid]
    print("current film :")
    print_movie(mid, movie)
    print("break the field empty if you don't want to change it.")
    new_title = input("new title : ").strip()
    new_director = input("new director : ").strip()
    new_year = input("new direction year ").strip()
    new_genre = input("new genre : ").strip()

    if new_title:
        movie["title"] = new_title
    if new_director:
        movie["director"] = new_director
    if new_year:
        try:
            movie["year"] = int(new_year)
        except ValueError:
            movie["year"] = new_year
    if new_genre:
        movie["genre"] = new_genre
        movies[mid] = movie
        print("film is edited.")
def delete_movie(movies):
    """حذف فيلم"""
    print("\n--- film deletion  ---")
    mid = find_movie_by_id(movies)
    if mid is None:
        return
    print(" the film that delete :")
    print_movie(mid, movies[mid])
    confirm = input("write yes to delete ").strip().lower()
    if confirm == "yes" or confirm == "y":
        del movies[mid]
        print("film is deleted.")
    else:
        print("deletion canceled  .")
def filter_movies(movies):
    """فلترة الأفلام حسب معايير"""
    if not movies:
        print("there are not films to filter.")
        return
    print("\n--- filtering film  ---")
    print("  choice film to filter:")
    print("1.  (genre)")
    print("2. year apperation ")
    print("3. director")
    choice = input("choice (1-3): ").strip()
    if choice == "1":
        g = input(" enter genre: ").strip().lower()
        results = {mid: m for mid, m in movies.items() if str(m.get("genre","")).lower() == g}
    elif choice == "2":
        y = input(" enter year (مثال: 2020): ").strip()
        # نقارن كسلاسل أو كأرقام
        def match_year(m):
            val = m.get("year")
            return str(val) == y
        results = {mid: m for mid, m in movies.items() if match_year(m)}
    elif choice == "3":
        d = input("enter name director ").strip().lower()
        results = {mid: m for mid, m in movies.items() if str(m.get("director","")).lower() == d}
    else:
        print(" choice is not correct .")
        return

    if not results:
        print("no result to filtering.")
        return
    print(f"\results filtering  ({len(results)}):")
    for mid in sorted(results.keys()):
        print_movie(mid, results[mid])

def main():
    movies = load_data()
    print("welcome in library films")
    while True:
        print("\n--- main list  ---")
        print("1.  film addition")
        print("2.  film edition")
        print("3.  film deletion")
        print("4. view all films  ")
        print("5. film filtering ")
        print("6. save now ")
        print("7. exit")
        choice = input(" select choice (1-7): ").strip()
        if choice == "1":
            add_movie(movies)
        elif choice == "2":
            edit_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            view_all(movies)
        elif choice == "5":
            filter_movies(movies)
        elif choice == "6":
            save_movies()
            print(" data saving .")
        elif choice == "7":
            save_movies()
            print("saved...")
            break
        else:
            print(" choice is not knoen.")
main()









            
    