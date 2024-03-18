import os

def delete_files():
    print("Deleting files")
    dir_path = 'cutted/'
    extension = '.mp4'

    files = os.listdir(dir_path)
    print(f"Files found: {files}")
    
    mp4_files = [file for file in files if os.path.splitext(file)[1] == extension]
    for mp4 in mp4_files:
        if os.path.exists(f"cutted/{mp4}"):
            os.remove(f"cutted/{mp4}")
    print(f"Deleted {len(mp4_files)} files")
        