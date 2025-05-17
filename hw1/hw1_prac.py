# Task 1: Reading Data
def read_ratings_data(f):
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

def read_movie_genre(f):
    with open(f, "r") as file:
        movie_dic = {}
        for line in file:
            temp_lst = line.strip().split("|")
            name = temp_lst[2]
            genre = temp_lst[0]
            movie_dic[name] = genre
        return movie_dic
            
# Task 2: Processing Data
def create_genre_dict(movie_dic):
    mov_genre_dic = {}
    for key, value in movie_dic.items():
        if value in mov_genre_dic:
            mov_genre_dic[value].append(key)
        else:
            mov_genre_dic[value] = [key]
    return mov_genre_dic

def calculate_average_rating(rate_dic):
    rate_ave_dic = {}
    for key, value in rate_dic.items():
        average = sum(value) / len(value)
        rate_ave_dic[key] = average
    return rate_ave_dic

# Task 3: Recommendation
def get_popular_movies(rate_ave_dic, n):
    rate_rank = sorted(rate_ave_dic.items(), key=lambda x: x[1], reverse=True)
    if n >= len(rate_rank):
        return dict(rate_rank)
    else:
        recom_dic = {}
        for i in range(n):
            key, value = rate_rank[i]
            recom_dic[key] = value
        return recom_dic

def filter_movies(rate_ave_dic, threshold):
    filtered_dic = {}
    for key, value in rate_ave_dic.items():
        if value >= threshold:
            filtered_dic[key] = value
    return filtered_dic

def get_popular_in_genre(genre, mov_genre_dic, rate_ave_dic, n):
    movie_lst = []
    gen_recom_mov = {}
    for key in mov_genre_dic:
        if key == genre:
            movie_lst = mov_genre_dic.get(key)
    for movie in movie_lst:
        if movie in rate_ave_dic:
                gen_recom_mov[movie] = rate_ave_dic.get(movie)
    gen_recom_sort = sorted(gen_recom_mov.items(), key=lambda x: x[1], reverse=True)
    return dict(gen_recom_sort[:n])

def get_genre_rating(genre, mov_genre_dic, rate_ave_dic):
    movie_lst = []
    rate_sum = 0
    for key in mov_genre_dic:
        if key == genre:
            movie_lst = mov_genre_dic.get(key)
    for movie in movie_lst:
        rate_sum += rate_ave_dic.get(movie, 0)

    return float(rate_sum / len(movie_lst))

def genre_popularity(mov_genre_dic, rate_ave_dic, n):
    genre_rate_ave = {}
    for key in mov_genre_dic:
        genre_rate_ave[key] = get_genre_rating(key, mov_genre_dic, rate_ave_dic)
    genre_rate_ave_sort = dict(sorted(genre_rate_ave.items(), key=lambda x: x[1], reverse=True))
    return dict(list(genre_rate_ave_sort.items())[:n])

# Task 4
def read_user_ratings(f):
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
    
def get_user_genre(user_id, id_rate_dic, movie_dic):
    rate_lst = id_rate_dic[user_id]
    genre_rate_dic = {}
    for key, value in rate_lst:
        moive_genre = movie_dic[key]
        if moive_genre:
            if moive_genre not in genre_rate_dic:
                genre_rate_dic[moive_genre] = [value]
            else:
                genre_rate_dic[moive_genre].append(value)            
    for key, value in genre_rate_dic.items():
        genre_rate_dic[key] = sum(value) / len(value)
    sorted_rate = sorted(genre_rate_dic.items(), key=lambda x: x[1], reverse=True)
    return sorted_rate[0][0]

def recommend_movies(user_id, id_rate_dic, movie_dic, rate_ave_dic):
    favor_genre = get_user_genre(user_id, id_rate_dic, movie_dic)
    all_genre_movie = []
    recommend_dic = {}
    watched_lst = id_rate_dic[user_id]
    watched_movie = []
    unwatched_moive = {}
    for i in range(len(watched_lst)):
        watched_movie.append(watched_lst[i][0])
    for key, value in movie_dic.items():
        if value == favor_genre:
            all_genre_movie.append(key)
    for name in all_genre_movie:
        if name not in watched_movie:
            unwatched_moive[name] = rate_ave_dic[name]
    recom_sort = sorted(unwatched_moive.items(), key=lambda x: x[1], reverse=True)
    return dict(recom_sort[:3])
