import subprocess;
import os;
import shutil;
import time;

CLASSE_VIRTUELLE_URL = 'https://classevirtuelle.ulaval.ca';
PATH = "example/";
DOWNLOAD_FOLDER = "/home/kento/Downloads/";

def hasKeyRecursive(event, keys):
    currentNode = event;
    for index,key in enumerate(keys):
        if (type(currentNode) == str) and index == len(keys) - 1:
            return True;
        if currentNode.get(key):
            currentNode = currentNode.get(key);
        else:
            return False;
    return True;

def getFilename(url):
    return url[url.find('&name=') + 6::];

def downloadPdfs(indexstream):
    print("Starting PDF download...");
    urls = set();
    
    for event in indexstream['root']['Message']:
        try:
            path = event.get('Array').get('Object').get('newValue').get('documentDescriptor').get('downloadUrl');
            print("got path");
            filename = getFilename(path);
            if not os.path.exists(PATH + filename):
                urls.add(CLASSE_VIRTUELLE_URL + path);
        except Exception:
            continue;
    print("urls: {}".format(urls));
    for url in urls:
        subprocess.call(['xdg-open', url]);
        print("downloading url:{}".format(url));
        while not os.path.exists(DOWNLOAD_FOLDER + getFilename(url)):
            time.sleep(1);
        shutil.copyfile(DOWNLOAD_FOLDER + getFilename(url), PATH + getFilename(url));
    print("Done downloading PDFs");
    
