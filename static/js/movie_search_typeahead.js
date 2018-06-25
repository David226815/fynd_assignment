$(document).ready(function() {
    $('#movie-search').typeahead({source: function (query, process) {
        return $.getJSON(
            '/autocomplete/movie_autocomplete/', // this is the url for the view we created in step 1
             { query : query },
             function (data) {
                console.log(data) ;
                return process(data);
             });
        }});
 });