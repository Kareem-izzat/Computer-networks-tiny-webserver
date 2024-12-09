# Computer-networks-tiny-webserver
# ENCS3320 - Computer Networks Project 1

## Overview

This project consists of three parts: socket programming with TCP clients and servers, HTTP web server creation, and handling various types of HTTP requests. The project uses socket programming  Python and follows standard RFC2616 guidelines for HTTP requests.

### Project Requirements

The project is divided into three parts:

### Part 1: Network Utilities

- **Ping**: Used to check connectivity to a device on the same network or external servers.
- **Tracert**: Tracks the route taken by packets to reach a destination.
- **Nslookup**: Queries DNS records for a domain name.
- **Telnet**: Used to test connectivity to remote servers.
  
You must:
1. Run these commands: 
    - `ping` (from a laptop to a smartphone)
    - `ping www.cornell.edu`
    - `tracert www.cornell.edu`
    - `nslookup www.cornell.edu`
2. Use Wireshark to capture DNS messages.
3. Provide screenshots of the results with explanations.

### Part 2: TCP Client and Server Application

- Implement a **TCP client** and **server** that communicates on port `9955`.
- The server should wait for a message and, if it matches any student ID from the group, it should:
    - Display a message about locking the screen in 10 seconds.
    - Lock the screen (Windows/Linux/Mac).
    - If the message is not a student ID, show an error message.

### Part 3: Simple HTTP Web Server

- Implement a simple **web server** listening on port `9966` to handle multiple requests.
- The server should serve content based on requests such as `/`, `/index.html`, `/main_en.html`, and `/ar`.
- Responses should be in HTML with appropriate `Content-Type`.
- Handle various types of content: HTML, CSS, images (PNG/JPG), and redirects.
- Provide 307 Temporary Redirect for specific URLs like `/cr`, `/so`, `/rt`.
- If the file doesn’t exist, return a custom 404 error page.

### System Features

- **Ping, Tracert, Nslookup, and Telnet** for networking testing.
- **TCP Client-Server** application for screen locking based on student IDs.
- **HTTP Web Server** for handling various HTTP requests and serving content.


