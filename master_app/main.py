from flask import Flask, request, jsonify, render_template
import pandas as pd
from utils import get_max_rating


app = Flask(__name__)


df = pd.read_json('cleaned_final_data.json', orient='record')

@app.route('/', methods=['GET', 'POST'])
def home():
    '''Show 10 random books from Data Frame, display card.
    redirect to other page when user click a book
    show that book and one book in separate card saying "You may also like..."'''
    N = 9
    sample = df.sample(N)
    sample10 = [dict(sample.iloc[i]) for i in range(N)]
    # print(sample10)

    return render_template('index.html', sample10=sample10)



@app.route('/output/<bookTitle>', methods=['GET', 'POST'])
def output(bookTitle):
    print('result is ', bookTitle)
    result = dict(df[df['book_title']==bookTitle].squeeze())
    prediction = get_max_rating(df, result['genre'])
    return render_template('output.html', result=result, prediction=prediction)




if __name__ == "__main__":
    app.run(debug=True)



