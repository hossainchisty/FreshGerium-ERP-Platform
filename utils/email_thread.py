import threading


class EmailThread(threading.Thread):
    ''' This module provides sending emails with threading that run in background. '''

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
