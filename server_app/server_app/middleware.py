from cryptography.fernet import Fernet

SECRET_KEY = b'ch7JZnJw1fVVFYXH4eSzlAXnQL8uPYTYjMyJ7ELsVq4='  # Same key as in the client
cipher = Fernet(SECRET_KEY)

class DecryptionAndCORSHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.body:
            try:
                # Decrypt incoming data
                decrypted_body = cipher.decrypt(request.body)
                request.body = decrypted_body
            except Exception as e:
                print(f"Decryption error: {e}")

        response = self.get_response(request)

        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"  # Client app URL
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

        if request.method == "OPTIONS":
            response.status_code = 200

        return response

class EncryptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.body:
            try:
                # Encrypt outgoing data
                encrypted_body = cipher.encrypt(request.body)
                print("Encrypted data:", encrypted_body.decode())  # This will print in the browser console
                request.body = encrypted_body
            except Exception as e:
                print(f"Encryption error: {e}")
        response = self.get_response(request)

        return response