from flask import Flask, render_template, request
app = Flask(__name__)

def is_triangular(num):
    n = 1
    triangular_num = 1
    
    while triangular_num < num:
        n += 1
        triangular_num = n * (n + 1) // 2
    
    return triangular_num == num

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            num3 = int(request.form['num3'])

            result = {
                'num1': 'Triangular' if is_triangular(num1) else 'Not Triangular',
                'num2': 'Triangular' if is_triangular(num2) else 'Not Triangular',
                'num3': 'Triangular' if is_triangular(num3) else 'Not Triangular'
            }
        except ValueError:
            result = {
                'num1': 'Error: Invalid Input',
                'num2': 'Error: Invalid Input',
                'num3': 'Error: Invalid Input'
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
