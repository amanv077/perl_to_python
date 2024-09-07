import socket
import urllib.parse

# Define the CGI configuration dictionary
cgi_config = {
    "name": "zfm.cgi",
    "url": "zfm.cgi",
    "uploadurl": "zfm.cgi"
}

# Set server name
hostname = socket.gethostname()
if '.' in hostname:
    hostname = hostname.split('.')[0]
cgi_config["servername"] = hostname

# Set mode
cgi_config["mode"] = "indiv"

# Set execution path based on local environment
cgi_config["exepath"] = "http://localhost/zfm/" if 'LOCAL' in globals() else "/zmf/"

# URL encode function
def url_encode(s):
    """Encode a string into URL format."""
    return urllib.parse.quote(s, safe='~()*!.\'')

# URL decode function
def url_decode(s):
    """Decode a URL-encoded string."""
    return urllib.parse.unquote(s)

# Example usage
if __name__ == "__main__":
    # Example of encoding and decoding
    original_string = "Hello World! @Python"
    encoded_string = url_encode(original_string)
    decoded_string = url_decode(encoded_string)
    
    print(f"Original: {original_string}")
    print(f"Encoded: {encoded_string}")
    print(f"Decoded: {decoded_string}")
