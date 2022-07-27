from imp import reload
from src.app import app

if __name__ == "__main__":
    app.run(reload=True)
    