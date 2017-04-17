'use strict';

var myApp = angular.module('myApp', [
 'ngRoute','smart-table', 'chart.js',
]);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/splash.html',
                 controller: 'SplashCtrl'
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html',
                 controller: 'AboutCtrl'
             }).
             when('/universities', {
                 templateUrl: '../static/partials/universities.html',
                 controller: 'UniversityCtrl'
             }).
             when('/universities/:id', {
                 templateUrl: '../static/partials/universitySpecific.html',
                 controller: 'UniversitySpecificCtrl'
             }).
             when('/states', {
                 templateUrl: '../static/partials/states.html',
                 controller: 'StateCtrl'
             }).
             when('/states/:id', {
                 templateUrl: '../static/partials/stateSpecific.html',
                 controller: 'StateSpecificCtrl'
             }).
             when('/degrees', {
                 templateUrl: '../static/partials/degrees.html',
                 controller: 'DegreeCtrl'
             }).
             when('/degrees/:id', {
                 templateUrl: '../static/partials/degreeSpecific.html',
                 controller: 'DegreeSpecificCtrl'
             }).
            when('/smashdb', {
                 templateUrl: '../static/partials/smashdb.html',
                 controller: 'SmashdbCtrl'
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);