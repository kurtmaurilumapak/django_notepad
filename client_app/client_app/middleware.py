from cryptography.fernet import Fernet

# Generate and store a secure key (reuse the same key in the server for decryption)
SECRET_KEY = b'ch7JZnJw1fVVFYXH4eSzlAXnQL8uPYTYjMyJ7ELsVq4='  # Replace with your own key
cipher = Fernet(SECRET_KEY)

class EncryptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.body:
            try:
                # Encrypt outgoing data
                request.body = cipher.encrypt(request.body)
            except Exception:
                pass
        response = self.get_response(request)

        return response
