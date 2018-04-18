let leaderboard; // for actual displaying
let topTen; // for updating
let previousData = {}; // for checking changes
let timestamp = {}; // for sorting by order of finish
let totalLaps = 0; // for tallying
let updateDaemon; // for interval updating

let tallyLap;
let tallyMeter;

$(document).ready(() => {
    if (!($(document).width() === 1920 && $(document).height() === 1080)) console.warn('Your screen dimensions might not be optimized to display this page. Consider changing to a 1920×1080 size.');
    $.ajaxSetup({cache: false}); // no cache
    tallyLap = $('.tally.laps.num');
    tallyMeter = $('.tally.meters.num');
    leaderboard = [];
    initLeaderboard();
    updateDaemon = setInterval(retrieve_data, UPDATE_INTERVAL);
});

function retrieve_data(callback=update_leaderboard) {
    $.getJSON(DATA_FILE, raw => {
        let keys = Object.keys(raw);
        let values = Object.values(raw);
        let data = keys.map((e, i) => Object({id: e, name: values[i][0], laps: values[i][1]}));
        data.forEach((e, i) => {
            let id = e.id
            if (timestamp[id] === undefined || (previousData[id] !== undefined && e.laps - previousData[id] > 0)) {
                timestamp[id] = Date.now() + i;
            }
            previousData[id] = e.laps;
        });
        data.sort((a, b) => a.laps > b.laps ? -1 : (a.laps < b.laps ? 1 : timestamp[a.id] < timestamp[b.id] ? -1 : 1));
        let newTotal = data.map(e => e.laps).reduce((a, b) => a + b);
        tally(newTotal);
        topTen = data.slice(0, 10);
        callback();
        leaderboard = topTen;
    });
}

function update_leaderboard() {
    let leaderboardIds = leaderboard.map(e => e.id);
    let topTenIds = topTen.map(e => e.id);
    if (leaderboard.length > topTen.length) {
        console.warn('Suspicious decreased leaderboard players!');
        return;
    }
    leaderboard.forEach(e => {
        let id = e.id;
        if (!topTenIds.includes(id)) remove_player(id); // fell out of leaderboard
    });
    topTen.forEach((e, i) => {
        let id = e.id;
        let laps = e.laps;
        if (!leaderboardIds.includes(id)) { // a new player
            insert_player(e, null, i, false);
            return;
        }
        // console.log(e, i);
        let diffLaps = laps - parseInt($(`#${id} .laps`).text());
        if (diffLaps > 0) {
            increment($(`#${id} .laps`), diffLaps);
            increment($(`#${id} .meters`), diffLaps * LAP_LENGTH);
        }
        change_rank(id, i);
    });
}

function tally(newTotal) {
    let tallyDiff = newTotal - totalLaps;
    if (tallyDiff > 0) {
        increment(tallyLap, tallyDiff);
        increment(tallyMeter, tallyDiff * LAP_LENGTH);
        totalLaps = newTotal;
    }
}

function increment(element, updateCount) {
    let current = parseInt(element.text());
    element.prop('counter', current).animate({counter: current + updateCount}, {
        duration: METER_UPDATE_SPAN,
        easing: 'swing',
        step: now => element.text(Math.ceil(now))
    });
}
