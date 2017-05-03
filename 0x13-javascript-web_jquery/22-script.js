$.get('http://swapi.co/api/films?format=json', function (data) {
  $.each(data['results'], function (index, movie) {
    $('UL#list_movies').append($('<LI></LI>').text(movie['title']));
  });
});
