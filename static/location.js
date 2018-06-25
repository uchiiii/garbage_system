function initMap() {
        var myLatLng = {'id':0, 'name': 'keisu_garbage', lat: 35.714162, lng: 139.761099};

        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: myLatLng
        });

        url = "/personal/0";
        var markers = new google.maps.Marker({
            position: new google.maps.LatLng(myLatLng.lat, myLatLng.lng),
            map: map,
            title: myLatLng.name
            });
        //add event 
        google.maps.event.addListener(markers, 'click', (function(url){
            return function(){ location.href = url; };
        })(url));
    
        /*
        Here below should be active when adding several garbage system    
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
        */
}
    

