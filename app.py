#!/usr/bin/env python3

import time
import os

def main():
    print("🐳 Docker Python App")
    print(f"📅 Current time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🖥️  Hostname: {os.uname().nodename}")
    print(f"👤 Running as user: {os.getenv('USER', 'unknown')}")
    print("✅ Python app is running successfully!")

if __name__ == "__main__":
    main()
