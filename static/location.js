function initMap() {
        var myLatLng = {lat: 35.658581, lng: 139.745433};

        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: myLatLng
        });

        for(i = 0; i < data.length; i++){
            data[i].url = '/gar_status/' + i;
            //register each marker
            var markers = new google.maps.Marker({
                position: new google.maps.LatLng(data[i].lat, data[i].lng),
                map: map,
                title: data[i].name
            });
            //add event 
            google.maps.event.addListener(markers, 'click', (function(url){
                return function(){ location.href = url; };
            })(data[i].url));
        }
    }
    

