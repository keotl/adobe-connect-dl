import threading;
import time;

class FtContentThread(threading.Thread):
    def __init__(self, ftcontentStream, streamDirectory):
        self.ftcontentStream = ftcontentStream;
        self.currentTime = 0;
        self.streamDirectory = streamDirectory;
        threading.Thread.__init__(self);
        
    def run(self):
        for event in self.ftcontentStream['root']['Message']:
            timeDelta = int(event['@time']) - self.currentTime;
            time.sleep(timeDelta / 1000.0);
            self.currentTime = int(event['@time']);
                

