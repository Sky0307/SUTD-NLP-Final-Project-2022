# SUTD-NLP-Final-Project-2022

## folder structure

-- (your folder)  
&emsp;&emsp;&emsp;&emsp;-- final-project.ipynb  
&emsp;&emsp;&emsp;&emsp;-- 6ii.ipynb  
&emsp;&emsp;&emsp;&emsp;-- dataset  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- dev.in  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- dev.out  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- dev.p2.out  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- dev.p4.out  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- dev.p5.out  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- test.p6.CRF.out  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- test.p6.model.out  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;-- train  

## How to run the code

1. install the libraries needed, `pip install -r requirements.txt`  
2. All the source code is done in jupyter notebook, run the jupyter notebook as per usual
3. change the directory of where you saved the data file (in the jupyter notebook) if the folder structure is not the same as above

## Result

### Part 2

`python eval.py dataset/dev.out dataset/dev.p2.out`  
processed 3809 tokens with 154 phrases; found: 210 phrases; correct: 71.  
accuracy:  43.06%; (non-O)  
accuracy:  93.25%; precision:  33.81%; recall:  46.10%; FB1:  39.01  
&emsp;&emsp;&emsp;&emsp; negative: precision:  13.85%; recall:  36.00%; FB1:  20.00  65  
&emsp;&emsp;&emsp;&emsp; neutral: precision:  12.50%; recall:  33.33%; FB1:  18.18  8  
&emsp;&emsp;&emsp;&emsp; positive: precision:  44.53%; recall:  48.41%; FB1:  46.39  137  
((33.80952380952381, 46.103896103896105, 39.010989010989015), 0)  

### Part 4

`python eval.py dataset/dev.out dataset/dev.p4.out`  
processed 3809 tokens with 149 phrases; found: 210 phrases; correct: 68.  
accuracy:  50.66%; (non-O)  
accuracy:  93.49%; precision:  32.38%; recall:  45.64%;     FB1:  37.88  
&emsp;&emsp;&emsp;&emsp;negative: precision:  15.38%; recall:  52.63%; FB1:  23.81  65  
&emsp;&emsp;&emsp;&emsp;neutral: precision:   0.00%; recall:   0.00%; FB1:   0.00  8  
&emsp;&emsp;&emsp;&emsp;positive: precision:  42.34%; recall:  44.62%; FB1:  43.45  137  
((32.38095238095238, 45.63758389261745, 37.883008356545965), 0)  

### Part 5
`python eval.py dataset/dev.out dataset/dev.p5.out`
processed 3809 tokens with 311 phrases; found: 210 phrases; correct: 110.
accuracy:  35.71%; (non-O)
accuracy:  91.52%; precision:  52.38%; recall:  35.37%; FB1:  42.23    
         negative: precision:  29.23%; recall:  25.00%; FB1:  26.95  65
          neutral: precision:  25.00%; recall:   5.00%; FB1:   8.33  8
         positive: precision:  64.96%; recall:  45.64%; FB1:  53.61  137
((52.38095238095239, 35.36977491961415, 42.226487523992326), 0)