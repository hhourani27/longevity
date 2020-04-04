function createMarker(latitude, longitude, popupText, url) {
	marker = new L.marker([latitude, longitude], {
        "win_url" : url
        });
	marker.bindPopup(popupText);
	
    marker.on('mouseover', function (e) {
            this.openPopup();
        });
    
	marker.on('mouseout', function (e) {
            this.closePopup();
        });
	
	marker.on('click', function (e) {
            window.open(this.options.win_url);
        });
		
	return marker
}