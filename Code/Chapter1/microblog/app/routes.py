from app import app

@app.route('/')
@app.route('/')
def index():
    return "Hello, World"
