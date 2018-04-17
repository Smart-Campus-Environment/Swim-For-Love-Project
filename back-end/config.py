from pathlib import Path

# Paths and files
SWIMMERS_DIR = Path('swimmers')
EXAMPLE_DIR = Path('resources/swimmer_template')
PICKLE_FILE = Path('Swimmer_Database.pickle')
STAT_FILE = Path('stat_all.json')
SWIMMER_SCAN_FILE = Path('scanned.json')

# Thresholds
MINIMUM_SIGNAL_STRENGTH = -50
MAXIMUM_SIGNAL_STRENGTH = -5
TIME_INTERVAL_BETWEEN_DETECTION = 20
