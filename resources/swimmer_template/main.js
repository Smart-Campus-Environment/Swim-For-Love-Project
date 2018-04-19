let currentLaps = 0;

function set_stat(element, to, span=2000) {
    let current = parseInt(element.text());
    if (current === to) return;
    element.prop('counter', current).animate({counter: to}, {
        duration: span,
        easing: 'swing',
        step: now => element.text(Math.ceil(now))
    });
}

$(document).ready(() => {
    $.ajaxSetup({cache: false}); // no cache
    // Initialize
    $.getJSON(SWIMMER_DATA_FILE, raw => {
        $('#name').text(raw.name);
        set_stat($('#laps'), raw.laps);
        set_stat($('#meters'), raw.laps * LAP_LENGTH);
        document.title = `${raw.name} | Swim For Love`;
    });
    setInterval(() => {
        $.getJSON(SWIMMER_DATA_FILE, raw => {
            set_stat($('#laps'), raw.laps);
            set_stat($('#meters'), raw.laps * LAP_LENGTH);
        });
    }, 2000);
});
