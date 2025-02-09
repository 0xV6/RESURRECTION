// class BloodDonationMap {
//     constructor() {
//         this.map = null;
//         this.userMarker = null;
//         this.markersLayer = L.markerClusterGroup({
//             maxClusterRadius: 50,
//             spiderfyOnMaxZoom: true,
//             showCoverageOnHover: true,
//             zoomToBoundsOnClick: true
//         });
//         this.hospitals = [];
//         this.bloodBanks = [];
//         this.ngos = [];
//         this.initMap();
//     }
//
//     initMap() {
//         // Initialize the map with new dimensions
//         this.map = L.map('map', {
//             center: [28.6139, 77.2090],
//             zoom: 13,
//             minZoom: 3,
//             maxZoom: 18
//         });
//
//         // Add OpenStreetMap tile layer
//         L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//             attribution: '© OpenStreetMap contributors'
//         }).addTo(this.map);
//
//         // Allow map to handle its own size
//         this.map.invalidateSize();
//
//         // Get user's location
//         this.getUserLocation();
//     }
//
//     addFilterButtons() {
//         // Create filter buttons container
//         const filterContainer = document.createElement('div');
//         filterContainer.className = 'flex space-x-2 mt-4';
//         filterContainer.innerHTML = `
//             <button id="showHospitals" class="bg-blue-500 text-white px-3 py-1 rounded text-sm">Hospitals</button>
//             <button id="showBloodBanks" class="bg-red-500 text-white px-3 py-1 rounded text-sm">Blood Banks</button>
//             <button id="showNGOs" class="bg-green-500 text-white px-3 py-1 rounded text-sm">NGOs</button>
//         `;
//
//         // Insert buttons after the map
//         document.getElementById('map').parentNode.insertBefore(filterContainer, document.getElementById('map').nextSibling);
//
//         // Add event listeners
//         document.getElementById('showHospitals').addEventListener('click', () => this.showFacilities('hospitals'));
//         document.getElementById('showBloodBanks').addEventListener('click', () => this.showFacilities('bloodBanks'));
//         document.getElementById('showNGOs').addEventListener('click', () => this.showFacilities('ngos'));
//     }
//
//     getUserLocation() {
//         if ("geolocation" in navigator) {
//             navigator.geolocation.getCurrentPosition(
//                 (position) => {
//                     const { latitude, longitude } = position.coords;
//                     this.map.setView([latitude, longitude], 13);
//
//                     // Add user marker
//                     if (this.userMarker) {
//                         this.map.removeLayer(this.userMarker);
//                     }
//                     this.userMarker = L.marker([latitude, longitude], {
//                         icon: L.divIcon({
//                             className: 'user-marker',
//                             html: '📍',
//                             iconSize: [25, 25]
//                         })
//                     }).addTo(this.map);
//
//                     // Search for nearby facilities
//                     this.searchNearbyFacilities(latitude, longitude);
//                 },
//                 (error) => {
//                     console.error("Error getting location:", error);
//                 }
//             );
//         }
//     }
//
//     async searchNearbyFacilities(latitude, longitude) {
//         const radius = 50000; // 5km radius
//         const query = `
//         [out:json][timeout:25];
//         (
//             node["amenity"="hospital"](around:${radius},${latitude},${longitude});
//             node["healthcare"="blood_donation"](around:${radius},${latitude},${longitude});
//             node["social_facility"="ngo"](around:${radius},${latitude},${longitude});
//         );
//         out body;
//         >;
//         out skel qt;
//         `;
//
//         try {
//             const response = await fetch('https://overpass-api.de/api/interpreter', {
//                 method: 'POST',
//                 body: query
//             });
//             const data = await response.json();
//             this.processResults(data.elements);
//             this.showFacilities('hospitals'); // Show hospitals by default
//         } catch (error) {
//             console.error('Error fetching nearby facilities:', error);
//         }
//     }
//
//     processResults(elements) {
//         this.hospitals = [];
//         this.bloodBanks = [];
//         this.ngos = [];
//
//         elements.forEach(element => {
//             if (element.type === 'node') {
//                 const facility = {
//                     lat: element.lat,
//                     lon: element.lon,
//                     name: element.tags.name || 'Unnamed Facility',
//                     address: element.tags['addr:full'] || element.tags['addr:street'] || '',
//                     phone: element.tags.phone || 'N/A'
//                 };
//
//                 if (element.tags.amenity === 'hospital') {
//                     this.hospitals.push(facility);
//                 } else if (element.tags.healthcare === 'blood_donation') {
//                     this.bloodBanks.push(facility);
//                 } else if (element.tags.social_facility === 'ngo') {
//                     this.ngos.push(facility);
//                 }
//             }
//         });
//
//         this.updateHospitalList();
//     }
//
//     updateHospitalList() {
//         const hospitalList = document.getElementById('hospitalList');
//         hospitalList.innerHTML = '';
//
//         // Combine all facilities
//         const allFacilities = [
//             ...this.hospitals.map(h => ({ ...h, type: 'Hospital' })),
//             ...this.bloodBanks.map(b => ({ ...b, type: 'Blood Bank' })),
//             ...this.ngos.map(n => ({ ...n, type: 'NGO' }))
//         ];
//
//         allFacilities.forEach(facility => {
//             const item = document.createElement('div');
//             item.className = 'hospital-item';
//             item.innerHTML = `
//                 <h3 class="font-bold">${facility.name}</h3>
//                 <p class="text-sm text-gray-400">${facility.type}</p>
//                 <p class="text-sm">${facility.address}</p>
//                 <p class="text-sm">📞 ${facility.phone}</p>
//             `;
//             hospitalList.appendChild(item);
//
//             // Add click event to center map on facility
//             item.addEventListener('click', () => {
//                 this.map.setView([facility.lat, facility.lon], 16);
//                 L.popup()
//                     .setLatLng([facility.lat, facility.lon])
//                     .setContent(`
//                         <strong>${facility.name}</strong><br>
//                         ${facility.address}<br>
//                         Phone: ${facility.phone}
//                     `)
//                     .openOn(this.map);
//             });
//         });
//     }
//
//     showFacilities(type) {
//         this.markersLayer.clearLayers();
//
//         let facilities = [];
//         let icon;
//
//         switch(type) {
//             case 'hospitals':
//                 facilities = this.hospitals;
//                 icon = this.createIcon('🏥', 'blue');
//                 break;
//             case 'bloodBanks':
//                 facilities = this.bloodBanks;
//                 icon = this.createIcon('🩸', 'red');
//                 break;
//             case 'ngos':
//                 facilities = this.ngos;
//                 icon = this.createIcon('🤝', 'green');
//                 break;
//         }
//
//         facilities.forEach(facility => {
//             const marker = L.marker([facility.lat, facility.lon], { icon })
//                 .bindPopup(`
//                     <strong>${facility.name}</strong><br>
//                     Address: ${facility.address}<br>
//                     Phone: ${facility.phone}
//                 `);
//             this.markersLayer.addLayer(marker);
//         });
//
//         this.map.addLayer(this.markersLayer);
//     }
//
//     createIcon(emoji, color) {
//         return L.divIcon({
//             className: 'custom-marker',
//             html: `<div style="background-color: ${color}; padding: 5px; border-radius: 50%;">${emoji}</div>`,
//             iconSize: [30, 30]
//         });
//     }
// }
//
// // Initialize the map when the document is ready
// document.addEventListener('DOMContentLoaded', () => {
//     new BloodDonationMap();
//
//     // Add resize handler to ensure map renders correctly
//     window.addEventListener('resize', () => {
//         if (window.map) {
//             window.map.invalidateSize();
//         }
//     });
// });


class BloodDonationMap {
    constructor() {
        this.map = null;
        this.userMarker = null;
        this.markersLayer = L.markerClusterGroup({
            maxClusterRadius: 50,
            spiderfyOnMaxZoom: true,
            showCoverageOnHover: true,
            zoomToBoundsOnClick: true
        });
        this.hospitals = [];
        this.bloodBanks = [];
        this.ngos = [];
        this.initMap();
    }

    initMap() {
        // Initialize the map with new dimensions
        this.map = L.map('map', {
            center: [28.6139, 77.2090],
            zoom: 13,
            minZoom: 3,
            maxZoom: 18
        });

        // Add OpenStreetMap tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(this.map);

        // Allow map to handle its own size
        this.map.invalidateSize();

        // Get user's location
        this.getUserLocation();
    }

    addFilterButtons() {
        // Create filter buttons container
        const filterContainer = document.createElement('div');
        filterContainer.className = 'flex space-x-2 mt-4';
        filterContainer.innerHTML = `
            <button id="showHospitals" class="bg-blue-500 text-white px-3 py-1 rounded text-sm">Hospitals</button>
            <button id="showBloodBanks" class="bg-red-500 text-white px-3 py-1 rounded text-sm">Blood Banks</button>
            <button id="showNGOs" class="bg-green-500 text-white px-3 py-1 rounded text-sm">NGOs</button>
        `;

        // Insert buttons after the map
        document.getElementById('map').parentNode.insertBefore(filterContainer, document.getElementById('map').nextSibling);

        // Add event listeners
        document.getElementById('showHospitals').addEventListener('click', () => this.showFacilities('hospitals'));
        document.getElementById('showBloodBanks').addEventListener('click', () => this.showFacilities('bloodBanks'));
        document.getElementById('showNGOs').addEventListener('click', () => this.showFacilities('ngos'));
    }

    getUserLocation() {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const { latitude, longitude } = position.coords;
                    this.map.setView([latitude, longitude], 13);

                    // Add user marker
                    if (this.userMarker) {
                        this.map.removeLayer(this.userMarker);
                    }
                    this.userMarker = L.marker([latitude, longitude], {
                        icon: L.divIcon({
                            className: 'user-marker',
                            html: '📍',
                            iconSize: [25, 25]
                        })
                    }).addTo(this.map);

                    // Search for nearby facilities
                    this.searchNearbyFacilities(latitude, longitude);
                },
                (error) => {
                    console.error("Error getting location:", error);
                    alert("Unable to access your location. Please enable location services or try again.");

                    // Fallback to a default location if geolocation fails
                    this.map.setView([28.6139, 77.2090], 13);
                    this.searchNearbyFacilities(28.6139, 77.2090);
                }
            );
        } else {
            console.error("Geolocation is not available in this browser.");
            alert("Geolocation is not available in this browser.");

            // Fallback to a default location if geolocation is not available
            this.map.setView([28.6139, 77.2090], 13);
            this.searchNearbyFacilities(28.6139, 77.2090);
        }
    }

    async searchNearbyFacilities(latitude, longitude) {
        const radius = 20000; // 5km radius
        const query = `
        [out:json][timeout:25];
        (
            node["amenity"="hospital"](around:${radius},${latitude},${longitude});
            node["healthcare"="hospital"](around:${radius},${latitude},${longitude});
            node["healthcare"="blood_donation"](around:${radius},${latitude},${longitude});
            node["social_facility"="ngo"](around:${radius},${latitude},${longitude});
        );
        out body;
        >;
        out skel qt;
        `;

        try {
            const response = await fetch('https://overpass-api.de/api/interpreter', {
                method: 'POST',
                body: query
            });
            const data = await response.json();
            this.processResults(data.elements);
            this.showFacilities('hospitals'); // Show hospitals by default
        } catch (error) {
            console.error('Error fetching nearby facilities:', error);
            alert('Error fetching nearby facilities. Please try again later.');
        }
    }

    processResults(elements) {
        this.hospitals = [];
        this.bloodBanks = [];
        this.ngos = [];

        elements.forEach(element => {
            if (element.type === 'node') {
                const facility = {
                    lat: element.lat,
                    lon: element.lon,
                    name: element.tags.name || 'Unnamed Facility',
                    address: element.tags['addr:full'] || element.tags['addr:street'] || '',
                    phone: element.tags.phone || 'N/A'
                };

                if (element.tags.amenity === 'hospital' || element.tags.healthcare === 'hospital') {
                    this.hospitals.push(facility);
                } else if (element.tags.healthcare === 'blood_donation') {
                    this.bloodBanks.push(facility);
                } else if (element.tags.social_facility === 'ngo') {
                    this.ngos.push(facility);
                }
            }
        });

        this.updateHospitalList();
    }

    updateHospitalList() {
        const hospitalList = document.getElementById('hospitalList');
        hospitalList.innerHTML = '';

        // Combine all facilities
        const allFacilities = [
            ...this.hospitals.map(h => ({ ...h, type: 'Hospital' })),
            ...this.bloodBanks.map(b => ({ ...b, type: 'Blood Bank' })),
            ...this.ngos.map(n => ({ ...n, type: 'NGO' }))
        ];

        allFacilities.forEach(facility => {
            const item = document.createElement('div');
            item.className = 'hospital-item';
            item.innerHTML = `
                <h3 class="font-bold">${facility.name}</h3>
                <p class="text-sm text-gray-400">${facility.type}</p>
                <p class="text-sm">${facility.address}</p>
                <p class="text-sm">📞 ${facility.phone}</p>
            `;
            hospitalList.appendChild(item);

            // Add click event to center map on facility
            item.addEventListener('click', () => {
                this.map.setView([facility.lat, facility.lon], 16);
                L.popup()
                    .setLatLng([facility.lat, facility.lon])
                    .setContent(`
                        <strong>${facility.name}</strong><br>
                        ${facility.address}<br>
                        Phone: ${facility.phone}
                    `)
                    .openOn(this.map);
            });
        });
    }

    showFacilities(type) {
        this.markersLayer.clearLayers();

        let facilities = [];
        let icon;

        switch(type) {
            case 'hospitals':
                facilities = this.hospitals;
                icon = this.createIcon('🏥', 'blue');
                break;
            case 'bloodBanks':
                facilities = this.bloodBanks;
                icon = this.createIcon('🩸', 'red');
                break;
            case 'ngos':
                facilities = this.ngos;
                icon = this.createIcon('🤝', 'green');
                break;
        }

        facilities.forEach(facility => {
            const marker = L.marker([facility.lat, facility.lon], { icon })
                .bindPopup(`
                    <strong>${facility.name}</strong><br>
                    Address: ${facility.address}<br>
                    Phone: ${facility.phone}
                `);
            this.markersLayer.addLayer(marker);
        });

        this.map.addLayer(this.markersLayer);
    }

    createIcon(emoji, color) {
        return L.divIcon({
            className: 'custom-marker',
            html: `<div style="background-color: ${color}; padding: 5px; border-radius: 50%;">${emoji}</div>`,
            iconSize: [30, 30]
        });
    }
}

// Initialize the map when the document is ready
document.addEventListener('DOMContentLoaded', () => {
    new BloodDonationMap();

    // Add resize handler to ensure map renders correctly
    window.addEventListener('resize', () => {
        if (window.map) {
            window.map.invalidateSize();
        }
    });
});