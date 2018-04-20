from pathlib import Path

# Paths and files
SWIMMERS_DIR = Path('swimmers')
EXAMPLE_DIR = Path('resources/swimmer_template')
PICKLE_FILE = Path('Swimmer_Database.pickle')
STAT_FILE = Path('stat_all.json')
SWIMMER_SCAN_FILE = Path('scanned.json')
REGISERS_URL = 'http://localhost/Swim-For-Love-Project/register.json'
SCANNED_URL = 'http://localhost/Swim-For-Love-Project/scanned.json'

# Thresholds
MIN_SIGNAL_STRENGTH = -50
MAX_SIGNAL_STRENGTH = -5
DETECTION_INTERVAL = 20

# Misc
HELP_MSG = '''
Arguments:
 -h, --help         Show this help message and exit
 -n, --new          Create new statistics (default: use existing data)
 -c, --clear-data   Delete all swimmer files and statistics and exit
 -d, --debug        Show debugging information (verbose output)\n'''
