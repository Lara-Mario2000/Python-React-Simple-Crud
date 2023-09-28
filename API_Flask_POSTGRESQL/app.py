from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

from config import config, Config

app = Flask(__name__)
CORS(app, origins="http://localhost:5173", supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])


conn = psycopg2.connect(Config.DATABASE_URL)

@app.route('/employee', methods=['GET'])
def read_all_emplooyes():
    try:
        cursor = conn.cursor()
        sql = 'SELECT id, first_name, last_name, job_title, phone_number, image_url FROM employee'
        cursor.execute(sql)
        data = cursor.fetchall()
        employees = []
        for row in data:
            employee = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'job_title': row[3],
                'phone_number': row[4],
                'image_url': row[5]
            }
            employees.append(employee)

        return jsonify({
            'employees': employees,
            'message': 'employee_list'
        })
    except Exception as ex:
        return jsonify({
            'message': 'Error'
        })
    
@app.route('/employee/<id>', methods=['GET'])
def read_one_employee(id):
    try:
        cursor = conn.cursor()
        sql = 'SELECT id, first_name, last_name, job_title, phone_number, image_url FROM employee WHERE id = {0}'.format(id)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data != None:
            employee = {
                'id': data[0],
                'first_name': data[1],
                'last_name': data[2],
                'job_title': data[3],
                'phone_number': data[4],
                'image_url': data[5]
            }
            return jsonify({
                'employees': employee,
                'message': 'Employee found'
            })
        else:
            return jsonify({
                'message': 'Employee not found'
            })
    except Exception as ex:
        return jsonify({
            'message': 'Error'
        })
    
@app.route('/employee', methods=['POST'])   
def create_employee():
    try:
        cursor = conn.cursor()
        sql = '''INSERT INTO employee (id, first_name, last_name, job_title, phone_number, image_url) 
        VALUES (%s, %s, %s, %s, %s, %s)'''
        data = (
            request.json['id'],
            request.json['first_name'],
            request.json['last_name'],
            request.json['job_title'],
            request.json['phone_number'],
            request.json['image_url']
        )
        cursor.execute(sql, data)
        conn.commit()
        return jsonify({
            'message': 'Registered employee'
        })
    except Exception as ex:
        return jsonify({
            'message': 'Error'
        })
    
@app.route('/employee/<id>', methods=['DELETE'])   
def delete_employee(id):
        try:
            cursor = conn.cursor()
            sql = 'DELETE FROM employee WHERE id ={0}'.format(id)
            cursor.execute(sql)
            conn.commit()
            return jsonify({
                'message': 'Deleted employee'
            })
        except Exception as ex:
            return jsonify({
                'message': 'Error'
            })

@app.route('/employee/<id>', methods=['PUT'])          
def update_employee(id):
        try:
            cursor = conn.cursor()
            sql = '''UPDATE employee SET 
                first_name = %s, 
                last_name = %s, 
                job_title = %s, 
                phone_number = %s, 
                image_url = %s 
                WHERE id = %s'''

            data = (
                request.json['first_name'],
                request.json['last_name'],
                request.json['job_title'],
                request.json['phone_number'],
                request.json['image_url'],
                id
            )

            cursor.execute(sql, data)
            conn.commit()
            return jsonify({
                'message': 'updated employee'
            })
        except Exception as ex:
            return jsonify({
                'message': 'Error'
            })
    
def not_found_page(error):
    return '<h1>La pagina que intentas buscar no existe</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, not_found_page)
    app.run()