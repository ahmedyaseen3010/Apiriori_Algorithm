from flask import Flask, render_template, request

# Import the apriori function from a separate module (e.g., apriori_algorithm.py)
from apriori_algorithm import apriori

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    # Get the form data
    casher = request.form.get('transactions')
    support_threshold = int(request.form.get('support_threshold'))

    # Split the transactions string into a list
    casher = [eval(transaction) for transaction in casher.split('\n') if transaction.strip()]

    # Run the Apriori algorithm
 
    frequent_itemsets = apriori(casher, support_threshold)

    return render_template('result.html', frequent_itemsets=frequent_itemsets)


if __name__ == '__main__':
    app.run(debug=True)
