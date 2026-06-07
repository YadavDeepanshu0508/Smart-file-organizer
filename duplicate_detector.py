import hashlib

def file_hash(path):
    sha = hashlib.sha256()

    with open(path, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)

    return sha.hexdigest()

def find_duplicates(files):
    hashes = {}
    duplicates = []

    for file in files:
        try:
            h = file_hash(file)

            if h in hashes:
                duplicates.append(file)
            else:
                hashes[h] = file

        except:
            pass

    return duplicates