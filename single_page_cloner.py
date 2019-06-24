import progressbar
import requests



def menu():
    print("Enter url:")
    url = input()
    print("Enter filename:")
    filestr = input()
    download_file(url,filestr)

def download_file(url,filestr):
    local_filename = filestr
    r = requests.get(url, stream=True)
    f = open(local_filename, 'wb')
    file_size = int(r.headers['Content-Length'])
    chunk = 1
    num_bars = file_size / chunk
    bar =  progressbar.ProgressBar(maxval=num_bars).start()
    i = 0
    for chunk in r.iter_content():
        f.write(chunk)
        bar.update(i)
        i+=1
    f.close()
    menu()


try:
    menu()
except:
    menu()
