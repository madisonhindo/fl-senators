from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal
from flask_bootstrap import Bootstrap

app = Flask(__name__)

application = app  

senator_list = convert_to_dict("florida-senators.csv")

Bootstrap(app)

@app.route('/')
def index():
    ids_list = []
    name_list = []
   
    for senator in senator_list:
        ids_list.append(senator['District'])
        name_list.append(senator['Senator'])
        
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title="Florida Senator Index")


@app.route('/senator/<num>')
def detail(num):
    for senator in senator_list:
        if senator['District'] == num:
            sen_dict = senator
            break
    ord = make_ordinal( int(num) )
    return render_template('senator.html', sen=sen_dict, ord=ord, the_title=sen_dict['Senator'])

    
if __name__ == '__main__':
    app.run(debug=True)
