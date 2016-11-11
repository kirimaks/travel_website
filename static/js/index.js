$(document).ready(function() {
    $("#mainNav ul li:nth-child(2)").addClass("active")

    ymaps.ready(init);
    var myMap, place1;

    function init(){     
        // Create map.
        myMap = new ymaps.Map("map", {
            center: [43.587272, 39.713958],
            zoom: 10
        });
        myMap.behaviors.disable('scrollZoom');

        // Create a place.
        place1 = new ymaps.Placemark([43.684401, 40.231909], 
                                      { hintContent: 'Красная Поляна', 
                                        balloonContent: '<a href="#">link</a>' });

        // Add the place.
        myMap.geoObjects.add(place1);
    }
});

