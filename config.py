API_KEY = "1234567890abcdef"
DB_PASSWORD = "mySuperSecretPassword"
def connect_to_db(password):
    if password == DB_PASSWORD:
        print("Connected to database successfully!")
    else:
        print("Failed to connect.")
def use_api(key):
    if key == API_KEY:
        print("API request successful!")
    else:
        print("Invalid API key.")
if __name__ == "__main__":
    connect_to_db("mySuperSecretPassword")
    use_api("1234567890abcdef")
