import threading;
import time;

class TranscriptThread(threading.Thread):
    def __init__(self, transcriptstream):
        self.transcriptstream = transcriptstream;
        self.currentTime = 0;
        threading.Thread.__init__(self);
        
    def run(self):
        for event in self.transcriptstream['root']['Message']:
            timeDelta = int(event['@time']) - self.currentTime;
            time.sleep(timeDelta / 1000.0);
            self.currentTime = int(event['@time']);

            if event['Method'] == "playEvent" and event.get('Object') and event['Object'].get('iconType') and event['Object']['iconType'] == "chat":
                print(self.__formatChatMessage(event['Object']));

    def __formatChatMessage(self,chatObject):
        return "{}: {}: {}".format(chatObject['time'], chatObject['name'], chatObject['label']);
                
