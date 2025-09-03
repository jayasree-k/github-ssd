GITHUB_TOKEN = "ghp_abcd1234efgh5678ijkl9012mnop3456qrst"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def use_github_token(token):
    if token == GITHUB_TOKEN:
        print("Authenticated with GitHub!")
    else:
        print("Invalid GitHub token.")
        
def connect_to_aws(access_key, secret_key):
    if access_key == AWS_ACCESS_KEY_ID and secret_key == AWS_SECRET_ACCESS_KEY:
        print("Connected to AWS successfully!")
    else:
        print("AWS authentication failed.")

if __name__ == "__main__":
    use_github_token(GITHUB_TOKEN)
    connect_to_aws(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
