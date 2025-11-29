from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Supabase configuration
SUPABASE_URL = "https://gabhllkyuzfptohcsjgr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdhYmhsbGt5dXpmcHRvaGNzamdyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIyNjE1MjQsImV4cCI6MjA3NzgzNzUyNH0.8dGc7LIg7oAJI4IxWv4cHNsOHA8p4zlkBG1MF9cTPzk"

@app.route('/', methods=['GET'])
def show_booking_form():
    return render_template("booking.html")

@app.route('/book', methods=['POST'])
def handle_booking():
    data = request.form.to_dict()
    print("Received form data:", data)

    payload = {
        "pet_name": data.get("pet_name"),
        "service_type": data.get("service_type"),
        "appointment_date": data.get("appointment_date"),
        "appointment_time": data.get("appointment_time"),
        "notes": data.get("notes")
    }

    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/Petservices",
        headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        },
        json=payload
    )

    print("Supabase response:", response.status_code)
    print("Response body:", response.text)

    # Redirect to index page after booking
    return redirect(url_for('show_home'))

@app.route('/index', methods=['GET'])
def show_home():
    return render_template("index.html")

@app.route('/appointment', methods=['GET'])
def show_appointment():
    return render_template("appointment.html")
if __name__ == '__main__':
    app.run(debug=True)