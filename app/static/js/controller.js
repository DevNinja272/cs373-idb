myApp.controller('UniversityCtrl',
    ['$scope', 'UniversityFactory',
    function($scope, UniversityFactory) {
        $scope.results = UniversityFactory.fetch();
    }]);

myApp.controller('UniversitySpecificCtrl',
    ['$scope', '$routeParams', 'UniversityFactory',
    function($scope, $routeParams, UniversityFactory) {
        $scope.results = UniversityFactory.fetchAt($routeParams['id']);
    }]);

myApp.controller('StateCtrl',
    ['$scope', 'StateFactory',
    function($scope, StateFactory) {
        $scope.results = StateFactory.fetch();
    }]);

myApp.controller('StateSpecificCtrl',
    ['$scope', '$routeParams', 'StateFactory',
    function($scope, $routeParams, StateFactory) {
        $scope.results = StateFactory.fetchAt($routeParams['id']);
    }]);

myApp.controller('DegreeCtrl',
    ['$scope', 'DegreeFactory',
    function($scope, DegreeFactory) {
        $scope.results = DegreeFactory.fetch();
    }]);

myApp.controller('DegreeSpecificCtrl',
    ['$scope', '$routeParams', 'DegreeFactory',
    function($scope, $routeParams, DegreeFactory) {
        $scope.results = DegreeFactory.fetchAt($routeParams['id']);
    }]);