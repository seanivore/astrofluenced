import http.server
import socketserver
import webbrowser
import os

# Set the port
PORT = 8000

# Change to the directory containing the website files
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the server
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Server started at http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")

# Open the website in the default browser
webbrowser.open(f"http://localhost:{PORT}")

# Start the server
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped by user.")
    httpd.server_close() 