const LAP_LENGTH = 50; // meters
const METER_UPDATE_SPAN = 950; // milliseconds
const LEADER_COLS_WIDTH = [0, 0.08, 0.6, 0.75];
const LEADER_LINE_HEIGHT = 46 * 1.5;

const SOCKET_URL = 'http://leaderboard.swim4love.com:8080';
const GOLD_THRESHOLD = 100; // laps
const SILVER_THRESHOLD = 50; // laps
const BRONZE_THRESHOLD = 20; // laps
const NO_MEDAL_BG = 'linear-gradient(-45deg, #b721ff 0%, #21d4fd 100%)';
const BRONZE_BG = 'linear-gradient(-45deg, #c79081 0%, #dfa579 100%)';
const SILVER_BG = 'linear-gradient(-45deg, #d5d4d0 0%, #d5d4d0 1%, #eeeeec 31%, #efeeec 75%, #e9e9e7 100%)';
const GOLD_BG = 'linear-gradient(-45deg, #e6b980 0%, #eacda3 100%)';
const CONFETTI_TIMEOUT = 2000; // milliseconds
