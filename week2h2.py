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
        print("خطأ بقراءة ملف البيانات", e)
        return{}
def save_movies(movies):
    try:
        with open(data_file,"w",encoding="utf-8")as f:
            json.dump({str(k):v for k,v in movies.items()},f,ensure_ascii=False,indent=2)
    except Exception as e:
        print("خطأ بقراءة البيانات",e)
def next_id(movies):
    """إرجاع ID جديد (أكبر رقم موجود + 1)"""
    if not movies:
        return 1
    return max(movies.keys()) + 1

def input_nonempty(prompt):
    """مساعدة: الحصول على إدخال غير فارغ"""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("لا يمكن ترك الحقل فارغًا.")

def add_movie(movies):
    print("enter a new film")
    title=input("اسم الفيلم")
    director=input("اسم المخرج")
    year=int(input("سنة الاصدار"))
    genre=input("نوع الفيلم")
    movie={
        "title":title,
        "director" :director,
        "year" :year,
        "genre":genre 
    }
    mid=next_id(movies)
    movies[mid]=movie
    print(f"تم اضافة الفيلم بالمعرف{mid}")
def print_movie(mid,movie):
       print(f"ID: {mid} | العنوان: {movie.get('title')}  | المخرج: {movie.get('director')} | سنة: {movie.get('year')} | النوع: {movie.get('genre')}")
def view_all(movies):
    """عرض كل الأفلام"""
    print("\n--- عرض كل الأفلام ---")
    if not movies:
        print("لا توجد أفلام حالياً.")
        return
    for mid in sorted(movies.keys()):
        print_movie(mid, movies[mid])
def find_movie_by_id(movies):
    """طلب ID والتحقق من وجوده، ثم إرجاعه أو None"""
    if not movies:
        print("لا توجد أفلام.")
        return None
    try:
        mid = int(input("أدخل الـ ID: ").strip())
    except ValueError:
        print("الـ ID يجب أن يكون رقماً.")
        return None
    if mid not in movies:
        print("لم يتم العثور على فيلم بهذا الـ ID.")
        return None
    return mid

def edit_movie(movies):
    """تعديل بيانات فيلم"""
    print("\n--- تعديل فيلم ---")
    mid = find_movie_by_id(movies)
    if mid is None:
        return
    movie = movies[mid]
    print("الفيلم الحالي:")
    print_movie(mid, movie)
    print("اترك الحقل فارغًا إذا لم ترغب بتغييره.")
    new_title = input("عنوان جديد: ").strip()
    new_director = input("مخرج جديد: ").strip()
    new_year = input("سنة إصدار جديدة: ").strip()
    new_genre = input("نوع جديد: ").strip()

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
        print("تم تعديل بيانات الفيلم.")
def delete_movie(movies):
    """حذف فيلم"""
    print("\n--- حذف فيلم ---")
    mid = find_movie_by_id(movies)
    if mid is None:
        return
    print("الفيلم الذي ستحذفه:")
    print_movie(mid, movies[mid])
    confirm = input("تأكيد الحذف؟ اكتب 'نعم' للحذف: ").strip().lower()
    if confirm == "نعم" or confirm == "y":
        del movies[mid]
        print("تم حذف الفيلم.")
    else:
        print("تم إلغاء الحذف.")
def filter_movies(movies):
    """فلترة الأفلام حسب معايير"""
    if not movies:
        print("لا توجد أفلام للفلترة.")
        return
    print("\n--- فلترة الأفلام ---")
    print("اختر معياراً للفلترة:")
    print("1. النوع (genre)")
    print("2. سنة الإصدار")
    print("3. المخرج")
    choice = input("اختيار (1-3): ").strip()
    if choice == "1":
        g = input("ادخل النوع: ").strip().lower()
        results = {mid: m for mid, m in movies.items() if str(m.get("genre","")).lower() == g}
    elif choice == "2":
        y = input("ادخل السنة (مثال: 2020): ").strip()
        # نقارن كسلاسل أو كأرقام
        def match_year(m):
            val = m.get("year")
            return str(val) == y
        results = {mid: m for mid, m in movies.items() if match_year(m)}
    elif choice == "3":
        d = input("ادخل اسم المخرج: ").strip().lower()
        results = {mid: m for mid, m in movies.items() if str(m.get("director","")).lower() == d}
    else:
        print("خيار غير صالح.")
        return

    if not results:
        print("لا توجد نتائج مطابقة للفلترة.")
        return
    print(f"\nنتائج الفلترة ({len(results)}):")
    for mid in sorted(results.keys()):
        print_movie(mid, results[mid])

def main():
    movies = load_data()
    print("مرحباً بك في نظام إدارة مكتبة الأفلام.")
    while True:
        print("\n--- القائمة الرئيسية ---")
        print("1. إضافة فيلم")
        print("2. تعديل فيلم")
        print("3. حذف فيلم")
        print("4. عرض كل الأفلام")
        print("5. فلترة الأفلام")
        print("6. حفظ الآن")
        print("7. خروج (وسيتم الحفظ تلقائياً)")
        choice = input("اختر خياراً (1-7): ").strip()
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
            print("تم حفظ البيانات.")
        elif choice == "7":
            save_movies()
            print("تم الحفظ. جاري الخروج...")
            break
        else:
            print("خيار غير معروف، حاول مرة أخرى.")

if __name__ == "__main___":
    main()


            
    