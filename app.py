from app import create_app

# ceate the Flask application using our factory function
app = create_app()

# runs the application when this script is executed
if __name__ == "__main__":
    app.run(debug=True)