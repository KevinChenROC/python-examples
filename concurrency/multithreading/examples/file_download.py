###########
# File Downloader
# Write a function to download a list of files.

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# !!!!! IMPORTANT !!!!!
# If it takes 1 second to download 1 file, it shouldn't
#   take 10 seconds to download 10 files.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# +++ START YOUR IMPLEMENTATION

import requests
from threading import Thread
from queue import Queue
import os

# def download_file(url, dest_folder, q=None):
#     r = requests.get(url)
#     idx = url.find("SN-")
#     fileName = url[idx:]
#     with open(dest_folder + "/" + fileName, "wb") as f:
#         f.write(r.content)

#     if not q:
#         q.task_done()


def download_file(dest_folder, q):
    # worker thread is blocked if q is empty
    url = q.get()

    fileName = url[url.find("SN-") :]
    dest_path = dest_folder + "/" + fileName

    # if the file is not found, download it!
    if not os.path.exists(dest_path):
        r = requests.get(url)
        with open(dest_folder + "/" + fileName, "wb") as f:
            f.write(r.content)

    # Make sure the main thread will not block after all tasks are done.
    if q:
        q.task_done()


def download(urls, dest_folder):
    """Download a collection of files designated by `urls` and save them
    in `dest_folder`.
    """
    # For each url, create a new thread
    N_threads = len(urls)
    q = Queue()

    # Create worker threads to download files
    for i in range(N_threads):
        t = Thread(target=download_file, args=(dest_folder, q))
        t.start()

    # Put tasks into q to be consumed by worker threads
    for url in urls:
        q.put(url)

    # the main thread is blocked until all tasks are done!
    q.join()


# --- START YOUR IMPLEMENTATION


def main():
    import time

    base_url = "https://www.grc.com/sn/"
    urls = []
    start = time.time()
    for i in range(500, 511):
        # urls.append(base_url + 'SN-' + str(i) + '-notes.pdf')
        urls.append(f"{base_url}SN-{i}-notes.pdf")
    download(urls, ".")
    end = time.time()
    print(f"Total time taken: {end-start:.2f}")


main()
print("---Done with file_downloader")
