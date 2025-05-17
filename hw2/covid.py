import csv

# 2-1
def change_age_format(data):
    for line in data:
        age = line[1]
        if "-" in age:
            a, b = map(int, age.split("-"))
            age_ave = round((a + b) / 2)
            line[1] = str(age_ave)

# 2-2
def make_date_change(date):
    day, month, year = date.split(".")
    new_date = ".".join([str(month), str(day), str(year)])
    return new_date

def change_date_format(data):
    for line in data:
        date_1 = line[8]
        date_2 = line[9]
        date_3 = line[10]
        if date_1 != "NaN":
            line[8] = make_date_change(date_1)
        if date_2 != "NaN":
            line[9] = make_date_change(date_2)
        if date_3 != "NaN":
            line[10] = make_date_change(date_3)

# 2-3
def get_average(data):
    prov_dic = {}
    ave_dic = {}

    for line in data:
        province = line[4]
        latitude = line[6]
        longitude = line[7]

        if latitude != "NaN" and longitude != "NaN":
            if province not in prov_dic:
                prov_dic[province] = []
            prov_dic[province].append([float(latitude), float(longitude)])
    for key, value in prov_dic.items():
        sum_lat = 0.0
        sum_lon = 0.0
        for [x, y] in value:
            sum_lat = sum_lat + x
            sum_lon = sum_lon + y
        
        lat_ave = round(sum_lat / len(value), 2)
        lon_ave = round(sum_lon / len(value), 2)
        ave_dic[key] = [lat_ave, lon_ave]

    return ave_dic

def fill_lat_lon(data):
    ave_dic = get_average(data)
    for line in data:
        province = line[4]
        latitude = line[6]
        longitude = line[7]
        if latitude == "NaN":
            line[6] = str(ave_dic[province][0])
        if longitude == "NaN":
            line[7] = str(ave_dic[province][1])

# 2-4
def fill_city(data):   
    city_dic = {}
    get_city = {}
    for line in data:
        city = line[3]
        province = line[4]
        if city != "NaN":
            if province not in city_dic:
                city_dic[province] = {}
            if city not in city_dic[province]:
                city_dic[province][city] = 1
            else:
                city_dic[province][city] += 1
    
    for province, count in city_dic.items():
        sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        maximum = sort_count[0][1]
        candi = []
        for city in sort_count:
            if city[1] == maximum:
                candi.append(city[0])
        candi.sort()
        get_city[province] = candi[0]

    for line in data:
        city = line[3]
        province = line[4]
        if city == "NaN":
            line[3] = get_city[province]

# 2-5
def fill_symptom(data):
    symp_dic = {}
    get_symp = {}
    for line in data:
        province = line[4]
        symptom = line[11]
        if symptom != "NaN":
            symp_lst = symptom.split(";")
            for elem in symp_lst:
                just_symp = elem.strip()
                if province not in symp_dic:
                    symp_dic[province] = {}
                if just_symp not in symp_dic[province]:
                    symp_dic[province][just_symp] = 1
                else:
                    symp_dic[province][just_symp] += 1
    
    for province, count in symp_dic.items():
        sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        maximum = sort_count[0][1]
        candi = []
        for symp in sort_count:
            if symp[1] == maximum:
                candi.append(symp[0])
        candi.sort()
        get_symp[province] = candi[0]

    for line in data:
        province = line[4]
        symptom = line[11]
        if symptom == "NaN":
            line[11] = get_symp[province]

def main():
    with open("covidTrain.csv", "r", newline='') as irisfile:
        reader = csv.reader(irisfile)
        header = next(reader)
        data = [line for line in reader]

    change_age_format(data)
    change_date_format(data)
    fill_lat_lon(data)
    fill_city(data)
    fill_symptom(data)

    with open("covidResult.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(data)

main()