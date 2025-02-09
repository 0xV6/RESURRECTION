# # import traceback
# #
# # from flask import render_template
# # import mysql.connector
# #
# # from flask import Flask, request, jsonify
# #
# # from flask_cors import CORS
# #
# #
# # app = Flask(__name__)
# #
# # CORS(app, resources={r"/*": {"origins": "*"}})
# #
# # # Database Connection
# # def get_db_connection():
# #     return mysql.connector.connect(
# #         host="localhost",
# #         user="root",
# #         password="root",
# #         database="resurrection_blood_donation",
# #         port = 3308
# #     )
# #
# # # User Registration Endpoint
# # @app.route('/register_user', methods=['POST'])
# # def register_user():
# #     data = request.json
# #     try:
# #         conn = get_db_connection()
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO users
# #         (full_name, phone_number, email, address, blood_type)
# #         VALUES (%s, %s, %s, %s, %s)
# #         """
# #         values = (
# #             data['full_name'],
# #             data['phone_number'],
# #             data['email'],
# #             data['address'],
# #             data['blood_type']
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({"status": "success", "message": "User registered successfully"}), 201
# #
# #     except mysql.connector.Error as err:
# #         return jsonify({"status": "error", "message": str(err)}), 400
# #
# #     finally:
# #         cursor.close()
# #         conn.close()
# #
# # @app.route('/register_hospital', methods=['POST', 'OPTIONS'])
# # def register_hospital():
# #     # Handle preflight CORS request
# #     if request.method == 'OPTIONS':
# #         return jsonify({"status": "success"}), 200
# #
# #     try:
# #         # Print incoming data for debugging
# #         print("Received Hospital Registration Data:", request.json)
# #
# #         data = request.json
# #         conn = get_db_connection()
# #
# #         if not conn:
# #             return jsonify({"status": "error", "message": "Database connection failed"}), 500
# #
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO hospitals
# #         (hospital_name, hospital_address, hospital_phone, hospital_email)
# #         VALUES (%s, %s, %s, %s)
# #         """
# #         values = (
# #             data.get('hospital_name', ''),
# #             data.get('hospital_address', ''),
# #             data.get('hospital_phone', ''),
# #             data.get('hospital_email', '')
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({"status": "success", "message": "Hospital registered successfully"}), 201
# #
# #     except Exception as e:
# #         # Detailed error logging
# #         print(f"Hospital Registration Error: {e}")
# #         print(traceback.format_exc())
# #         return jsonify({"status": "error", "message": str(e)}), 400
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # @app.route('/create_post', methods=['POST', 'OPTIONS'])
# # def create_post():
# #     # Handle preflight CORS request
# #     if request.method == 'OPTIONS':
# #         return jsonify({"status": "success"}), 200
# #
# #     try:
# #         # Print incoming data for debugging
# #         print("Received Blood Post Data (Raw):", request.data)
# #         print("Received Blood Post Data (JSON):", request.json)
# #
# #         data = request.json
# #
# #         # Validate incoming data
# #         if not data:
# #             return jsonify({
# #                 "status": "error",
# #                 "message": "No data received",
# #                 "details": "Request body is empty"
# #             }), 400
# #
# #         # Validate required fields
# #         required_fields = ['name', 'phone', 'address', 'bloodType']
# #         for field in required_fields:
# #             if field not in data or not data[field]:
# #                 return jsonify({
# #                     "status": "error",
# #                     "message": f"Missing required field: {field}"
# #                 }), 400
# #
# #         conn = get_db_connection()
# #
# #         if not conn:
# #             return jsonify({
# #                 "status": "error",
# #                 "message": "Database connection failed"
# #             }), 500
# #
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO blood_posts
# #         (name, phone, address, blood_type, urgency)
# #         VALUES (%s, %s, %s, %s, %s)
# #         """
# #         values = (
# #             data['name'],
# #             data['phone'],
# #             data['address'],
# #             data['bloodType'],
# #             data['urgency']
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({
# #             "status": "success",
# #             "message": "Blood post created successfully",
# #             "post_id": cursor.lastrowid
# #         }), 201
# #
# #     except Exception as e:
# #         # Detailed error logging
# #         print(f"Create Post Error: {e}")
# #         print(traceback.format_exc())
# #         return jsonify({
# #             "status": "error",
# #             "message": "Internal server error",
# #             "details": str(e)
# #         }), 500
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# # # Donation Offer Endpoint
# # @app.route('/donate_blood', methods=['POST'])
# # def donate_blood():
# #     data = request.json
# #     try:
# #         conn = get_db_connection()
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO donation_offers
# #         (blood_type, last_donation_date, medical_conditions, availability, contact)
# #         VALUES (%s, %s, %s, %s, %s)
# #         """
# #         values = (
# #             data['bloodType'],
# #             data.get('lastDonationDate'),
# #             data.get('medicalConditions'),
# #             data.get('availability'),
# #             data['contact']
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({"status": "success", "message": "Donation offer submitted successfully"}), 201
# #
# #     except mysql.connector.Error as err:
# #         return jsonify({"status": "error", "message": str(err)}), 400
# #
# #     finally:
# #         cursor.close()
# #         conn.close()
# #
# # @app.route('/get_blood_posts', methods=['GET'])
# # def get_blood_posts():
# #     try:
# #         conn = get_db_connection()
# #
# #         if not conn:
# #             return jsonify({
# #                 "status": "error",
# #                 "message": "Database connection failed"
# #             }), 500
# #
# #         cursor = conn.cursor(dictionary=True)
# #
# #         query = """
# #         SELECT id, name, phone, address, blood_type, urgency, created_at
# #         FROM blood_posts
# #         ORDER BY urgency DESC;
# #         """
# #
# #         cursor.execute(query)
# #         posts = cursor.fetchall()
# #
# #         return jsonify({
# #             "status": "success",
# #             "posts": posts
# #         }), 200
# #
# #     except Exception as e:
# #         print(f"Fetch Posts Error: {e}")
# #         print(traceback.format_exc())
# #         return jsonify({
# #             "status": "error",
# #             "message": "Internal server error",
# #             "details": str(e)
# #         }), 500
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
#
#
#
#
# # import traceback
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import mysql.connector
# # from datetime import datetime
# #
# # app = Flask(__name__)
# # CORS(app, resources={r"/*": {"origins": "*"}})
# #
# # # Database Connection
# # def get_db_connection():
# #     return mysql.connector.connect(
# #         host="localhost",
# #         user="root",
# #         password="root",
# #         database="resurrection_blood_donation",
# #         port=3308
# #     )
# #
# # # User Registration Endpoint
# # @app.route('/register_user', methods=['POST'])
# # def register_user():
# #     data = request.json
# #     try:
# #         conn = get_db_connection()
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO users
# #         (full_name, phone_number, email, address, blood_type)
# #         VALUES (%s, %s, %s, %s, %s)
# #         """
# #         values = (
# #             data['full_name'],
# #             data['phone_number'],
# #             data['email'],
# #             data['address'],
# #             data['blood_type']
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({"status": "success", "message": "User registered successfully"}), 201
# #
# #     except mysql.connector.Error as err:
# #         return jsonify({"status": "error", "message": str(err)}), 400
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # @app.route('/register_hospital', methods=['POST', 'OPTIONS'])
# # def register_hospital():
# #     if request.method == 'OPTIONS':
# #         return jsonify({"status": "success"}), 200
# #
# #     try:
# #         print("Received Hospital Registration Data:", request.json)
# #         data = request.json
# #         conn = get_db_connection()
# #
# #         if not conn:
# #             return jsonify({"status": "error", "message": "Database connection failed"}), 500
# #
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO hospitals
# #         (hospital_name, hospital_address, hospital_phone, hospital_email)
# #         VALUES (%s, %s, %s, %s)
# #         """
# #         values = (
# #             data.get('hospital_name', ''),
# #             data.get('hospital_address', ''),
# #             data.get('hospital_phone', ''),
# #             data.get('hospital_email', '')
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({"status": "success", "message": "Hospital registered successfully"}), 201
# #
# #     except Exception as e:
# #         print(f"Hospital Registration Error: {e}")
# #         print(traceback.format_exc())
# #         return jsonify({"status": "error", "message": str(e)}), 400
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # @app.route('/create_post', methods=['POST', 'OPTIONS'])
# # def create_post():
# #     if request.method == 'OPTIONS':
# #         return jsonify({"status": "success"}), 200
# #
# #     try:
# #         print("Received Blood Post Data:", request.json)
# #         data = request.json
# #
# #         if not data:
# #             return jsonify({
# #                 "status": "error",
# #                 "message": "No data received"
# #             }), 400
# #
# #         # Updated required fields to include urgency
# #         required_fields = ['name', 'phone', 'address', 'blood_type', 'urgency']
# #         for field in required_fields:
# #             if field not in data or not data[field]:
# #                 return jsonify({
# #                     "status": "error",
# #                     "message": f"Missing required field: {field}"
# #                 }), 400
# #
# #         conn = get_db_connection()
# #         if not conn:
# #             return jsonify({
# #                 "status": "error",
# #                 "message": "Database connection failed"
# #             }), 500
# #
# #         cursor = conn.cursor()
# #
# #         # Updated query to include urgency
# #         query = """
# #         INSERT INTO blood_posts
# #         (name, phone, address, blood_type, urgency, created_at)
# #         VALUES (%s, %s, %s, %s, %s, %s)
# #         """
# #         values = (
# #             data['name'],
# #             data['phone'],
# #             data['address'],
# #             data['blood_type'],
# #             data['urgency'],
# #             datetime.now()
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({
# #             "status": "success",
# #             "message": "Blood post created successfully",
# #             "post_id": cursor.lastrowid
# #         }), 201
# #
# #     except Exception as e:
# #         print(f"Create Post Error: {e}")
# #         print(traceback.format_exc())
# #         return jsonify({
# #             "status": "error",
# #             "message": "Internal server error",
# #             "details": str(e)
# #         }), 500
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # @app.route('/donate_blood', methods=['POST'])
# # def donate_blood():
# #     data = request.json
# #     try:
# #         conn = get_db_connection()
# #         cursor = conn.cursor()
# #
# #         query = """
# #         INSERT INTO donation_offers
# #         (blood_type, last_donation_date, medical_conditions, availability, contact)
# #         VALUES (%s, %s, %s, %s, %s)
# #         """
# #         values = (
# #             data['bloodType'],
# #             data.get('lastDonationDate'),
# #             data.get('medicalConditions'),
# #             data.get('availability'),
# #             data['contact']
# #         )
# #
# #         cursor.execute(query, values)
# #         conn.commit()
# #
# #         return jsonify({"status": "success", "message": "Donation offer submitted successfully"}), 201
# #
# #     except mysql.connector.Error as err:
# #         return jsonify({"status": "error", "message": str(err)}), 400
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # @app.route('/get_blood_posts', methods=['GET'])
# # def get_blood_posts():
# #     try:
# #         conn = get_db_connection()
# #         if not conn:
# #             return jsonify({
# #                 "status": "error",
# #                 "message": "Database connection failed"
# #             }), 500
# #
# #         cursor = conn.cursor(dictionary=True)
# #
# #         # Updated query to order by urgency priority and creation date
# #         query = """
# #         SELECT id, name, phone, address, blood_type, urgency, created_at
# #         FROM blood_posts
# #         ORDER BY
# #             CASE urgency
# #                 WHEN 'critical' THEN 1
# #                 WHEN 'urgent' THEN 2
# #                 WHEN 'normal' THEN 3
# #             END,
# #             created_at DESC;
# #         """
# #
# #         cursor.execute(query)
# #         posts = cursor.fetchall()
# #
# #         # Convert datetime objects to strings for JSON serialization
# #         for post in posts:
# #             if 'created_at' in post and post['created_at']:
# #                 post['created_at'] = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
# #
# #         return jsonify({
# #             "status": "success",
# #             "posts": posts
# #         }), 200
# #
# #     except Exception as e:
# #         print(f"Fetch Posts Error: {e}")
# #         print(traceback.format_exc())
# #         return jsonify({
# #             "status": "error",
# #             "message": "Internal server error",
# #             "details": str(e)
# #         }), 500
# #
# #     finally:
# #         if 'cursor' in locals():
# #             cursor.close()
# #         if 'conn' in locals():
# #             conn.close()
# #
# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)
#
#
# import traceback
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import mysql.connector
# from datetime import datetime
#
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
#
# # Constants
# CURRENT_TIME = "2025-01-20 06:18:28"  # Fixed timestamp as per requirement
# CURRENT_USER = "DeepanshuSharma05"    # Fixed user as per requirement
#
# # Database Connection
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root",
#         database="resurrection_blood_donation",
#         port=3308
#     )
#
# def get_current_time():
#     return CURRENT_TIME
#
# def get_current_user():
#     return CURRENT_USER
#
# @app.route('/system_info', methods=['GET'])
# def system_info():
#     return jsonify({
#         'current_time_utc': get_current_time(),
#         'current_user': get_current_user()
#     })
#
# # User Registration Endpoint
# @app.route('/register_user', methods=['POST'])
# def register_user():
#     data = request.json
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#
#         query = """
#         INSERT INTO users
#         (full_name, phone_number, email, address, blood_type)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         values = (
#             data['full_name'],
#             data['phone_number'],
#             data['email'],
#             data['address'],
#             data['blood_type']
#         )
#
#         cursor.execute(query, values)
#         conn.commit()
#
#         return jsonify({"status": "success", "message": "User registered successfully"}), 201
#
#     except mysql.connector.Error as err:
#         return jsonify({"status": "error", "message": str(err)}), 400
#
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()
#
# @app.route('/register_hospital', methods=['POST', 'OPTIONS'])
# def register_hospital():
#     if request.method == 'OPTIONS':
#         return jsonify({"status": "success"}), 200
#
#     try:
#         print("Received Hospital Registration Data:", request.json)
#         data = request.json
#         conn = get_db_connection()
#
#         if not conn:
#             return jsonify({"status": "error", "message": "Database connection failed"}), 500
#
#         cursor = conn.cursor()
#
#         query = """
#         INSERT INTO hospitals
#         (hospital_name, hospital_address, hospital_phone, hospital_email)
#         VALUES (%s, %s, %s, %s)
#         """
#         values = (
#             data.get('hospital_name', ''),
#             data.get('hospital_address', ''),
#             data.get('hospital_phone', ''),
#             data.get('hospital_email', '')
#         )
#
#         cursor.execute(query, values)
#         conn.commit()
#
#         return jsonify({"status": "success", "message": "Hospital registered successfully"}), 201
#
#     except Exception as e:
#         print(f"Hospital Registration Error: {e}")
#         print(traceback.format_exc())
#         return jsonify({"status": "error", "message": str(e)}), 400
#
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()
#
# @app.route('/create_post', methods=['POST', 'OPTIONS'])
# def create_post():
#     if request.method == 'OPTIONS':
#         return jsonify({"status": "success"}), 200
#
#     try:
#         print("Received Blood Post Data:", request.json)
#         data = request.json
#
#         if not data:
#             return jsonify({
#                 "status": "error",
#                 "message": "No data received"
#             }), 400
#
#         required_fields = ['name', 'phone', 'address', 'blood_type', 'urgency']
#         for field in required_fields:
#             if field not in data or not data[field]:
#                 return jsonify({
#                     "status": "error",
#                     "message": f"Missing required field: {field}"
#                 }), 400
#
#         conn = get_db_connection()
#         cursor = conn.cursor()
#
#         query = """
#         INSERT INTO blood_posts
#         (name, phone, address, blood_type, urgency, created_at)
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """
#         values = (
#             data['name'],
#             data['phone'],
#             data['address'],
#             data['blood_type'],
#             data['urgency'],
#             get_current_time()
#         )
#
#         cursor.execute(query, values)
#         conn.commit()
#
#         return jsonify({
#             "status": "success",
#             "message": "Blood post created successfully",
#             "post_id": cursor.lastrowid
#         }), 201
#
#     except Exception as e:
#         print(f"Create Post Error: {e}")
#         print(traceback.format_exc())
#         return jsonify({
#             "status": "error",
#             "message": "Internal server error",
#             "details": str(e)
#         }), 500
#
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()
#
#
# @app.route('/donate_blood', methods=['POST'])
# def donate_blood():
#     data = request.json
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#
#         query = """
#         INSERT INTO donation_offers
#         (blood_type, last_donation_date, medical_conditions, availability, contact)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         values = (
#             data['bloodType'],
#             data.get('lastDonationDate'),
#             data.get('medicalConditions'),
#             data.get('availability'),
#             data['contact']
#         )
#
#         cursor.execute(query, values)
#         conn.commit()
#
#         return jsonify({"status": "success", "message": "Donation offer submitted successfully"}), 201
#
#     except mysql.connector.Error as err:
#         return jsonify({"status": "error", "message": str(err)}), 400
#
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()
#
#
# @app.route('/get_donation_offers', methods=['GET'])
# def get_donation_offers():
#     try:
#         connection = get_db_connection()
#         if not connection:
#             return jsonify({'error': 'Database connection failed'}), 500
#
#         cursor = connection.cursor(dictionary=True)
#         blood_type = request.args.get('blood_type', '')
#         sort = request.args.get('sort', 'newest')
#
#         query = "SELECT * FROM donation_offers"
#         params = []
#
#         if blood_type:
#             query += " WHERE blood_type = %s"
#             params.append(blood_type)
#
#         query += " ORDER BY created_at " + ('DESC' if sort == 'newest' else 'ASC')
#
#         cursor.execute(query, params)
#         results = cursor.fetchall()
#
#         for row in results:
#             if row.get('last_donation_date'):
#                 row['last_donation_date'] = row['last_donation_date'].strftime('%Y-%m-%d')
#             if row.get('created_at'):
#                 row['created_at'] = row['created_at'].strftime('%Y-%m-%d %H:%M:%S')
#
#         return jsonify(results)
#
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'connection' in locals():
#             connection.close()
#
# @app.route('/submit_donation_offer', methods=['POST'])
# def submit_donation_offer():
#     try:
#         data = request.get_json()
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
#
#         connection = get_db_connection()
#         cursor = connection.cursor()
#
#         query = """
#         INSERT INTO donation_offers
#         (blood_type, last_donation_date, medical_conditions, availability, contact, created_at)
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """
#
#         values = (
#             data.get('blood_type'),
#             data.get('last_donation_date'),
#             data.get('medical_conditions'),
#             data.get('availability'),
#             data.get('contact'),
#             get_current_time()
#         )
#
#         cursor.execute(query, values)
#         connection.commit()
#
#         return jsonify({
#             'message': 'Donation offer submitted successfully',
#             'timestamp': get_current_time()
#         }), 201
#
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'connection' in locals():
#             connection.close()
#
# @app.route('/get_blood_posts', methods=['GET'])
# def get_blood_posts():
#     try:
#         conn = get_db_connection()
#         if not conn:
#             return jsonify({
#                 "status": "error",
#                 "message": "Database connection failed"
#             }), 500
#
#         cursor = conn.cursor(dictionary=True)
#
#         query = """
#         SELECT id, name, phone, address, blood_type, urgency, created_at
#         FROM blood_posts
#         ORDER BY
#             CASE urgency
#                 WHEN 'critical' THEN 1
#                 WHEN 'urgent' THEN 2
#                 WHEN 'normal' THEN 3
#             END,
#             created_at DESC;
#         """
#
#         cursor.execute(query)
#         posts = cursor.fetchall()
#
#         for post in posts:
#             if 'created_at' in post and post['created_at']:
#                 post['created_at'] = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
#
#         return jsonify({
#             "status": "success",
#             "posts": posts
#         }), 200
#
#     except Exception as e:
#         print(f"Fetch Posts Error: {e}")
#         print(traceback.format_exc())
#         return jsonify({
#             "status": "error",
#             "message": "Internal server error",
#             "details": str(e)
#         }), 500
#
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'conn' in locals():
#             conn.close()
#
# @app.route('/user_donation_history', methods=['GET'])
# def user_donation_history():
#     try:
#         user_contact = request.args.get('contact')
#         if not user_contact:
#             return jsonify({'error': 'Contact number is required'}), 400
#
#         connection = get_db_connection()
#         cursor = connection.cursor(dictionary=True)
#
#         query = """
#         SELECT * FROM donation_offers
#         WHERE contact = %s
#         ORDER BY created_at DESC
#         """
#
#         cursor.execute(query, (user_contact,))
#         results = cursor.fetchall()
#
#         for row in results:
#             if row.get('last_donation_date'):
#                 row['last_donation_date'] = row['last_donation_date'].strftime('%Y-%m-%d')
#             if row.get('created_at'):
#                 row['created_at'] = row['created_at'].strftime('%Y-%m-%d %H:%M:%S')
#
#         return jsonify(results)
#
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         if 'cursor' in locals():
#             cursor.close()
#         if 'connection' in locals():
#             connection.close()
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
#
#
#






import traceback
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import mysql.connector
from datetime import datetime
import os

app = Flask(__name__,
            static_folder='.idea/dist/static',  # Update this path if you have static files
            template_folder='.idea/dist'        # Set template folder to .idea/dist
            )
CORS(app, resources={r"/*": {"origins": "*"}})

# Constants
CURRENT_TIME = "2025-01-20 06:44:26"  # Updated timestamp
CURRENT_USER = "DeepanshuSharma05"

# Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="resurrection_blood_donation",
        port=3308
    )

def get_current_time():
    return CURRENT_TIME

def get_current_user():
    return CURRENT_USER

# Serve static files from .idea/dist
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.idea/dist', path)

# Main routes
@app.route('/')
def index():
    return send_from_directory('.idea/dist', 'index.html')

@app.route('/history')
def history():
    return send_from_directory('.idea/dist', 'history.html')

@app.route('/appointment')
def appointment():
    return send_from_directory('.idea/dist', 'appointment.html')

@app.route('/form')
def form():
    return send_from_directory('.idea/dist', 'form.html')

@app.route('/system_info', methods=['GET'])
def system_info():
    return jsonify({
        'current_time_utc': get_current_time(),
        'current_user': get_current_user()
    })

# User Registration Endpoint
@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO users
        (full_name, phone_number, email, address, blood_type)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            data['full_name'],
            data['phone_number'],
            data['email'],
            data['address'],
            data['blood_type']
        )

        cursor.execute(query, values)
        conn.commit()

        return jsonify({"status": "success", "message": "User registered successfully"}), 201

    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)}), 400

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/register_hospital', methods=['POST', 'OPTIONS'])
def register_hospital():
    if request.method == 'OPTIONS':
        return jsonify({"status": "success"}), 200

    try:
        print("Received Hospital Registration Data:", request.json)
        data = request.json
        conn = get_db_connection()

        if not conn:
            return jsonify({"status": "error", "message": "Database connection failed"}), 500

        cursor = conn.cursor()

        query = """
        INSERT INTO hospitals
        (hospital_name, hospital_address, hospital_phone, hospital_email)
        VALUES (%s, %s, %s, %s)
        """
        values = (
            data.get('hospital_name', ''),
            data.get('hospital_address', ''),
            data.get('hospital_phone', ''),
            data.get('hospital_email', '')
        )

        cursor.execute(query, values)
        conn.commit()

        return jsonify({"status": "success", "message": "Hospital registered successfully"}), 201

    except Exception as e:
        print(f"Hospital Registration Error: {e}")
        print(traceback.format_exc())
        return jsonify({"status": "error", "message": str(e)}), 400

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/create_post', methods=['POST', 'OPTIONS'])
def create_post():
    if request.method == 'OPTIONS':
        return jsonify({"status": "success"}), 200

    try:
        print("Received Blood Post Data:", request.json)
        data = request.json

        if not data:
            return jsonify({
                "status": "error",
                "message": "No data received"
            }), 400

        required_fields = ['name', 'phone', 'address', 'blood_type', 'urgency']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO blood_posts
        (name, phone, address, blood_type, urgency, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data['name'],
            data['phone'],
            data['address'],
            data['blood_type'],
            data['urgency'],
            get_current_time()
        )

        cursor.execute(query, values)
        conn.commit()

        return jsonify({
            "status": "success",
            "message": "Blood post created successfully",
            "post_id": cursor.lastrowid
        }), 201

    except Exception as e:
        print(f"Create Post Error: {e}")
        print(traceback.format_exc())
        return jsonify({
            "status": "error",
            "message": "Internal server error",
            "details": str(e)
        }), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


@app.route('/donate_blood', methods=['POST'])
def donate_blood():
    data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO donation_offers
        (blood_type, last_donation_date, medical_conditions, availability, contact)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            data['bloodType'],
            data.get('lastDonationDate'),
            data.get('medicalConditions'),
            data.get('availability'),
            data['contact']
        )

        cursor.execute(query, values)
        conn.commit()

        return jsonify({"status": "success", "message": "Donation offer submitted successfully"}), 201

    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)}), 400

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


@app.route('/get_donation_offers', methods=['GET'])
def get_donation_offers():
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500

        cursor = connection.cursor(dictionary=True)
        blood_type = request.args.get('blood_type', '')
        sort = request.args.get('sort', 'newest')

        query = "SELECT * FROM donation_offers"
        params = []

        if blood_type:
            query += " WHERE blood_type = %s"
            params.append(blood_type)

        query += " ORDER BY created_at " + ('DESC' if sort == 'newest' else 'ASC')

        cursor.execute(query, params)
        results = cursor.fetchall()

        for row in results:
            if row.get('last_donation_date'):
                row['last_donation_date'] = row['last_donation_date'].strftime('%Y-%m-%d')
            if row.get('created_at'):
                row['created_at'] = row['created_at'].strftime('%Y-%m-%d %H:%M:%S')

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

@app.route('/submit_donation_offer', methods=['POST'])
def submit_donation_offer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO donation_offers
        (blood_type, last_donation_date, medical_conditions, availability, contact, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data.get('blood_type'),
            data.get('last_donation_date'),
            data.get('medical_conditions'),
            data.get('availability'),
            data.get('contact'),
            get_current_time()
        )

        cursor.execute(query, values)
        connection.commit()

        return jsonify({
            'message': 'Donation offer submitted successfully',
            'timestamp': get_current_time()
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

@app.route('/get_blood_posts', methods=['GET'])
def get_blood_posts():
    try:
        conn = get_db_connection()
        if not conn:
            return jsonify({
                "status": "error",
                "message": "Database connection failed"
            }), 500

        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT id, name, phone, address, blood_type, urgency, created_at
        FROM blood_posts
        ORDER BY
            CASE urgency
                WHEN 'critical' THEN 1
                WHEN 'urgent' THEN 2
                WHEN 'normal' THEN 3
            END,
            created_at DESC;
        """

        cursor.execute(query)
        posts = cursor.fetchall()

        for post in posts:
            if 'created_at' in post and post['created_at']:
                post['created_at'] = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')

        return jsonify({
            "status": "success",
            "posts": posts
        }), 200

    except Exception as e:
        print(f"Fetch Posts Error: {e}")
        print(traceback.format_exc())
        return jsonify({
            "status": "error",
            "message": "Internal server error",
            "details": str(e)
        }), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/user_donation_history', methods=['GET'])
def user_donation_history():
    try:
        user_contact = request.args.get('contact')
        if not user_contact:
            return jsonify({'error': 'Contact number is required'}), 400

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT * FROM donation_offers
        WHERE contact = %s
        ORDER BY created_at DESC
        """

        cursor.execute(query, (user_contact,))
        results = cursor.fetchall()

        for row in results:
            if row.get('last_donation_date'):
                row['last_donation_date'] = row['last_donation_date'].strftime('%Y-%m-%d')
            if row.get('created_at'):
                row['created_at'] = row['created_at'].strftime('%Y-%m-%d %H:%M:%S')

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"status": "error", "message": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

