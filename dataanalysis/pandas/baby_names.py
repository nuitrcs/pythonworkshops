#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys

# Set up some variables for use later
dataset_path = 'data\\names'
begin_year = 1880
end_year = 2016

def create_dataframe():
    columns = ('name', 'sex', 'births')
    pieces = []
    for year in range(begin_year, end_year + 1):
        filename = '%s/yob%d.txt' % (dataset_path, year)
        piece = pd.read_csv(filename, names=columns)
        piece['year'] = year
        pieces.append(piece)
        
    return pd.concat(pieces, ignore_index=True)

def get_births_series(df, name, sex):
    single_sex_df = df.xs(sex, level='sex')
    return single_sex_df[single_sex_df.name == name]['births']

def create_births_figure(s, name, sex):
    plt.style.use('seaborn')
    sex_full = 'female'
    if sex == 'M':
        sex_full = 'male'
    plot = s.plot(title='Annual count of US %s births for name %s' % (sex_full, name))
    return plot.get_figure()

def main():
    name = sys.argv[1]
    sex = sys.argv[2]

    df = create_dataframe()
    df = df.set_index(keys=['year', 'sex'])
    name_series = get_births_series(df, name, sex)
    fig = create_births_figure(name_series, name, sex)
    fig.savefig('%s.png' % name)

if __name__ == '__main__':
    main()