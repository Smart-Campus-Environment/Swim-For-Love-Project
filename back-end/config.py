from pathlib import Path

# Paths and files
SWIMMERS_DIR = Path('swimmers')
EXAMPLE_DIR = Path('resources/swimmer_template')
PICKLE_FILE = Path('Swimmer_Database.pickle')
STAT_FILE = Path('stat_all.json')
LOCAL_SCANNED_FILE = Path('scanned.json')
REGISTER_FILE_PATH=Path('register/register.json')
SWIMMERS_PATH='swimmers/'
TEMP_PHOTO_PATH='register/temp_photo/'
REGISTER_PATH='register/'
REMOTE_ROOT = 'http://localhost/Swim-For-Love-Project/'
REGISTERS_URL = REMOTE_ROOT + 'register/'
REGISTER_FILE_URL = REGISTERS_URL + 'register.json'
SCANNED_URL = REMOTE_ROOT + 'scanned.json'

<<<<<<< HEAD
# Signal Handling
=======

# Thresholds
>>>>>>> 042ddde2892508530dbda9ef00096400244c0540
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
