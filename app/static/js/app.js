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
             when('/universities/:universityId', {
                 templateUrl: '../static/partials/universitySpecific.html',
                 controller: 'UniversitySpecificCtrl'
             }).
             when('/states', {
                 templateUrl: '../static/partials/states.html',
                 controller: 'StateCtrl'
             }).
             when('/states/:stateId', {
                 templateUrl: '../static/partials/stateSpecific.html',
                 controller: 'StateSpecificCtrl'
             }).
             when('/degrees', {
                 templateUrl: '../static/partials/degrees.html',
                 controller: 'DegreeCtrl'
             }).
             when('/degrees/:degreeId', {
                 templateUrl: '../static/partials/degreeSpecific.html',
                 controller: 'DegreeSpecificCtrl'
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);