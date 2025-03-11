from flask import Flask, render_template, request

app = Flask(__name__)

shopping_list = []

@app.route('/', methods=['GET', 'POST'])
def home():
    global shopping_list

    if request.method == 'POST':
        input1 = request.form['input1'] 
        input2 = request.form['input2']  
        if input1 == '1':  
            shopping_list.append(input2)
        elif input1 == '2': 
            index = int(input2) - 1
            if 0 <= index < len(shopping_list):
                new_item = request.form['input2']
                shopping_list[index] = new_item
        elif input1 == '3':  
            index = int(input2) - 1
            if 0 <= index < len(shopping_list):
                shopping_list.pop(index)
        elif input1 == '4':  
            shopping_list = []  
            return render_template('index.html', shopping_list=shopping_list)
        
    return render_template('index.html', shopping_list=shopping_list)  

if __name__ == '__main__':
    app.run(debug=True)





