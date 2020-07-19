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
    //activate materialize built-in datepicker
    $('.datepicker').datepicker();
    //activate materialize material box
    $('.materialboxed').materialbox();
        

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

 $('label .radio-star').click(function() {
  //1. unbind mouseleave
  //2. remove class selected for all spans
  //3. add back the selected class
  //4. style the color
  $('.radio-star').unbind('mouseleave');
  $(this).removeClass('selected')
  $(this).parent().siblings().children('span').removeClass('selected');
  
  $(this).css('color','#9e9e9e')
  $(this).parent().siblings().children('span').css('color','#9e9e9e')
  
  //query current star value
  let onStar = $(this).prev('input').val();
  $(this).addClass('selected')
  //$(this).parent().nextAll().children('span').addClass('selected');
  $(this).parent().prevAll().children('span').addClass('selected');
  $('.selected').css('color',"#ea0");
});

/**
 * Adjust the indices of form fields when removing items.
 */
function adjustIndices(removedIndex) {
  var $forms = $('.subform');

  $forms.each(function(i) {
      var $form = $(this);
      var index = parseInt($form.data('index'));
      var newIndex = index - 1;

       // Pass - do nothing if current input index is less than removedIndex
      if (index < removedIndex) {
          return true;
      }

      // Change ID in form itself
      $form.attr('id', $form.attr('id').replace(index, newIndex));
      $form.data('index', newIndex);

      // Change IDs in form inputs
      $form.find('input').each(function(j) {
          var $item = $(this);
          $item.attr('id', $item.attr('id').replace(index, newIndex));
          $item.attr('name', $item.attr('name').replace(index, newIndex));
      });
  });
}

/*
Remove a subform.
*/
function removeForm() {
  var $removedForm = $(this).closest('.subform');
  var removedIndex = parseInt($removedForm.data('index'));
  if (removedIndex>0){
  $removedForm.remove();
  // Update indices
  adjustIndices(removedIndex);
  } else {
  var toastHTML = '<span>This input is required.</span>';
  M.toast({html: toastHTML});   
  }
  
}

/* Add a subform */

function addForm() {
  let $templateForm = $('#sightings-0-form');

  // Get Last index
  let $lastForm = $('.subform').last();
  let newIndex = 0;

  if ($lastForm.length > 0) {
    newIndex = parseInt($lastForm.data('index')) + 1;
  }
  
  // Maximum of 6 subforms
  if (newIndex > 5) {  
  var toastHTML = '<span>[WARNING], Reached max number of inputs</span>';
  M.toast({html: toastHTML});   
      return;
  }

  // Add elements
  let $newForm = $templateForm.clone();

  //replace the x in id (sightings-x-form) to the new index
  $newForm.attr('id', $newForm.attr('id').replace('0', newIndex));
  //replace the data-index value by its loop index
  $newForm.attr('data-index', $newForm.attr('data-index').replace('0', newIndex));
  
  $newForm.find('input').each(function(idx) {
    let $item = $(this);
    //remove the existing value in input
    $item.val('');
    //do the same for input (replace x in id and replace data-index by loop-value)
    $item.attr('id', $item.attr('id').replace('0', newIndex));
    $item.attr('name', $item.attr('name').replace('0', newIndex));
});

// Append the cloned item to the table
$('#sightings-container').append($newForm);
$newForm.addClass('subform');
$newForm.removeClass('is-hidden');

}

//event listener to (function)add input when clicked '+'
$('#add-sightings').click(addForm);
//event listener to (function)remove input when clicked '-'
$(document).on('click', '.remove', removeForm)


  });// end document ready