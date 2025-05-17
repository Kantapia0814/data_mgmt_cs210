import csv

# 1-1
def get_ratio_above_40(f):
    with open(f, "r", newline='') as irisfile:
        reader = csv.reader(irisfile)
        next(reader)
        fire_lst = []
        count = 0
        for line in reader:
            if (line[4] == "fire"):
                fire_lst.append(int(float(line[2])))
        for i in range(len(fire_lst)):
            if fire_lst[i] >= 40:
                count += 1
        if len(fire_lst) > 0:
            ratio = round((count / len(fire_lst)) * 100)
        else:
            ratio = 0
    with open("pokemon1.txt", "w") as file:
        file.write(f"Percentage of fire type Pokemons at or above level 40 = {ratio}")
            
# 1-2
def fill_weakness(f):
    with open(f, "r", newline='') as irisfile:
        reader = csv.reader(irisfile)
        header = next(reader)
        data = [line for line in reader]

    weak_dic = {}
    get_type = {}
 
    for line in data:
        poke_type = line[4]
        poke_weak = line[5]
        if poke_type != "NaN":
            if poke_weak not in weak_dic:
                weak_dic[poke_weak] = {}
            if poke_type not in weak_dic[poke_weak]:
                weak_dic[poke_weak][poke_type] = 0
            else:
                weak_dic[poke_weak][poke_type] += 1
    for weak, count in weak_dic.items():
        sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        maximum = sort_count[0][1]
        candi = []
        for poke_type in sort_count:
            if poke_type[1] == maximum:
                candi.append(poke_type[0])
        candi.sort()
        get_type[weak] = candi[0]

    for line in data:
        poke_type = line[4]
        poke_weak = line[5]
        if poke_type == "NaN":
            if poke_weak in get_type:
                line[4] = get_type[poke_weak]
    
    with open("pokemonResult.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(data) 

# 1-3
def get_average(data):
    atk_lst = []
    def_lst = []
    hp_lst = []

    for line in data:
        poke_atk = line[6]    
        if poke_atk != "NaN":
            atk_lst.append(float(poke_atk))
        poke_def = line[7]    
        if poke_def != "NaN":
            def_lst.append(float(poke_def))
        poke_hp = line[8]    
        if poke_hp != "NaN":
            hp_lst.append(float(poke_hp))
    atk_ave = round(sum(atk_lst) / len(atk_lst), 1) if atk_lst else 0
    def_ave = round(sum(def_lst) / len(def_lst), 1) if def_lst else 0
    hp_ave = round(sum(hp_lst) / len(hp_lst), 1) if hp_lst else 0

    return [atk_ave, def_ave, hp_ave]

def fill_values(f):
    with open(f, "r", newline='') as irisfile:
        reader = csv.reader(irisfile)
        header = next(reader)
        data = [line for line in reader]

    above_40 = []
    under_40 = []
    for line in data:
        poke_lv = int(float(line[2]))
        if poke_lv > 40:
            above_40.append(line)
        else:
            under_40.append(line)
    
    above_40_ave = get_average(above_40)
    under_40_ave = get_average(under_40)

    for line in data:
        poke_lv = int(float(line[2]))
        if poke_lv > 40:
            if line[6] == "NaN":
                line[6] = above_40_ave[0]
            if line[7] == "NaN":
                line[7] = above_40_ave[1]
            if line[8] == "NaN":
                line[8] = above_40_ave[2]
        else:
            if line[6] == "NaN":
                line[6] = under_40_ave[0]
            if line[7] == "NaN":
                line[7] = under_40_ave[1]
            if line[8] == "NaN":
                line[8] = under_40_ave[2]
    
    with open("pokemonResult.csv", "w", newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(data)
        
def make_new_csv(f):
    fill_weakness(f)
    fill_values("pokemonResult.csv")

# 1-4
def make_person_dic(f):
    with open(f, "r", newline='') as irisfile:
        reader = csv.reader(irisfile)
        next(reader)
        data = [line for line in reader]

    pers_dic = {}
    for line in data:
        poke_pers = line[3]
        poke_type = line[4]
        if poke_type not in pers_dic:
            pers_dic[poke_type] = []
        if poke_pers not in pers_dic[poke_type]:
            pers_dic[poke_type].append(poke_pers)

    sort_type = sorted(pers_dic.keys())
        
    with open("pokemon4.txt", "w") as file:
        file.write("Pokemon type to personality mapping:\n\n")
        for t in sort_type:
            sort_pers = sorted(pers_dic[t])
            pers_str = ", ".join(sort_pers)
            print_line = f"    {t}: {pers_str}\n"
            file.write(print_line)

# 1-5
def get_hp_ave(f):
    with open(f, "r", newline='') as irisfile:
        reader = csv.reader(irisfile)
        next(reader)
        data = [line for line in reader]

    hp_lst = []
    for line in data:
        if line[9] != "NaN" and line[8] != "NaN":
            poke_hp = float(line[8])
            poke_stg = float(line[9])
            if poke_stg == 3.0:
                hp_lst.append(poke_hp)
    if len(hp_lst) == 0:
        hp_ave = 0
    else:
        hp_ave = round(sum(hp_lst) / len(hp_lst))

    with open("pokemon5.txt", "w") as file:
        file.write(f"Average hit point for Pokemons of stage 3.0 = {hp_ave}")

def main():
    get_ratio_above_40("pokemonTrain.csv")
    make_new_csv("pokemonTrain.csv")
    make_person_dic("pokemonResult.csv")
    get_hp_ave("pokemonResult.csv")

main()