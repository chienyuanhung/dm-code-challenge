import dosing
import pandas as pd

# read the csv files
file1 = "t2_ec 20190619.csv"
t2_ec = pd.read_csv(file1)

file2 = "t2_registry 20190619.csv"
t2_registry = pd.read_csv(file2)

# test filter_df function
def test_filter_df():
    assert dosing.filter_df(t2_ec, 'VISCODE', 'w04').ENTRY[0] == 4
    assert dosing.filter_df(t2_registry, 'VISCODE', 'sc').USERID[0] == 'BBAGGINS_UCSD_EDU_2'

def test_filter_not_df():
    assert dosing.filter_not_df(t2_ec, 'ID', 6).VISCODE[1] == 'w08'
    assert len(dosing.filter_not_df(t2_registry, "VISCODE", "sc")) == 11

def test_left_mergedf():
    assert dosing.left_mergedf(t2_registry, t2_ec, 'RID', 'VISCODE').SVSTDT[0] == '8/9/18'
    assert dosing.left_mergedf(t2_ec, t2_registry,'RID', 'VISCODE').SVRESCRN[0] == '-4'
    
    
