let leaderboard; // for actual displaying
let topTen; // for updating
let totalLaps = 0; // for tallying
let updateDaemon; // for interval updating

let tallyLap;
let tallyMeter;

$(document).ready(() => {
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
        data.sort((a, b) => (a.laps > b.laps) ? 1 : ((a.laps < b.laps) ? -1 : 0));
        let newTotal = data.map(e => e.laps).reduce((a, b) => a + b);
        tally(newTotal);
        topTen = data.reverse().slice(0, 10);
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
        change_rank(id, i);
        let diffLaps = laps - parseInt($(`#${id} .laps`).text());
        if (diffLaps > 0) {
            $(`#${id} .laps`).text(laps);
            add_meters(id, diffLaps);
        }
    });
}

function tally(newTotal) {
    let tallyDiff = newTotal - totalLaps;
    if (tallyDiff > 0) {
        let totalMeters = totalLaps * LAP_LENGTH;
        let lapUpdateInterval = METER_UPDATE_SPAN / LAP_LENGTH / tallyDiff;
        let meterUpdateInterval = METER_UPDATE_SPAN / tallyDiff;
        for (let i = 0; i < tallyDiff; i++) {
            setTimeout(() => tallyLap.text(parseInt(tallyLap.text()) + 1), i * meterUpdateInterval);
            for (let j = 0; j < LAP_LENGTH; j++) {
                setTimeout(() => tallyMeter.text(parseInt(tallyMeter.text()) + 1), (i * LAP_LENGTH + j) * lapUpdateInterval);
            }
        }
        totalLaps = newTotal;
    }
}
