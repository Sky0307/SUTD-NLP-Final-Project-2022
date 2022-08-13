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
processed 3809 tokens with 44 phrases; found: 210 phrases; correct: 14.  
accuracy:  50.00%; (non-O)  
accuracy:  92.41%; precision:   6.67%; recall:  31.82%; FB1:  11.02  
&emsp;&emsp;&emsp;&emsp;negative: precision:   0.00%; recall:   0.00%; FB1:   0.00  65  
&emsp;&emsp;&emsp;&emsp;neutral: precision:   0.00%; recall:   0.00%; FB1:   0.00  8  
&emsp;&emsp;&emsp;&emsp;positive: precision:  10.22%; recall:  32.56%; FB1:  15.56  137  
((6.666666666666667, 31.818181818181817, 11.023622047244094), 0)

### Part 6i
`python eval.py dataset/dev.out dataset/dev.p6.CRF.out`  
processed 3809 tokens with 56 phrases; found: 210 phrases; correct: 20.  
accuracy:  31.82%; (non-O)  
accuracy:  92.26%; precision:   9.52%; recall:  35.71%; FB1:  15.04  
&emsp;&emsp;&emsp;&emsp;negative: precision:   4.62%; recall:  25.00%; FB1:   7.79  65  
&emsp;&emsp;&emsp;&emsp;neutral: precision:  12.50%; recall:  16.67%; FB1:  14.29  8  
&emsp;&emsp;&emsp;&emsp;positive: precision:  11.68%; recall:  42.11%; FB1:  18.29  137  
((9.523809523809524, 35.714285714285715, 15.037593984962406), 0)  

### Part 6ii
`python eval.py dataset/dev.out dataset/dev.p6.model.out`  
processed 3809 tokens with 177 phrases; found: 210 phrases; correct: 81.  
accuracy:  44.35%; (non-O)  
accuracy:  93.12%; precision:  38.57%; recall:  45.76%; FB1:  41.86  
&emsp;&emsp;&emsp;&emsp;negative: precision:  16.92%; recall:  36.67%; FB1:  23.16  65  
&emsp;&emsp;&emsp;&emsp;neutral: precision:   0.00%; recall:   0.00%; FB1:   0.00  8  
&emsp;&emsp;&emsp;&emsp;positive: precision:  51.09%; recall:  47.95%; FB1:  49.47  137  
((38.57142857142858, 45.76271186440678, 41.860465116279066), 0)  
