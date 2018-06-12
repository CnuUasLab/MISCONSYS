/*

*/


angular.module('MISCONSYS')
    .config(['$routeProvider', '$locationProvider',
	     function($routeProvider, $locationProvider) {

		 // Route functionality for the interop
		 // section of the application

		 $routeProvider
		     .when('/img', {
			 templateUrl: './img/img.html',
			 controller: 'ImgController',
			 controllerAs: 'vm',
			 css: './img/img.css'
		     });	 
	     }])
	    .controller("ImgController", function($scope) {
		var vm = this;
		
	    });
