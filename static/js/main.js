$(document).ready(function(){
    //initialize parallax
    $('.parallax').parallax();
    //initialize collapsible (accordion)
    $('.collapsible').collapsible();
    //initialize sidenav 
    $('.sidenav').sidenav();
    //initialize tooltip
    $('.tooltipped').tooltip();
    $('.modal').modal();

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