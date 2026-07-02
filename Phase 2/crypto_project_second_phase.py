import random
import math
import json
import os
import socket
from datetime import datetime, timedelta
from crypto_project_first_phase import (
    CBC_mode_decryption,
    CBC_mode_encryption,
    int_to_binary_array,
    decode_binary_array_with_errors,
    EBC_mode_decryption,
    EBC_mode_encryption,
    OFB_mode_decryption,
    OFB_mode_encryption,
    CTR_mode_decryption,
    CTR_mode_encryption
)
# import crypto_project_first_phase
from crypto_project_first_phase import (
    string_to_padded_binary_array,
    binary_array_to_integer,
    binary_xor_array,
    pre_key1,
    pre_key2,
    key_gen1,
    key_gen2,
    key_gen3
)
import threading
import os
import time
import hashlib

# Directories
SHARED_DIR_CSR = "shared_csr"
SHARED_DIR_CERT = "shared_cert"
CLIENT_DIR = "client"
CA_DIR = "ca"

def is_prime_miller_rabin(n: int, k: int):
    """
    Perform the Miller-Rabin primality test on a number.

    :param n: The number to test for primality.
    :param k: The number of iterations of the test to perform.
    :return: True if n is probably prime, False if n is composite.
    """
    # Edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n - 1 as 2^r * d where d is odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations of the test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def generate_large_prime(bits: int, k: int):
    """
    Generate a large prime number with the specified bit length.

    :param bits: Number of bits for the prime number.
    :param k: Number of iterations for the Miller-Rabin test.
    :return: A large prime number.
    """
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << (bits - 1)) | 1  # Ensure it's odd and has the required bit length
        if is_prime_miller_rabin(candidate, k):
            return candidate

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int):
    """
    Extended Euclidean Algorithm to find gcd(a, b), and coefficients x, y such that ax + by = gcd(a, b).
    """
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def mod_inverse(e: int, phi: int) -> int:
    """Compute the modular inverse of e modulo phi using the extended Euclidean algorithm."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError(f"e ({e}) and phi ({phi}) are not coprime. Modular inverse does not exist.")
    return x % phi

def generate_rsa_key_pair():
    """
    Generate RSA keys and save them in proper PEM format.
    """
    print("Generating RSA Key Pair...")
    bits = 2048  # For real applications, this should be at least 2048 or higher.
    k = 40  # Number of iterations for primality test
    p = generate_large_prime(bits // 2, k)
    q = generate_large_prime(bits // 2, k)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Select a random e such that gcd(e, phi) = 1   
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    # Calculate the private key d
    d = mod_inverse(e, phi)

    # Create the keys
    private_key = {"p": p, "q": q, "n": n, "d": d, "e": e}
    public_key = {"n": n, "e": e}

    # Encode the keys to Base64
    private_key_encoded = base64.b64encode(json.dumps(private_key).encode()).decode()
    public_key_encoded = base64.b64encode(json.dumps(public_key).encode()).decode()

    # Save the keys in PEM format
    os.makedirs(CLIENT_DIR, exist_ok=True)
    with open(os.path.join(CLIENT_DIR, "client_private_key.pem"), "w") as f:
        f.write(f"-----BEGIN RSA PRIVATE KEY-----\n{private_key_encoded}\n-----END RSA PRIVATE KEY-----")

    with open(os.path.join(CLIENT_DIR, "client_public_key.pem"), "w") as f:
        f.write(f"-----BEGIN RSA PUBLIC KEY-----\n{public_key_encoded}\n-----END RSA PUBLIC KEY-----")

    print("RSA Key Pair Generated and Saved in PEM Format.")
    return private_key, public_key



def create_csr():
    print("Client: Creating CSR...")
    csr = {
        "common_name": "client1",
        "organization": "ExampleCorp",
        "organization_unit": "IT",
        "country": "US",
        "state": "California",
        "locality": "San Francisco",
        "email": "client1@example.com",
    }

    # Load the public key from the client's RSA public key file
    with open(os.path.join(CLIENT_DIR, "client_public_key.pem"), "r") as f:
        public_key_pem = f.read()
        csr["public_key"] = public_key_pem  # Include public key as PEM format

    # Save the CSR to the shared directory
    os.makedirs(SHARED_DIR_CSR, exist_ok=True)
    with open(os.path.join(SHARED_DIR_CSR, "csr.json"), "w") as f:
        json.dump(csr, f, indent=4)

    print("Client: CSR created and saved to shared directory.")


import base64

def generate_dsa_key_pair():
    """
    Generate DSA keys using manual prime generation and parameters.
    Save the private key and public key in proper PEM format.
    """
    print("Generating DSA Key Pair...")
    # First, generate q
    q = generate_large_prime(20, 40)

    # Then find p so that p = k * q + 1 is prime
    while True:
        k = random.randint(2, (1 << 8))  # For demo, pick a small search space
        p_candidate = k * q + 1
        if is_prime_miller_rabin(p_candidate, 40):
            p = p_candidate
            break

    h = random.randint(2, p - 2)
    # Compute g modulo p, not q
    g = pow(h, (p - 1) // q, p)

    x = random.randint(1, q - 1)        # Private key x
    y = pow(g, x, p)                    # Public key y = g^x mod p

    # Prepare the keys in dictionary format
    private_key = {"p": p, "q": q, "g": g, "x": x}
    public_key = {"p": p, "q": q, "g": g, "y": y}

    # Encode the keys to Base64
    private_key_encoded = base64.b64encode(json.dumps(private_key).encode()).decode()
    public_key_encoded = base64.b64encode(json.dumps(public_key).encode()).decode()

    # Save the keys in PEM format
    os.makedirs(CA_DIR, exist_ok=True)
    with open(os.path.join(CA_DIR, "ca_private_key.pem"), "w") as f:
        f.write(f"-----BEGIN DSA PRIVATE KEY-----\n{private_key_encoded}\n-----END DSA PRIVATE KEY-----")

    with open(os.path.join(CA_DIR, "ca_public_key.pem"), "w") as f:
        f.write(f"-----BEGIN DSA PUBLIC KEY-----\n{public_key_encoded}\n-----END DSA PUBLIC KEY-----")

    print("DSA Key Pair Generated and Saved in PEM Format.")
    return private_key, public_key

def sign_csr_and_generate_cert():
    """
    CA signs the CSR and generates the certificate using the updated PEM structure.
    """
    print("CA: Signing CSR and generating certificate...")

    # Load the CA private key from the PEM file
    with open(os.path.join(CA_DIR, "ca_private_key.pem"), "r") as f:
        private_key_pem = f.read().splitlines()[1]  # Extract the Base64 content
        ca_private_key = json.loads(base64.b64decode(private_key_pem))  # Decode and load JSON
        x = ca_private_key["x"]

    # Load the CA public key from the PEM file
    with open(os.path.join(CA_DIR, "ca_public_key.pem"), "r") as f:
        public_key_pem = f.read().splitlines()[1]  # Extract the Base64 content
        ca_public_key = json.loads(base64.b64decode(public_key_pem))  # Decode and load JSON
        y = ca_public_key["y"]
        p = ca_public_key["p"]
        q = ca_public_key["q"]
        g = ca_public_key["g"]

    # Load the CSR file
    with open(os.path.join(SHARED_DIR_CSR, "csr.json"), "r") as f:
        csr = json.load(f)

    # Extract the public key from the CSR
    csr_public_key_pem = csr["public_key"]  # Full PEM string
    hash_obj = hashlib.sha256(csr_public_key_pem.encode()).digest()  # Hash the PEM string directly
    hash_value = int.from_bytes(hash_obj, byteorder='big') % q  # Mod q


    # Generate the DSA signature
    k = random.randint(1, q - 1)
    k_inv = pow(k, -1, q)# Modular inverse of k mod q
    r = pow(g, k, p) % q
    s = (k_inv * (hash_value + x * r)) % q
    # Create the certificate JSON
    cert = {
        "certificate_id": "cert_001",
        "issued_to": csr["common_name"],
        "organization": csr["organization"],
        "issued_by": "Jocker",
        "public_key": csr["public_key"],
        "signature": {"r": r, "s": s},
        "validity_period": f"{datetime.now().date()} to {(datetime.now() + timedelta(days=365)).date()}",
    }


    # Save the certificate to the shared directory
    os.makedirs(SHARED_DIR_CERT, exist_ok=True)
    with open(os.path.join(SHARED_DIR_CERT, "cert.json"), "w") as f:
        json.dump(cert, f, indent=4)

    print("CA: Certificate signed and saved as 'cert.json'.")


def start_client():
    """Client communicates with the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("localhost", 8080))
        print("Client: Connected to the server.")

        # Server requests certification
        request = client_socket.recv(1024).decode()
        if request == "SEND_CERTIFICATE":
            print("Client: Received certificate request from server.")

            # Send CERT.json to the server
            with open(os.path.join(SHARED_DIR_CERT, "cert.json"), "r") as f:
                certificate = f.read()
            client_socket.sendall(certificate.encode())
            print("Client: Sent certificate to server.")

        # Receive symmetric key and mode (encrypted)
        response = client_socket.recv(4096).decode()
        if response == "INVALID":
            print("Client: Received INVALID certificate response. Closing connection.")
        else:
            encrypted_key, mode = json.loads(response)
            print("Client: Received encrypted symmetric key and mode.")

            # Decode and display the private key
            with open(os.path.join(CLIENT_DIR, "client_private_key.pem"), "r") as f:
                lines = f.read().splitlines()
                base64_content = lines[1]
                private_key = json.loads(base64.b64decode(base64_content))

            d = private_key["d"]
            n = private_key["n"]
            p = private_key["p"]
            q = private_key["q"]
            e = private_key["e"]

            # Decode and display the public key
            with open(os.path.join(CLIENT_DIR, "client_public_key.pem"), "r") as f:
                lines = f.read().splitlines()
                base64_content = lines[1]
                public_key = json.loads(base64.b64decode(base64_content))

            n_pub = public_key["n"]
            e_pub = public_key["e"]

            # Decrypt the symmetric key with the private key
            symmetric_key = pow(encrypted_key, d, n)
            print(f"this is the symmetric key: {int_to_binary_array(symmetric_key)}")
            print("***************************************************************************************************************************************************")
            # Encrypt a message using CBC mode and send to server
            iv = ["10101000"] * 16
            message = "There is nothing more to be said or to be done tonight, so hand me over my violin and let us try to forget for half an hour the miserable weather and the still more miserable ways of our fellowmen."
            encrypted_message = EBC_mode_encryption(message, int_to_binary_array(symmetric_key))
            print(f"this is the encrypted message in client: {decode_binary_array_with_errors(encrypted_message)}")
            print("****************************************************************************************************************************************************")
            client_socket.sendall(json.dumps(encrypted_message).encode())
            print("Client: Sent encrypted message to server.")
            print("****************************************************************************************************************************************************")

def start_server():
    """Server communicates with the client and CA."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("localhost", 8080))
        server_socket.listen(1)
        print("Server: Waiting for a client connection...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Server: Connected to client at {addr}.")
            conn.sendall("SEND_CERTIFICATE".encode())

            # Receive CERT.json from client
            certificate = conn.recv(4096).decode()
            print("Server: Received certificate from client.")
            # Validate certificate with CA
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ca_socket:
                ca_socket.connect(("localhost", 9090))
                ca_socket.sendall(certificate.encode())
                print("Server: Sent certificate to CA.")

                validation_result = ca_socket.recv(1024).decode()

            if validation_result == "VALID":
                print("Server: Certificate is valid.")

                # Generate symmetric key and encrypt with client's public RSA key
                symmetric_key = random.randint(1, 2**128)
                print(f"this in the symmetric_key: {symmetric_key}")
                print("**************************************************************************************************************************")
                with open(os.path.join(CLIENT_DIR, "client_public_key.pem"), "r") as f:
                    lines = f.read().splitlines()           # Split into lines
                    base64_content = lines[1]              # The second line
                    public_key = json.loads(base64.b64decode(base64_content))

                e = public_key["e"]
                n = public_key["n"]

                encrypted_key = pow(symmetric_key, e, n)

                conn.sendall(json.dumps([encrypted_key, "CBC"]).encode())
                print("Server: Sent encrypted symmetric key to client.")

                # Receive encrypted message and decrypt
                data = b''
                while True:
                    chunk = conn.recv(4096)
                    if not chunk:
                        break  # No more data, client closed
                    data += chunk
                # print(f"this is encrypted message length in server : {data}")
                encrypted_message = json.loads(data.decode())
                print(f"this is encrypted message in server: {encrypted_message}")
                print("************************************************************************************************************************************************")
                
                print(f"and this is len of that: {len(encrypted_message)}")
                print("*************************************************************************************************************************************************")
                iv = ["10101000"] * 16
                print(f"this is symmetric key binary: {int_to_binary_array(symmetric_key)}")
                print("*************************************************************************************************************************************************")
                decrypted_message = EBC_mode_decryption(
                    encrypted_message, int_to_binary_array(symmetric_key)
                )
                decrypted_message = decrypted_message[:len(decrypted_message)//2]
                print("server: binary of decrypted_message: ", decrypted_message)
                print("Server: Decrypted message:", decode_binary_array_with_errors(decrypted_message))
                print("this is len of decrypted message: ", len(decrypted_message))
                print("**************************************************************************************************************************************************")
                
            else:
                print("Server: Certificate is invalid.")
                conn.sendall("INVALID".encode())
def start_ca():
    """CA validates certificates."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ca_socket:
        ca_socket.bind(("localhost", 9090))
        ca_socket.listen(1)
        print("CA: Waiting for server connection...")

        conn, addr = ca_socket.accept()
        with conn:
            print(f"CA: Connected to server at {addr}.")

            # Receive the certificate from the server
            certificate = conn.recv(4096).decode()
            print("CA: Received certificate from server.")

            # Load the CA's public key
            with open(os.path.join(CA_DIR, "ca_public_key.pem"), "r") as f:
                pem_content = f.read().strip().splitlines()
                if len(pem_content) < 3 or not pem_content[0].startswith("-----BEGIN DSA PUBLIC KEY-----"):
                    raise ValueError("Invalid or malformed CA public key file.")
                public_key_pem = pem_content[1]  # Extract the Base64 content
                ca_public_key = json.loads(base64.b64decode(public_key_pem))  # Decode and load JSON

            # Ensure the public key components are integers
            y = int(ca_public_key["y"])
            p = int(ca_public_key["p"])
            q = int(ca_public_key["q"])
            g = int(ca_public_key["g"])

            # Parse the received certificate
            cert = json.loads(certificate)

            # Extract the signature and validate it
            r, s = cert["signature"]["r"], cert["signature"]["s"]

            # Decode the public key in the certificate
            cert_public_key_pem = cert["public_key"]  # Full PEM string
            hash_obj = hashlib.sha256(cert_public_key_pem.encode()).digest()  # Hash the PEM string directly
            hash_value = int.from_bytes(hash_obj, byteorder='big') % q  # Mod q

        
            # Validate the signature
            w = pow(s, -1, q)
            u1 = (hash_value * w) % q
            u2 = (r * w) % q
            v = ((pow(g, u1) % p * pow(y, u2) % p) % p)
            v = v % q
            

            if v == r:
                print("CA: Certificate is valid.")
                conn.sendall("VALID".encode())
            else:
                print("CA: Certificate is invalid.")
                conn.sendall("INVALID".encode())


import threading
import time
import os

# Ensure all directories exist
def setup_directories():
    os.makedirs("shared_csr", exist_ok=True)
    os.makedirs("shared_cert", exist_ok=True)
    os.makedirs("client", exist_ok=True)
    os.makedirs("ca", exist_ok=True)

# Offline steps
def offline_setup():
    print("--- Offline Setup ---")

    # Generate RSA key pair for the client
    private_key, public_key = generate_rsa_key_pair()
    print("Client: RSA key pair generated.")
    

    # Create a CSR and save it in the shared directory
    create_csr()
    print("Client: CSR created and saved to shared directory.")

    # Generate DSA key pair for the CA
    ca_private_key, ca_public_key = generate_dsa_key_pair()
    print("CA: DSA key pair generated.")

    # CA signs the CSR and generates a certificate
    sign_csr_and_generate_cert()
    print("CA: Certificate signed and saved to shared directory.")

# Online steps (testing client, server, and CA communication)
def online_test():
    print("\n--- Online Test ---")

    # Start CA server
    def run_ca():
        start_ca()

    ca_thread = threading.Thread(target=run_ca, daemon=True)
    ca_thread.start()

    # Start server
    def run_server():
        start_server()

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Allow CA and server to initialize
    time.sleep(2)

    # Start client
    def run_client():
        start_client()

    client_thread = threading.Thread(target=run_client, daemon=True)
    client_thread.start()

    # Wait for threads to complete
    client_thread.join()
    server_thread.join()
    ca_thread.join()

if __name__ == "__main__":
    # Step 1: Setup directories
    setup_directories()

    # Step 2: Run offline setup
    offline_setup()

    # Step 3: Test online communication
    online_test()
