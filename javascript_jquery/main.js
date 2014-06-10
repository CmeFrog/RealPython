$(function() {
  
  console.log("whee!")
  
  // event handler
  $("#btn-click").click(function() {
    if ($('input').val() !== '') {
      // grab the value from the input box after the button click
      var input = $('input').val()
      // display input if javascript console
      console.log(input)
      // display value on web page (DOM)
      $('ol').append('<li><a href="">x</a> - ' + input + '</li>');
    }
    $('input').val('');
  });

});

$(document).on('click', 'a', function (e) {
	e.preventDefault();
	$(this).parent().remove();
});