from pathlib import Path

ROOT_URL = 'http://leaderboard.swim4love.com'
PERSONAL_SPAN = 5 # seconds

API_URL = 'http://leaderboard.swim4love.com:8080'
CHECK_URL = API_URL + '/swimmer/info/{}'
NEW_SWIMMER_URL = API_URL + '/swimmer/new'
UPDATE_AVATAR_URL = API_URL + '/swimmer/update/avatar'
UPDATE_NAME_URL = API_URL + '/swimmer/update/name'
LOCAL_AVATAR_DIR = Path('avatars')
DEFAULT_AVATAR = LOCAL_AVATAR_DIR / 'default.jpg'
AVATAR_SIZE = (1000, 1000)
