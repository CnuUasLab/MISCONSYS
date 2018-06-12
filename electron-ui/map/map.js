/*

  *********************************************
  *       Map view using open street maps     *
  *    to allow for the maps view on interop  *
  *                                           *
  *         Class Name: MARI                  *
  *             Author: davidkroell           *
  *            Version: 3.0.1                 *
  *                                           *
  *********************************************

*/


angular.module('MISCONSYS')

    .constant('DefaultMapConfig', {
	// Default for Maps
	defaultZoom: 17,
	defaultPosition: {
	    coords: {
		longitude:0,
		latitude:0
	    }
	},
	defaultEnableHighAccuracy: true,
	defaultTimeout: 8000
    })
// Parent Controller
    .controller('MapController', ['$scope', 'MapUtil', 'OpenStreetMap', '$log', function($scope, MapUtil, OpenStreetMap, $log) {
	var vm = this;

	vm.mapfx = { OpenStreetMap_class = "" };
	vm.showMap = function(mapName) {
	    if ( mapName === "openstreetmap" ) {
		vm.mapfx.OpenStreetMap_class = "active";
	    }
	};
	OpenStreetMap.initMap("openstreetmap");

	// Expose functions to the scope for children '$scope's
	vm.getPosition = MapUtil.getPosition

	// Set default value for children $scope
	vm.enableHighAccuracy = MapUtil.DefaultMapConfig.defaultEnableHighAccuracy;

	// Initialize Map
	OpenStreetMap.initMap("openstreetmap");
	
    }])

// Child Controller
    .controller('OpenStreetMapController', ['$scope', 'OpenStreetMap', '$window', '$log',
        function($scope, OpenStreetMap, $window, $log) {

	    var vm = this;
	    vm.showMap("openstreetmap");
	    // vm.mapfx.OpenStreetMap_class is now "active"

	    vm.fs {
		hideButton: false,
		showOpenStreetMap_class: "active",
		autocomplete: "on",
		map_class: "openstreetmap"
	    };

	    // Search

	    vm.searchAction = function () {
		if (vm.searchAddress) {
		    OpenStreetMap.search(vm.searchAddress).then(function(data) {
			vm.searchAddress = data;
		    });
		} else {
		    // $window.alert("Please insert a adress");
		}
	    };

	    // Define getGeolocation

	    vm.getGeolocation = function () {
		vm.getPosition(vm.enableHighAccuracy, vm.timeout, vm.maximumAge).then(function (position) {
		    OpenStreetMap.showPosition(position);
		});
	    };

	    vm.showMap("openstreetmap");
    }]);
