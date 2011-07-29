$(function() {
  $('div[id^="sshow_"]').each(function() {
    var id = this.id.split("_")[1];
    $.getJSON("/ajax/slideshow/",
      {"id":id},
      function(data) {
        start_slide(data[1], id, data[0].width, data[0].height);
      });
  });
});

function start_slide(data, id, w, h) {
  $('#flavor_1').agile_carousel({
    carousel_data: data,
    carousel_outer_height: h,
    carousel_height: h,
    slide_height: h+2,
    carousel_outer_width: w,
    slide_width: w,
    transition_time: 700,
    timer: 4000,
    continuous_scrolling: true,
    control_set_1: "numbered_buttons",
  });
}
