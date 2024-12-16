def sorted_df(df,priority):
    is_asc = False if priority is None else True
    filter_value = 'comprehensive_score' if priority is None else priority.value
    rdf_sorted = df.sort_values(filter_value, ascending=is_asc)
    return rdf_sorted