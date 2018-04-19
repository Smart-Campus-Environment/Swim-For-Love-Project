previous_lap_count=null;
current_lap_count=null;
current_meters_count=null;
previous_meters_count=null;
function increment(type,element,updateCount) {
    if (type=='Lap'){
        current = previous_lap_count;
    }
    else if (type=='Meters'){
        current = previous_meters_count;
    }
    element.prop('counter', current).animate({counter: current + updateCount}, {
        duration: 2000,
        easing: 'swing',
        step: now => element.text(Math.ceil(now))
    });
}

(function update() {
    $(document).ready(() => {
        $.getJSON(SWIMMER_DATA_FILE, raw => {
            current_lap_count=raw.laps;
            current_meters_count=current_lap_count*LAP_LENGTH;
            change=current_lap_count-previous_lap_count;
            $('#name').text(raw.name);
            increment('Lap',$('#laps'),change);
            increment('Meters',$('#meters'),change * LAP_LENGTH);
            document.title = `${raw.name} | Swim For Love`;
            previous_lap_count=current_lap_count;
            previous_meters_count=current_meters_count;
        });
    });
    setTimeout(update, 500);
})();