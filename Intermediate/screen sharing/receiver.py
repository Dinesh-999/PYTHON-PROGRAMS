# screen sharing
# install vidstream
# neuralnine

from vidstream import StreamingServer
import threading

receiver = StreamingServer("192.168.0.107", 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != "STOP":
    continue

receiver.stop_server()











