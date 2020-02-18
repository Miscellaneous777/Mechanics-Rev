import hashlib

def genHash(given):
    item = hashlib.sha256()
    item.update(given.encode())
    return item.hexdigest()
    
if __name__ == "__main__":
    print(genHash("jeff"))
