# simple voice chat
# neuralnine
# install vidstream  # pip install vidstream
# run this script on both client and server side
# it is little bit noisy


from vidstream import AudioSender
from vidstream import AudioReceiver

import threading
import socket

receiver = AudioReceiver("192.168.0.127", 9999)  # check your ip address # receiver ip address
receiver_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender("192.168.0.207", 5555)  # sender ip address
sender_thread = threading.Thread(target=sender.start_server)

receiver_thread.start()
sender_thread.start()