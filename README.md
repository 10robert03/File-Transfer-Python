# Simple Python Socket Transfer

A lightweight, terminal-based file transfer system using raw TCP sockets. Developed to handle data transmission between a **Raspberry Pi** and a **Linux Laptop**.

## Features
- **Custom Handshake:** Uses a 1024-byte padded header to sync metadata (filename/size)
- **Auto-Reconnect:** The sender retries every 5 seconds if the receiver isn't ready.
- **Binary Mode:** Safe for all file types (images, binaries, text).

## Requirements
- Python 3.x
- Both devices must be in the same network.
