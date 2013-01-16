#!/usr/bin/python

import _thread
import time
import threading

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
	  

# Create two threads as follows
i=0;
while (i<20):
   if(threading.activeCount()<=4):
      try:
         threadname="thread"+str(i);
         _thread.start_new_thread( print_time, (threadname, 2, ) );
         i=i+1;
      except:
         print ("Error: unable to start thread");
