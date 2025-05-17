# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO AUTOLAB

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    with open(f, "r") as file:
        rate_dic = {}
        for line in file:
            temp_lst = line.strip().split("|")
            name = temp_lst[0]
            rate = float(temp_lst[1])
            if name in rate_dic:
                rate_dic[name].append(rate)
            else:
                rate_dic[name] = [rate]
        return rate_dic
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    with open(f, "r") as file:
        movie_dic = {}
        for line in file:
            temp_lst = line.strip().split("|")
            name = temp_lst[2]
            genre = temp_lst[0]
            movie_dic[name] = genre
        return movie_dic

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    mov_genre_dic = {}
    for key, value in d.items():
        if value in mov_genre_dic:
            mov_genre_dic[value].append(key)
        else:
            mov_genre_dic[value] = [key]
    return mov_genre_dic
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    rate_ave_dic = {}
    for key, value in d.items():
        average = sum(value) / len(value)
        rate_ave_dic[key] = average
    return rate_ave_dic
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    rate_rank = sorted(d.items(), key=lambda x: x[1], reverse=True)
    if n >= len(rate_rank):
        return dict(rate_rank)
    else:
        recom_dic = {}
        for i in range(n):
            key, value = rate_rank[i]
            recom_dic[key] = value
        return recom_dic
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filtered_dic = {}
    for key, value in d.items():
        if value >= thres_rating:
            filtered_dic[key] = value
    return filtered_dic
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    movie_lst = []
    gen_recom_mov = {}
    for key in genre_to_movies:
        if key == genre:
            movie_lst = genre_to_movies.get(key)
    for movie in movie_lst:
        if movie in movie_to_average_rating:
                gen_recom_mov[movie] = movie_to_average_rating.get(movie)
    gen_recom_sort = sorted(gen_recom_mov.items(), key=lambda x: x[1], reverse=True)
    return dict(gen_recom_sort[:n])
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    movie_lst = []
    rate_sum = 0
    for key in genre_to_movies:
        if key == genre:
            movie_lst = genre_to_movies.get(key)
    if len(movie_lst) == 0:
        return None    
    for movie in movie_lst:
        rate_sum += movie_to_average_rating.get(movie, 0)

    return float(rate_sum / len(movie_lst))
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    genre_rate_ave = {}
    for key in genre_to_movies:
        genre_rate_ave[key] = get_genre_rating(key, genre_to_movies, movie_to_average_rating)
    genre_rate_ave_sort = dict(sorted(genre_rate_ave.items(), key=lambda x: x[1], reverse=True))
    return dict(list(genre_rate_ave_sort.items())[:n])

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    with open(f, "r") as file:
        id_rate_dic = {}
        for line in file:
            temp_lst = line.strip().split("|")
            name = temp_lst[0]
            rate = float(temp_lst[1])
            id = temp_lst[2]
            new_item = (name, rate)
            if id in id_rate_dic:
                id_rate_dic[id].append(new_item)
            else:
                id_rate_dic[id] = [new_item]
        return id_rate_dic
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    rate_lst = user_to_movies[user_id]
    genre_rate_dic = {}
    for key, value in rate_lst:
        movie_genre = movie_to_genre[key]
        if movie_genre:
            if movie_genre not in genre_rate_dic:
                genre_rate_dic[movie_genre] = [value]
            else:
                genre_rate_dic[movie_genre].append(value)            
    for key, value in genre_rate_dic.items():
        genre_rate_dic[key] = sum(value) / len(value)
    sorted_rate = sorted(genre_rate_dic.items(), key=lambda x: x[1], reverse=True)
    return sorted_rate[0][0]
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    favor_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    all_genre_movie = []
    recommend_dic = {}
    watched_lst = user_to_movies[user_id]
    watched_movie = []
    unwatched_moive = {}
    for i in range(len(watched_lst)):
        watched_movie.append(watched_lst[i][0])
    for key, value in movie_to_genre.items():
        if value == favor_genre:
            all_genre_movie.append(key)
    for name in all_genre_movie:
        if name not in watched_movie:
            unwatched_moive[name] = movie_to_average_rating[name]
    recom_sort = sorted(unwatched_moive.items(), key=lambda x: x[1], reverse=True)
    return dict(recom_sort[:3])

# -------- main function for your testing -----
def main():
    pass
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()