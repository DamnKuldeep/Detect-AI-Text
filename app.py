from flask import Flask, render_template, request, jsonify
import model_kul

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        user_input = data.get('text', '')
        ans,prob = model_kul.result(user_input)
        print(ans)
        if ans==0:
            modified_text = "It's a Human written text. With probability of " + str(f'{prob*100:.4f}') +"%."
        else:
            modified_text = "It's a AI generated text. With probability of " + str(f'{prob*100:.4f}') +"%."
        return jsonify(result=modified_text)
    
    return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    