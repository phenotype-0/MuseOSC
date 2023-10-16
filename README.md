# Muse Player

Replays data that was recorded from a Muse EEG Headset.

## Installation

`pip install -r requirements.txt`

## Run

`python museplayer.py`

This will send 10+ minutes of data at 256 samples per second over OSC.

By default, it is on port 9807 with addresses of:

```
/muse/TP9
/muse/AF7
/muse/AF8
/muse/TP10
```

## Options

`python museplayer.py --help`

To change the port that OSC data is being transmitted on, use `--port` command line argument.
To change the base address path for the OSC data, use the `--address` command line argument.

```
python museplayer.py --port 9876 --address /eeg`
```

This will send the data over OSC on port 9876 with the addresses of: 

```
/eeg/TP9
/eeg/AF7
/eeg/AF8
/eeg/TP10
```

