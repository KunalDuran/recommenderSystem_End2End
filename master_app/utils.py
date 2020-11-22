


def get_max_rating(df, genre):
    sorted_df = df[df['genre']==genre].sort_values('ratings', ascending=False)
    if sorted_df.shape[0] <= 2:
        ''' Return a book from top 10 rated book'''
        return dict(df.sort_values('ratings', ascending=False).iloc[:10].sample(1).iloc[0])
    top_value = sorted_df.iloc[0]
    return dict(top_value)