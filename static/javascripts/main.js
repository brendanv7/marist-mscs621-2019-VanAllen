$(document).ready(function() {

  function reload() {
    $('.hidden').fadeOut();
    $('displayOutput').empty();
    $.get( '/words', function(data) {
      console.log("showing", data);

      var data = JSON.parse(data);
      var rendered = "<ul>";
      data.forEach(function(item) {
        rendered = rendered + "<li>" + item.word + ": " + item.definition + "</li>";
      });
      rendered = rendered + "</ul>";

      $('#displayOutput').html(rendered);
    });
    $('.hidden').fadeIn();
  }

  $('#add-word').submit(function(e) {
    e.preventDefault();
    $.ajax({
      url: '/words',
      type: 'PUT',
      data: $(this).serialize(),
      success: function(data) {
        reload();
      }
    });
  });

  reload();

});
