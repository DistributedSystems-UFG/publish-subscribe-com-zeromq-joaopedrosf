import zmq, time
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://0.0.0.0:"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
staticMsg = "This is a static message"
i = 0
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg = str.encode("TIME " + time.asctime())
	msg2 = str.encode("COUNTER " + str(i))
	msg3 = str.encode("STATIC " + staticMsg)
	i += 1
	s.send(msg) # publish the current time
	s.send(msg2)
	s.send(msg3)
