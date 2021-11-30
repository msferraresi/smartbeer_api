import os
from app import create_app

app = create_app(os.getenv("APP_ENV", "development"))
#app = create_app(os.getenv("APP_ENV", "production"))

if __name__ == "__main__":  # Only in dev
    app.run()  # nosec
