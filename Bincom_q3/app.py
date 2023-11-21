from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Boluwatito",
    database="bincom_test"
)
app = Flask(__name__)

def parties_names():
    cursor = mydb.cursor()
    query = 'SELECT partyname FROM party;'
    cursor.execute(query)
    party_list = cursor.fetchall()

    names = []

    for name in party_list:
        names.append(name)

    parties = []
    for party in names:
        list_of_parties = party[0].strip()
        parties.append(list_of_parties)
    return parties


@app.route('/polling_unit_form', methods=['GET'])
def polling_unit_form():
    parties = parties_names()
    return render_template('polling_unit_form.html', parties=parties)

@app.route('/store_results', methods=['POST'])
def store_results():
    try:
        polling_unit_id = request.form.get('polling_unit_id')
        selected_party = request.form.get('party')
        results = request.form.get('result')

        # Create a cursor to interact with the database
        cursor = mydb.cursor()

        # Create the table if it doesn't exist (you may want to do this separately)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS pu_results (
            polling_unit_id INT PRIMARY KEY,
            {}
        );
        """.format(' INT, '.join(parties_names()) + ' INT')
        cursor.execute(create_table_query)

        # Insert the result into the database for the selected party
        insert_query = f"""
    INSERT INTO pu_resultsgit
    (polling_unit_id, {selected_party}, {', '.join(parties_names())})
    VALUES (%s, %s, {', '.join(['%s'] * len(parties_names()))});
"""


        # Commit the changes
        mydb.commit()

        # Close the cursor
        cursor.close()

        return "Result stored successfully!"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
