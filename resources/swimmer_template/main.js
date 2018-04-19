function increment(element, updateCount) {
    let current = parseInt(element.text());
    element.prop('counter', current).animate({counter: current + updateCount}, {
        duration: 2000,
        easing: 'swing',
        step: now => element.text(Math.ceil(now))
    });
}

$(document).ready(() => {
    $.ajaxSetup({cache: false}); // no cache
    $.getJSON(SWIMMER_DATA_FILE, raw => {
        $('#name').text(raw.name);
        increment($('#laps'), raw.laps);
        increment($('#meters'), raw.laps * LAP_LENGTH);
        document.title = `${raw.name} | Swim For Love`;
    });
});
