import re
import math
# part 1
# 3-1-1
def make_clean(file):
    file = file.strip()
    file = re.sub(r'[^\w\s]', '', file)
    file = re.sub(r'\s+', ' ', file)
    file = re.sub(r'http://\S+', '', file)
    file = re.sub(r'https://\S+', '', file)
    file = file.lower()
    return file

# 3-1-2
def remove_sw(file, stopwords):
    with open(stopwords, "r") as word_file:
        stopword_lst = []
        for line in word_file:
            stopword = line.strip().lower()
            stopword_lst.append(stopword)
    
    word_lst = file.split()
    new_word_lst = []
    for i in range(len(word_lst)):
        word_lst[i] = word_lst[i].lower()
    for word in word_lst:
        if word not in stopword_lst:
            new_word_lst.append(word)
    result = " ".join(new_word_lst)
    return result

# 3-1-3
def stem_and_lem(file):
    word_lst = file.split()
    new_word_lst = []

    for word in word_lst:
        if word[-3:] == "ing":
            word = word[:-3]
        elif word[-2:] == "ly":
            word = word[:-2]
        elif word[-4:] == "ment":
            word = word[:-4]
        new_word_lst.append(word)
    result = " ".join(new_word_lst)
    return result

def preprocess(file, stopwords):
    with open(file, "r") as text_file:
        total = text_file.read()
    
    total = make_clean(total)
    total = remove_sw(total, stopwords)
    total = stem_and_lem(total)
    with open("preproc_" + file, "w") as text_file:
        text_file.write(total)

# part 2
def check_word_freq(file):
    word_lst = file.split()
    word_freq_dic = {}
    for word in word_lst:
        if word not in word_freq_dic:
            word_freq_dic[word] = 1
        else:
            word_freq_dic[word] += 1
    return word_freq_dic

def get_tf(word_freq_dic):
    tf_dic = {}
    count = 0
    for word in word_freq_dic:
        count += word_freq_dic[word]
    for word in word_freq_dic:
        tf_dic[word] = round(word_freq_dic[word] / count, 2)
    return tf_dic

def get_idf(num_of_t_dic, num_of_doc):
    idf_dic = {}
    for word, count in num_of_t_dic.items():
        idf_dic[word] = round(math.log(num_of_doc / count) + 1, 2)
    return idf_dic

def get_tf_idf_score(tf_dic, idf_dic):
    tf_idf_dic = {}
    for word in tf_dic:
        if word in idf_dic:
            tf_idf_dic[word] = round(tf_dic[word] * idf_dic[word], 2)
    sort_list = sorted(tf_idf_dic.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for i in range(min(5, len(sort_list))):
        result.append(sort_list[i])
    return result

def main():
    with open("tfidf_docs.txt", "r") as whole_file:
        file_names = []
        for file_name in whole_file:
            file = file_name.strip()
            file_names.append(file)
    new_file_names = []
    for file in file_names:
        preprocess(file, "stopwords.txt")
        new_file_names.append("preproc_" + file)
    file_word_freq = []
    num_of_t_dic = {}
    
    for file in new_file_names:
        with open(file, "r") as text_file:
            total = text_file.read()
        word_freq_dic = check_word_freq(total)
        file_word_freq.append((file, word_freq_dic))
        check_word = set(word_freq_dic.keys())
        for word in check_word:
            if word not in num_of_t_dic:
                num_of_t_dic[word] = 1
            else:
                num_of_t_dic[word] += 1
    idf_dic = get_idf(num_of_t_dic, len(file_word_freq))

    for (file, word_freq_dic) in file_word_freq:
        tf_dic = get_tf(word_freq_dic)
        result = get_tf_idf_score(tf_dic, idf_dic)

        output_name = "tfidf_" + file.replace("preproc_", "")
        with open(output_name, "w") as output:
            for (word, score) in result:
                output.write(f"({word},{score})\n")

main()