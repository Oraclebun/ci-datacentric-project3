$(document).ready(function(){
    //activate parallax
    $('.parallax').parallax();
    //activate collapsible (accordion)
    $('.collapsible').collapsible();
    //initialize sidenav 
    $('.sidenav').sidenav();
    //activate tooltip
    $('.tooltipped').tooltip();
    //activate modal
    $('.modal').modal();
    //activate drop down menu
    $(".dropdown-trigger").dropdown();
        

    $.fn.stars = function () {
        return $(this).each(function () {
            var val = parseFloat($(this).html());       //value of rating
            var size = Math.max(0, (Math.min(5, val))) * 24;    //find the max of the rating, multiply by 24
            var $span = $('<span />').width(size);      //use the calculated size to size the span
            $(this).html($span);                        //replace this with width of the span
        });
    }
  
    $(function() {
        $('span.stars').stars();
    });

  });// end document ready