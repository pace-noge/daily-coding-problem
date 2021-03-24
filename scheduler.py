from time import time, sleep
import threading


class Scheduler:
    def __init__(self):
        self.fns = []
        t = threading.Thread(target=self.poll)
        t.start

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
                self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
                sleep(0.01)
    def delay(self, f, n):
        self.fns.append((f, time()*1000 +n))


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.delay(print("haloo"), 30000)
    scheduler.delay(print("world"), 35000)

