# dm-code-challenge

* dosing.py takes two csv files (t2_ec 20190619.csv, t2_registry 20190619.csv), merges them, fiters with conditions on viscode, svdose, ECSDSTXT and generate a csv file and a pie chart. It contains three functions:
  * left_mergedf(df1, df2, c1, c2): left merge dataframe df1 with df2 on conditions c1 and c2
  * filter_df(dataframe, column, condition): filter dataframe according to the condition on column
  * filter_not_df(dataframe, column, condition):: filter dataframe with column items not equal to the condition


* dosing.py takes three or four command line parameters: viscode, svdose, ECSDSTXT and directory(if entering 4 
parameters). To execute dosing.py, enter 'python dosing.py Pm1 Pm2 Pm3 (Pm4)'. If the Pm4 is not provided, the result csv file will be saved at the current directory. If no parameters are provided (python dosing.py), dosing.py will use the default setting: viscode = 'w02', svdose = 'Y', ECSDSTXT = 280, directory = ""


* If a non-exising directory is provided, the program will show "not a vaild directory" on the terminal after generating the pie chart

* test_dosing.py use pytest to test three functions used in dosing.py. To execute the program enter "pytest test_dosing.py" on command line. 
