/*
  ************************************************
  *   Interop controller and AngularJS handeler  * 
  *    for the controller on the interop side.   *
  *                                              *
  *             Author: David Kroell             *
  *            Version: 1.0.0                    *
  *                                              *
  ************************************************
*/


angular.module('MISCONSYS')
    .config(['$routeProvider', '$locationProvider',
	     function($routeProvider, $locationProvider) {

		 // Route functionality for the interop
		 // section of the application

		 $routeProvider
		     .when('/interop', {
			 templateUrl: './interop/interop.html',
			 controller: 'InteropController',
			 controllerAs: 'vm',
			 css: './interop/interop.css'
		     });	 
	     }])
	    .controller("InteropController", function($scope) {
		var vm = this;
		
	    });
