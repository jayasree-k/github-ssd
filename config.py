API_KEY = "ghp_abcd1234efgh5678ijkl9012mnop3456qrst"
DB_PASSWORD = "P@ssw0rd_123456789!"
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
    connect_to_db("mySuper_Secret_Password")
    use_api("1234567890_abcdef")
