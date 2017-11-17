import multiprocessing as mp
from Queue import Queue
import threading

class Worker(threading.Thread):
    def __init__(self, id, queue, res, func, progress):
        threading.Thread.__init__(self)
        self.queue = queue
        self.results = res
        self.name = id
        self.process = func
        self.progress = progress


    def run(self):
        while True:
            input1, input2 = self.queue.get()
            status = 'Processing {} - {} on thread {}\n'.format(input1.idstu,
                input2.idstu, self.name)
            self.results.put(self.process(input1, input2))
            self.progress.update(self.results.qsize(), status).show_progress()
            self.queue.task_done()


def main():
    data = xrange(10) # Some test data to work with
    q = Queue() # Queue to store items to process
    r = Queue() # Queue to store items processed
    workers = [] # Active thread pool

    for core in xrange(mp.cpu_count()):
        worker = DataProcessor(core + 1, q, r, double)
        worker.daemon = True
        worker.start()
        workers.append(worker)

    for i in data:
        item = i + 1
        print 'Adding {} to queue\n'.format(item)
        q.put(item)

    q.join() # Wait for the queue to be processed entirely

    print [r.get() for i in xrange(r.qsize())] # Get all results in one nice list

