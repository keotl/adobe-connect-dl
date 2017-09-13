import threading;
import time;
import playsound;

def playStream(streamFile):
    print("Playing file {}".format(streamFile));
    playsound.playsound(streamFile, False);
    

class MainstreamThread(threading.Thread):
    def __init__(self, mainstream, streamDirectory):
        self.mainstream = mainstream;
        self.currentTime = 0;
        self.streamDirectory = streamDirectory;
        threading.Thread.__init__(self);
        
    def run(self):
        for event in self.mainstream['root']['Message']:
            timeDelta = int(event['@time']) - self.currentTime;
            time.sleep(timeDelta / 1000.0);
            self.currentTime = int(event['@time']);
            if event.get('Method') and event.get('String') and event.get('Array') and event.get('String') == "streamAdded" and event.get('Array').get('Object'):
                playStream(self.streamDirectory + event['Array']['Object']['streamName'].replace('/','') + ".flv");
                
