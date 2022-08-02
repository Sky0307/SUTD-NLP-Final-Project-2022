import sys 
from collections import defaultdict
import math

def read_train_file(directory):
    x_train = []
    y_train = []
    all_tags = []
    all_words = []

    with open(directory) as f:
        x_sent = []
        y_sent = []
        for line in f:
            if line == '\n': # end of a sentence
                x_train.append(x_sent)
                y_train.append(y_sent)
                x_sent=[]
                y_sent=[]
            else:
                temp = line.strip().split()
                x_sent.append(temp[0]) # word
                y_sent.append(temp[1]) # tag

                if temp[1] not in all_tags:
                    all_tags.append(temp[1])
                if temp[0] not in all_words:
                    all_words.append(temp[0])

    return x_train, y_train, all_tags, all_words

def get_feature_dict(x_train, y_train):
    label_dict = defaultdict(int)  # {LABEL : COUNT} e.g: {'o': 24273, 'B-negative': 278, ...}
    word_label_dict = defaultdict(int) # {(LABEL, WORD): COUNT} 
                               # e.g: {('O', 'All'): 3, ('B-positive', 'food'): 131, ...}

    for i in range(len(x_train)):
        for j in range(len(x_train[i])):
            label_dict[y_train[i][j]] += 1
            word_label_dict[(y_train[i][j], x_train[i][j])] += 1
    
    # print(f"y_dict: {y_dict}")
    # print(f"yx_dict: {yx_dict}")

    emission = defaultdict(int)
    for k in word_label_dict:
        tag = k[0]
        string = 'emission:'+ str(k[0]) + '+' + str(k[1])
        emission[string] = math.log(float(word_label_dict[k])/label_dict[tag])
    # print(f"emission: {emission}")

    for i in ALL_TAGS:
        for j in ALL_WORDS:
            try:
                string = 'emission:'+str(i)+'+'+str(j)
                emission[string]
            except KeyError:
                emission[string] = - math.inf

    # getting transition
    yi_dict = defaultdict(int)
    yj_dict = defaultdict(int)
    
    for i in range(len(x_train)):
        if len(y_train[i]) == 0: # this seems to be useless
            continue

         # adding START and STOP tag to each sentence
        yi_dict['START'] += 1
        yj_dict[('START', y_train[i][0])] += 1
        yj_dict[(y_train[i][-1],'STOP')] += 1

        for j in range(len(x_train[i])-1):
            yi_dict[y_train[i][j]] += 1
            yj_dict[(y_train[i][j],y_train[i][j+1])] += 1
        yi_dict[y_train[i][-1]] += 1
                
    transition = defaultdict(int)
    for k in yj_dict:
        string = 'transition:' + str(k[0]) + '+' + str(k[1])
        transition[string] = math.log(float(yj_dict[k])/yi_dict[k[0]])
    
    for u in ALL_TAGS + ["START"]:
        for v in ALL_TAGS + ["STOP"]:
            try:
                string = 'transition:'+str(u)+'+'+str(v)
                transition[string]
            except KeyError:
                transition[string] = - math.inf
    
    if "transition:START+STOP" in transition:
        del transition["transition:START+STOP"]

    write_output(emission, "emission_P1.txt") # save emission dictionary
    write_output(transition, "transition_P1.txt") # save transition dictionary

    features = {}
    for key in emission:
        features[key] = emission[key]
    for key in transition:
        features[key] = transition[key]
    
    # name_to_index = {}
    # index_to_name = {}
    # index = 0
    # for key in features:
    #     name_to_index[key] = index
    #     index_to_name[index] = key
    #     index += 1
    return features

def write_output(feat, output_file):
    with open(output_file, "w") as out:
        for (k, v) in feat.items():
            out.write(f"{k} {v}\n")


if __name__ == "__main__":
    folder =  sys.argv[1]

    x_train, y_train, ALL_TAGS, ALL_WORDS = read_train_file(folder+'/train')

    feature_dict = get_feature_dict(x_train, y_train)

    write_output(feature_dict, "features_P1.txt") # save overall features dictionary