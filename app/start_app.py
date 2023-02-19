from app import app, db

@app.before_first_request
def create_tables():
    print("Creating database tables...")
    db.create_all()
    print("Done!")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
