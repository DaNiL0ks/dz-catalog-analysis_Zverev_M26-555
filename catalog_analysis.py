import math

movies = [
    {
        "title": "The Dune Chronicles", 
        "year": 2021, "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

#---------- № 1

def average_rating(movies):
    total_rating = sum(movie["rating"] for movie in movies)
    return round(total_rating / len(movies), 1) if movies else 0  


def catalog_age_stats(movies, current_year=2026):
    ages = []

    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)

    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))

    return oldest, newest, average_age

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return f"{hours}ч {remaining_minutes}м"

#---------- № 2

def rating_tier(rating):
    if rating >= 9: 
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые" 
        case _ if year >= 2015:
            return "недавние"
        case _ if year < 2015:
            return "старые"

#---------- № 3

def print_non_comedy(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def find_first_masterpiece(movies):
    n = 0
    while n < len(movies):
        if movies[n]["rating"] > 9:
            print(movies[n]['title'])
            break
        n += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

#---------- № 4

def normalize_title(title):
    words = title.split()
    normalized_words = [word[0].upper() + word[1:] for word in words]
    return " ".join(normalized_words)

def make_slug(title):
    title = normalize_title(title)
    title = title.lower()
    title = title.replace(" ", "-")
    return title

def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'

#---------- № 5

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)[:n]
    title_rating_pairs = [(movie["title"], movie["rating"]) for movie in sorted_movies]
    return title_rating_pairs

#---------- № 6

def count_by_genre(movies):
    genre_count = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography

def ratings_above_average(movies):
    average = average_rating(movies)
    title_rating = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }
    return title_rating

#---------- № 7

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

#---------- № 7



if __name__ == "__main__":
    print("Средний рейтинг:", average_rating(movies))
    print("Возраст фильмов:", catalog_age_stats(movies))
    print("Продолжительность:", duration_in_hours(155))

    print(rating_tier(4.9))  # слабо
    print(rating_tier(5.0))  # средне
    print(rating_tier(7.0))  # хорошо
    print(rating_tier(8.95)) # хорошо
    print(rating_tier(9.0))  # шедевр

    print(decade_label(2014))  # старые
    print(decade_label(2015))  # недавние
    print(decade_label(2020))  # недавние
    print(decade_label(2021))  # новые

    print_non_comedy(movies)
    find_first_masterpiece(movies)
    find_first_masterpiece(movies[:7])
    find_first_masterpiece([])
    print(count_long_movies(movies))       # 4
    print(count_long_movies(movies, 155))  # 0
    print(count_long_movies([])) 

    print(normalize_title("good morning"))
    print(make_slug("Good Morning"))
    print(format_report_line(movies[0]))
    print(normalize_title("  silent   hours  "))  # Silent Hours
    print(normalize_title(""))                   # пустая строка
    print(make_slug("midnight in oslo"))         # midnight-in-oslo
    print(format_report_line(movies[7]))

    print(titles_sorted_by_rating(movies))
    print(top_n_by_rating(movies))
    print(top_n_by_rating(movies, 0))   # []
    print(top_n_by_rating([]))         # []

    print(count_by_genre(movies))
    print(actor_filmography(movies))
    print(actor_filmography(movies)["A. Novak"])

    print(ratings_above_average(movies))

    print(all_genres(movies))                       # 6 уникальных жанров
    print(common_actors(movies[0], movies[3]))       # {'O. Isaac'}
    print(genres_only_in_one(movies[5:6], movies[:5]))  # {'mystery'}
    print(all_genres([]))                           # set()
    print(genres_only_in_one(movies, movies))       # set()

    
