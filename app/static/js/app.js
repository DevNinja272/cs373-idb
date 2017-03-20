'use strict';

var myApp = angular.module('myApp', [
 'ngRoute',
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/search.html',
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html',
             }).
             when('/universities', {
                 templateUrl: '../static/partials/universities.html',
                 controller: 'UniversityCtrl'
             }).
             when('/states', {
                 templateUrl: '../static/partials/states.html',
<<<<<<< HEAD
                 // controller: 'StateCtrl'
=======
                 controller: 'StateCtrl'
>>>>>>> master
             }).
             when('/degrees', {
                 templateUrl: '../static/partials/degrees.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);