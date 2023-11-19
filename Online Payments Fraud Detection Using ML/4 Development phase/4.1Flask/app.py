from flask import Flask, request, render_template
import pickle as pkl

model = pkl.load(open("model.pkl", 'rb'))

app = Flask(__name__)


@app.route("/Home.html")
def home1():
    return render_template("Home.html")


@app.route("/")
def home():
    return render_template("Home.html")


@app.route('/Predict.html')
def predict_page():
    return render_template('Predict.html')


@app.route('/Submit.html', methods=['POST'])
def predict():
    # Get user input from the form
    feature1 = float(request.form['step'])
    feature2 = float(request.form['type'])
    feature3 = float(request.form['amount'])
    feature4 = float(request.form['oldbalanceOrg'])
    feature5 = float(request.form['newbalanceOrg'])
    feature6 = float(request.form['oldbalanceDest'])
    feature7 = float(request.form['newbalanceDest'])

    # Make a prediction using the loaded model
    prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6, feature7]])

    output = None
    if prediction[0] == 0:
        output = "is not a fraud transaction !!! "
    else:
        output = "is a fraud transaction !!! "

    # return str(prediction[0])  # Convert the prediction to a string
    return render_template('submit.html', prediction=output)


if __name__ == "__main__":
    app.run(debug=True)