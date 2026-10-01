# HTTP Server in Python

A small HTTP server built with Python's standard `socket` library.

## What it does

The server listens on `127.0.0.1:8080`, accepts browser connections, prints
the raw HTTP request, and responds with a simple HTML page.

## Requirements

- Python 3

## Run it

From this project directory:

```powershell
python server.py
```

Then open <http://127.0.0.1:8080> in a browser. Press `Ctrl+C` in the
terminal to stop the server.

## How the server works

1. Create a TCP socket.
2. Bind it to `127.0.0.1:8080`.
3. Listen for incoming connections.
4. Accept one client connection at a time.
5. Read the request and send an HTTP response.
6. Close the client connection.

This is a learning project, not a production web server.
