from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request
from service import inference

app = Flask(__name__)
app.config['SECRET_KEY'] = 'atut-datascience'
Bootstrap(app)


@app.route('/', methods=["POST", "GET"]) # home page that return 'index'
def index():
    if request.method == 'GET':  # if the request is a GET we return the home page
        return render_template('index.html')
    else:
        tenure = request.form.get('tenure')
        MonthlyCharges = request.form.get('MonthlyCharges')
        TotalCharges = request.form.get('TotalCharges')
        gender = request.form.get('gender')
        SeniorCitizen = request.form.get('SeniorCitizen')
        Partner = request.form.get('Partner')
        Dependents = request.form.get('Dependents')
        PhoneService = request.form.get('PhoneService')
        MultipleLines = request.form.get('MultipleLines')
        InternetService = request.form.get('InternetService')
        OnlineSecurity = request.form.get('OnlineSecurity')
        OnlineBackup = request.form.get('OnlineBackup')
        DeviceProtection = request.form.get('DeviceProtection')
        TechSupport = request.form.get('TechSupport')
        StreamingTV = request.form.get('StreamingTV')
        StreamingMovies = request.form.get('StreamingMovies')
        Contract = request.form.get('Contract')
        PaperlessBilling = request.form.get('PaperlessBilling')
        PaymentMethod = request.form.get('PaymentMethod')

        data = {
            "tenure":int(tenure),
            "MonthlyCharges": float(MonthlyCharges),
            "TotalCharges":float(TotalCharges),
            "gender":gender,
            "SeniorCitizen":int(SeniorCitizen),
            "Partner":Partner,
            "Dependents":Dependents,
            "PhoneService":PhoneService,
            "MultipleLines":MultipleLines,
            "InternetService":InternetService,
            "OnlineSecurity":OnlineSecurity,
            "OnlineBackup":OnlineBackup,
            "DeviceProtection":DeviceProtection,
            "TechSupport":TechSupport,
            "StreamingTV":StreamingTV,
            "StreamingMovies":StreamingMovies,
            "Contract":Contract,
            "PaperlessBilling":PaperlessBilling,
            "PaymentMethod":PaymentMethod
        }

        result = inference(data)
        message = "{} the probability is: {}".format(result["message"], result["probability"])

        return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9000", debug=True)
