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
                request.body = cipher.decrypt(request.body)
            except Exception:
                pass
        response = self.get_response(request)

        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8001"  # Client app URL
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"

        if request.method == "OPTIONS":
            response.status_code = 200

        return response

