let map;
let marker;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });

  // Use watchPosition() method to continuously track the location of the GPS tracker and update the map
  navigator.geolocation.watchPosition(updateMap, showError);
}

function updateMap(position) {
  // Create a new marker on the map at the current location of the GPS tracker
  if (!marker) {
    marker = new google.maps.Marker({
      position: {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      },
      map,
      title: "GPS Tracker",
    });
  } else {
    // Update the marker position every time the watchPosition() method is called
    marker.setPosition({
      lat: position.coords.latitude,
      lng: position.coords.longitude,
    });
  }

  // Center the map on the current location of the GPS tracker
  map.setCenter({
    lat: position.coords.latitude,
    lng: position.coords.longitude,
  });
}

function showError(error) {
  console.log(error);
}