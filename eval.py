import sys
from conlleval import evaluate

def eval(pred,gold):
    f_predict = open(pred,encoding = 'utf-8')
    f_true = open(gold,encoding = 'utf-8')

    data_pred = f_predict.readlines()
    data_gold = f_true.readlines()
    
    true_labels = []
    predict_labels = []

    for sent in range(len(data_pred)):
        predict_w = data_pred[sent].strip().split(' ')
        true_w = data_gold[sent].strip().split(' ')  
        
        if len(true_w)==1:
            continue
        
        true_labels.append(true_w[1])
        predict_labels.append(predict_w[1])

    return true_labels, predict_labels

if __name__ == '__main__':
    """
        Usage: python eval.py dataset/dev.out dataset/dev.p2.out
    """
    
    if len(sys.argv) != 3:
        print("Please make sure you have typed in the corrent command!")
        print("Usage: python eval.py [gold file directory] [predict file directory]")
        print("Example: python eval.py dataset/dev.out dataset/dev.p2.out")
        sys.exit()
    
    gold_path = sys.argv[1]
    predict_path = sys.argv[2]

    gold_labels, predict_labels = eval(gold_path, predict_path)
    print(evaluate(gold_labels, predict_labels, verbose=True))

