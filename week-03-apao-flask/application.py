from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def show_application_form():
    """Show the application form page."""

    return render_template("application-form.html")


@app.route("/application", methods=['POST', 'GET'])
def show_submitted_application():
    """Acknowledge receipt of application form and show details on page."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary_req = request.form.get("salaryrequirement")
    position_type = request.form.get("positiontype")

    return render_template("application-response.html",
                           firstname=first_name,
                           lastname=last_name,
                           salaryreq=salary_req,
                           positiontype=position_type)

if __name__ == "__main__":
    app.run(debug=True)
