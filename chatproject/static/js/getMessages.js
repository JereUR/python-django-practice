$(document).ready(function () {
  setInterval(function () {
    $.ajax({
      type: 'GET',
      url: '/getMessages/' + room + '/',
      success: function (response) {
        $('#display').empty()
        for (var i = 0; i < response.messages.length; i++) {
          var temp =
            "<div class='container darker'><b>" +
            response.messages[i].user +
            '</b><p>' +
            response.messages[i].value +
            "</p><span class='time-left'>" +
            response.messages[i].date +
            '</span></div>'
          $('#display').append(temp)
        }
      },
      error: function (response) {
        alert('An error occurred')
      }
    })
  }, 1000)
})
