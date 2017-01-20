import pyinotify
import stream
import threading

class StreamThread(threading.Thread):
	# define behavoir of thread
    def __init__(self):
        self.stopped = False
        threading.Thread.__init__(self)

    def run(self):
        stream.start()

    def stop(self):
    	self.stopped = True

global thr
thr = StreamThread()

class ModHandler(pyinotify.ProcessEvent):
	# start stream on startup in a separate thread
	thr.start()
	def process_IN_MODIFY(self, event):
		# restart stream on modification of configuration
		global thr	
		thr.stop()
		stream.disconnect()
		thr = StreamThread()
		thr.start()

# define notifier to watch for configuration modifications without polling 	
handler = ModHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('config.yaml', pyinotify.IN_MODIFY)
notifier.loop()
