from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:w>/<int:h>')
def tinhBmi(w, h):
    bmi = w / ((h/100)**2)  
    
    if bmi < 16:
        return 'Thieu can nghiem trong'
    elif 16 <= bmi < 18.5:
        return 'Thieu can'
    elif 18.5 <= bmi < 25:
        return 'Binh thuong'
    elif 25 <= bmi < 30:
        return 'Thua can'
    else:
        return 'Beo phi'


chiso = {}
@app.route('/bmi_2/<int:w2>/<int:h2>')

def tinhBmi2(w2, h2):
    bmi2 = w2 / ((h2/100)**2)
    chiso['w'] = w2
    chiso['h'] = h2
    chiso['bmi'] = bmi2

    return render_template('bmi.html', chiso = chiso)

if __name__ == '__main__':
    app.run(debug=True)

