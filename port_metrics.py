import socket
import time
import json

s = socket.socket()

def get_socket_timings(ip, port):

    timings = {}
    timings['ip'] = ip
    timings['port'] = port
    timings['start_time'] = int(time.time()*1000)

    s.connect(( timings.get('ip'), 
                timings.get('port')
                ))

    timings['end_time'] = int(time.time()*1000)
    timings['elapsed_time'] = '{}ms'.format(timings.get('end_time') - timings.get('start_time'))

    print(json.dumps(timings))
    s.close()

if __name__ == '__main__':
    get_socket_timings('www.google.com', 80)