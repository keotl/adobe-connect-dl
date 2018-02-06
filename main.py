import xmltodict
import time
import collections
from TranscriptThread import TranscriptThread
from MainstreamThread import MainstreamThread
from IndexstreamThread import *;

TEST_FILE_PATH = "example/";

with open(TEST_FILE_PATH + "indexstream.xml") as fd:
# with open(TEST_FILE_PATH + "test.xml") as fd:
    indexstream = xmltodict.parse(fd.read())
with open(TEST_FILE_PATH + "transcriptstream.xml") as fd:
    transcriptstream = xmltodict.parse(fd.read())
with open(TEST_FILE_PATH + "mainstream.xml") as fd:
    mainstream = xmltodict.parse(fd.read())
with open(TEST_FILE_PATH + "ftcontent1.xml") as fd:
    ftcontent = xmltodict.parse(fd.read())

downloadPdfs(indexstream);
    
events = indexstream['root']['Message'];

currentTime = 0;

transcriptThread = TranscriptThread(transcriptstream);
transcriptThread.start();

mainstreamThread = MainstreamThread(mainstream, TEST_FILE_PATH);
mainstreamThread.start();

for event in events:
    timeDelta = int(event['@time']) - currentTime;
    time.sleep(timeDelta / 1000.0);
    currentTime = int(event['@time']);
    if event.get('Object') and type(event['Object']) == collections.OrderedDict and event['Object'].get('name'):
        print ("{} : {}".format(float(event['@time'])/1000.0, event['Object']['name']));
    else:
        print("{} : {}".format(float(event['@time'])/1000, event['Method']));
    
