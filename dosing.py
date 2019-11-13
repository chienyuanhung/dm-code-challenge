# import the dependency
import pandas as pd
import plotly.graph_objects as go
import sys

# set vaules for parameters
viscode = 'w02'
svdose = 'Y'
ECSDSTXT = 280
directory = ""

# filter function with 'equal to' condition
def filter_df(dataframe, column, condition):
    return dataframe[dataframe[column] == condition]

# filter function with 'not equal to' condition
def filter_not_df(dataframe, column, condition):
    return dataframe[dataframe[column] != condition]

# function for left_merge two datafrane on conditions
def left_mergedf(df1, df2, c1, c2):
    return pd.merge(df1, df2,  how='left', on = [c1, c2])


# set parameters from command line
if len(sys.argv) == 4:
    viscode = sys.argv[1]
    svdose = sys.argv[2]
    ECSDSTXT = int(sys.argv[3])

if len(sys.argv) == 5:
    viscode = sys.argv[1]
    svdose = sys.argv[2]
    ECSDSTXT = sys.argv[3]
    directory = sys.argv[3]+'/'


# read the csv files
file1 = "t2_ec 20190619.csv"
t2_ec = pd.read_csv(file1)

file2 = "t2_registry 20190619.csv"
t2_registry = pd.read_csv(file2)

# filter t2_registry 20190619 for pie chart
pie_chart_filter = filter_not_df(t2_registry, "VISCODE", "bl")  
pie_chart_filter = filter_df(pie_chart_filter, "SVPERF", "Y") 

pie_chart_data = pie_chart_filter['VISCODE'].value_counts()

# List of VISCODE
pie_chart_index = pie_chart_data.index

# create the pie chart with plotly

labels = pie_chart_index
values = pie_chart_data

fig = go.Figure(go.Pie(labels=labels, values=values, 
                hovertemplate = 'VISCODE: %{label} <br> Count: %{value} (%{percent})'))

fig.update_layout(title_text="Viscodes from Registry")
fig.show()



# Left merge t2_registry and t2_ec (t2_registry as the left)
merge_df = left_mergedf(t2_registry, t2_ec, 'RID', 'VISCODE') 

# filter records with values of VISCODE(default as 'w02'), svdose(default as 'Y')
# ECSDSTXT(default not equal to 280) 
merge_filter = filter_df(merge_df,"VISCODE",  viscode) 
merge_filter = filter_df(merge_filter,"SVDOSE",  svdose)  
merge_filter = filter_not_df(merge_filter, "ECSDSTXT", ECSDSTXT) 

# rename the columns and select ID, RID, USERID, VISCODE, SVDOSE, ECSDSTXT for new dataframe
merge_filter = merge_filter.rename(columns={"ID_x": "ID", "USERID_x": "USERID"})
final_merge = merge_filter[['ID', 'RID', 'USERID', 'VISCODE', 'SVDOSE', 'ECSDSTXT']]

# save the dataframe as results.csv
file = directory+"results.csv"
final_merge.to_csv(file, index=False)
