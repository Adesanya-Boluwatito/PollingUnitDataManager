from flask import Flask, render_template,request
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Boluwatito",
    database="bincom_test"
)


def get_polling_unit_results(polling_id):

    cursor = mydb.cursor()
    query = f'SELECT result_id, party_score FROM announced_pu_results;'

    cursor.execute(query)
    rows = cursor.fetchall()
    score_list = []
    for row in rows:
        score_list.append(list(row))

    for item in score_list:
        if int(polling_id) == item[0]:
            result = f"The polling Unit result is: {item[1]}"
            return result

    cursor.close()
    mydb.close()


@app.route('/polling_unit', methods=["GET", "POST"])
def polling_unit_results():
    if request.method == 'POST':
        polling_id = request.form['polling_id']
        results = get_polling_unit_results(polling_id)
        return render_template('polling_unit_results.html', results=results)

    return render_template('polling_unit_form.html')


if __name__ == '__main__':
    app.run(debug=True)


