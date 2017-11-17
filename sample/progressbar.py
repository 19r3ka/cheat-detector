'''
  Simplest progress bar
'''
import sys
import time

class ProgressBar(object):
    def __init__(self, length, goal, status='Work in progress'):
        self.goal = float(goal)
        self.length = int(length)
        self.progress = 0
        self.status = status


    def draw(self):
        done = '#' * int(round(self.length * self.progress))
        todo = '-' * (self.length - len(done))
        full_bar = done + todo
        return full_bar


    def get_status(self):
        if self.progress >= 1:
            self.status = 'Done !'
        return self.status


    def update(self, value, status=''):
        self.progress = value / self.goal
        self.status = status if status else self.status
        return self


    def set_goal(self, goal):
        self.goal = float(goal)
        return self


    def show_progress(self):
        #sys.stdout.write('[%s] %d %s - %s\r' % (full_bar, percentage, '%', status),)
        print '\r[{}] {} % - {}'.format(self.draw(), int(round(self.progress *
            100)), self.get_status()),
        sys.stdout.flush()
        return self

