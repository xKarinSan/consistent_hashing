from HashRing import HashRing  # Make sure your class is saved as hash_ring.py

def main():
    # Create a HashRing with 4 servers
    ring = HashRing(size=4)
    
    # Add some keys
    for key in [10, 22, 37, 49, 55, 63, 72]:
        ring.add_key(key)
    
    print("\nInitial server key distribution:")
    ring.view_server_keys()
    
    # Add a server
    print("\nAdding a server...")
    ring.add_server()
    ring.view_server_keys()

    # Add more keys after server addition
    for key in [85, 91]:
        ring.add_key(key)
    
    print("\nAfter adding more keys:")
    ring.view_server_keys()

    # Delete a server (e.g., index 2)
    print("\nDeleting server at index 2...")
    ring.delete_server(2)
    ring.view_server_keys()

if __name__ == "__main__":
    main()
