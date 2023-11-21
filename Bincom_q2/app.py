from flask import Flask, render_template,request
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Boluwatito",
    database="bincom_test"
)


def sum_of_each_polling_unit_result():
    cursor = mydb.cursor()
    query = f'SELECT polling_unit_uniqueid, party_score FROM announced_pu_results;'
    cursor.execute(query)
    rows = cursor.fetchall()
    lists = []

    for row in rows:
        lists.append(list(row))

    sums_dict = {}

    for item in lists:
        key = item[0]
        value = item[1]

        if key in sums_dict:
            sums_dict[key] += value
        else:
            sums_dict[key] = value

    return sums_dict
# print(sums_dict)

def name_of_each_lga():
    cursor = mydb.cursor()
    name = 'SELECT lga_id, lga_name FROM lga;'
    cursor.execute(name)
    rows = cursor.fetchall()
    list_name = []
    for name in rows:
        list_name.append(name)

    dict_name = dict(list_name)
    return dict_name

def local_government_data():
    new_dict = {}
    for key in name_of_each_lga():
        str_key = str(key)
        if str_key in sum_of_each_polling_unit_result():
            new_dict[name_of_each_lga()[key]] = sum_of_each_polling_unit_result()[str_key]

    return new_dict


def get_total_result_by_local_government(lga):
    if lga in local_government_data():
        resu = (local_government_data()[lga])

        return resu

def get_local_governments():
    lga = []
    for key in local_government_data():
        lga.append(key)

    return lga


@app.route('/total_results', methods=["GET", "POST"])
def total_results():
    if request.method == 'POST':
        local_government = request.form['local_government']
        total_result = get_total_result_by_local_government(local_government)
        return render_template('total_results.html', local_government=local_government, total_result=total_result)

    local_governments = get_local_governments()
    return render_template('total_results_form.html', local_governments=local_governments)



if __name__ == '__main__':
    app.run(debug=True)