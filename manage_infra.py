#!/usr/bin/env python3
import os

def main():
    print("Managing infrastructure...")
    # Example action: Listing files in a directory
    files = os.listdir('/usr/bin')
    for file in files:
        print(file)

if __name__ == "__main__":
    main()
