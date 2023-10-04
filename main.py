import argparse
import csv
import os
from time import sleep, time
from pathlib import Path

from pythonosc.udp_client import SimpleUDPClient


def main(port, address):
    print(f"sending on localhost:{port} to {address}/*")
    channels = ('TP9', 'AF7', 'AF8', 'TP10')
    file_path = os.path.join(Path(__file__).parent, 'muse.eegsv')
    if not os.path.exists(file_path):
        raise FileNotFoundError('could not find muse.eegsv')
    file_handle = open(file_path)
    muse_data = csv.DictReader(file_handle)

    client = SimpleUDPClient('127.0.0.1', port)

    current_ts = 0
    sample_count = 0
    start_time = time()
    for sample in muse_data:
        ts = int(sample['timestamp'])
        if current_ts:
            delay = ts - current_ts
            sleep(delay / 1e6)
        for channel in channels:
            address = f"/eeg/{channel}"

            client.send_message(address, [float(sample[channel]), ])
        current_ts = ts
        sample_count += 1

        minutes = int((time() - start_time) / 60)
        seconds = int((time() - start_time) % 60)

        print(f'\rmuse samples sent: {sample_count} ({minutes}:{seconds:02})', end='')

    #
    # client = SimpleUDPClient('127.0.0.1', 9807)
    # timestamp = None
    # total_time = 0
    # sample_count = 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='utility to replay muse recording over OSC, requires ')
    parser.add_argument('--port', type=int, help="OSC port to send data (default: 9807)", default=9807)
    parser.add_argument('--address', type=str, help="OSC channel address (default: '/muse')", default='/muse')

    args = parser.parse_args()
    main(args.port, args.address)
    print('\ncomplete.')

