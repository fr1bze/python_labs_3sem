'H'] >= 10) | (data_all['G'] >= 10) ].groupby(by = 'group_out', as_index=False).count()
print(data_all_res.loc[:,['group_faculty'