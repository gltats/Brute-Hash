import os
import hashlib

def main():
    target_image = 'Python/hacker_fingerprint.tif'
    with open(target_image, 'rb') as f:
        target_hash = hashlib.sha256(f.read()).hexdigest()
    image_dir = 'Python/img'
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.tif'):
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                if file_hash == target_hash:
                    print(f"[+] Image found: {file_path}")

if __name__ == '__main__':
    main()