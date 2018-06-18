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

function BG_Update(laps){
    if (laps<BRONZE_MEDAL_LAP_COUNT){
        document.getElementById("bg").style.background = NO_MEDAL_BG;
    }
    else if (laps>=BRONZE_MEDAL_LAP_COUNT && laps<SILVER_MEDAL_LAP_COUNT){
        document.getElementById("bg").style.background = BRONZE_MEDAL_BG;
    }
    else if (laps>=SILVER_MEDAL_LAP_COUNT && laps<GOLD_MEDAL_LAP_COUNT){
        document.getElementById("bg").style.background = SILVER_MEDAL_BG; 
    }
    else if (laps>=GOLD_MEDAL_LAP_COUNT){
        document.getElementById("bg").style.background = GOLD_MEDAL_BG; 
    }

}
$(document).ready(() => {
    $.ajaxSetup({cache: false}); // no cache
    // Initialize
    $.getJSON(SWIMMER_DATA_FILE, raw => {
        BG_Update(raw.laps)
        $('#name').text(raw.name);
        set_stat($('#laps'), raw.laps);
        set_stat($('#meters'), raw.laps * LAP_LENGTH);
        document.title = `${raw.name} | Swim For Love`;
    });
    setInterval(() => {
        $.getJSON(SWIMMER_DATA_FILE, raw => {
            BG_Update(raw.laps)
            set_stat($('#laps'), raw.laps);
            set_stat($('#meters'), raw.laps * LAP_LENGTH);

        });
    }, 2000);
});
