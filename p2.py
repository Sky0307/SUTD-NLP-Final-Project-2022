import sys

def add_dict_item(_dict, first_elem, sec_elem, value):
    if first_elem not in _dict.keys():
        _dict[first_elem] = {}
    _dict[first_elem][sec_elem] = float(value)

def get_features(directory=""):
    emission_dict = {}
    transition_dict = {}
    
    with open (directory + "/emission_P1.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                split_idx = line.index(":") + 1
                weight = line.split(" ")[1]
                tag = line[split_idx : ].split(" ")[0].split("+")[0]
                token = line[split_idx : ].split(" ")[0].split("+")[1]
                add_dict_item(emission_dict, tag, token, weight)

    with open (directory + "/transition_P1.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                split_idx = line.index(":") + 1
                weight = line.split(" ")[1]
                U = line[split_idx : ].split(" ")[0].split("+")[0]
                V = line[split_idx : ].split(" ")[0].split("+")[1]
                add_dict_item(transition_dict, U, V, weight)
    
    feature_dict = {}
    feature_dict["emission"] = emission_dict
    feature_dict["transition"] = transition_dict
    return feature_dict

def viterbi(sent, feature_dict):
    word_dict = {0: {"START":0}}
    pointer = {}
    tag = []

    for i in range(len(sent)):
        word_dict[i+1] = {}
        pointer[i] = {}

        for current_tag in word_dict[i].keys():
            score = word_dict[i][current_tag]
            if current_tag != "STOP":
                for next_tag in feature_dict["transition"][current_tag].keys():
                    current = score + feature_dict["transition"][current_tag][next_tag]
                    if next_tag != "STOP":
                        current += feature_dict["emission"][next_tag].get(sent[i], 0)
                        
                        if ((word_dict[i+1].get(next_tag)!= None and\
                            current > word_dict[i+1][next_tag] or\
                            word_dict[i+1].get(next_tag) == None)):
                            pointer[i][next_tag] = current_tag
                            word_dict[i+1][next_tag] = current

    word_dict[len(sent) + 1] = {}
    pointer[len(sent)] = {}
    for current_tag in word_dict[len(sent)].keys():
        next_tag = "STOP"
        if current_tag != "STOP":
            score = word_dict[len(sent)][current_tag] + feature_dict["transition"][current_tag][next_tag]
            if(word_dict[len(sent) + 1].get(next_tag) != None and\
                score > word_dict[len(sent) + 1][next_tag] or\
                word_dict[len(sent) + 1].get(next_tag) == None):
                pointer[len(sent)][next_tag] = current_tag
                word_dict[len(sent) + 1][next_tag] = score
    
    current="STOP"
    tag.append(current)

    for i in range(len(sent),-1,-1):
        tag.insert(0,pointer[i][current])
        current = pointer[i][current]
    return tag[1:-1]

def run_viterbi(test_file, output_file, feature_dict):
    sent = []
    with open(output_file, "w") as output:
        for line in open(test_file, "r"):
            # constructing sentence
            if line != "\n":
                sent.append(line.strip())
            else:
                tag = viterbi(sent, feature_dict) # send to viterbi
                for i in range(len(sent)):
                    string = f"{str(sent[i])} {str(tag[i])}\n"
                    output.write(string)
                # finish a sentence and reset the sent list
                sent = []
                output.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(len(sys.argv))
        print(f"Please ensure you have typed in the correct command")
        print(f"Example: python p2.py features dataset/dev.in")
        sys.exit()
    
    
    features_dir = sys.argv[1]
    test_file = sys.argv[2]
    output_file = sys.argv[3]

    feature_dict = get_features(features_dir)
    run_viterbi(test_file, output_file, feature_dict)