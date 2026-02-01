import os
import threading
import sys
from socketserver import TCPServer, BaseRequestHandler
import hud


class ProcessExitHandler:
    def __init__(self):
        self.can_process_exit: bool= False
    def expect_process_exit(self):
        self.can_process_exit = True


process_exit_handler = ProcessExitHandler()


class RequestHandler(BaseRequestHandler):
    def handle(self):
        process_exit_handler.expect_process_exit()


server = TCPServer(("localhost", 6961), RequestHandler)


def is_process_running(pid: int) -> bool:
    try: os.kill(pid, 0)
    except OSError: return False
    else: return True


def main():
    pid: int= 0
    for arg in sys.argv:
        parg = arg.split("=")
        if parg[0] == "--monitor-pid":
            pid = int(parg[1])
            break
    
    if pid <= 0:
        raise Exception("0 is not a valid pid")
    if not is_process_running(pid):
        raise Exception("Program with PID of {pid} doesn't exist".format(pid=pid))

    server_thread = threading.Thread(target = server.serve_forever)
    server_thread.start()

    print("Running...")
    while is_process_running(pid):
        if process_exit_handler.can_process_exit:
            server.shutdown()
            print("Closed normally")
            return
    server.shutdown()
    print("Closed abnormally")
    hud.crash_window()

if __name__ == '__main__':
    main()