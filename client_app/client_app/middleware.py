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
                encrypted_body = cipher.encrypt(request.body)
                print("Encrypted data:", encrypted_body.decode())  # This will print in the browser console
                request.body = encrypted_body
            except Exception as e:
                print(f"Encryption error: {e}")
        response = self.get_response(request)

        return response
    
class DecryptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.body:
            try:
                # Decrypt incoming data
                decrypted_body = cipher.decrypt(request.body)
                print("Decrypted data:", decrypted_body.decode())  # Logs decrypted data in the server console
                request._body = decrypted_body  # Reassign the decrypted body for further processing
            except Exception as e:
                print(f"Decryption error: {e}")
        
        response = self.get_response(request)
        return response