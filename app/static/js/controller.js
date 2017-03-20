myApp.controller('UniversityCtrl',
    ['$scope', 'UniversityFactory',
    function($scope, UniversityFactory) {
        /*$scope.sortType     = 'title';
        $scope.sortReverse  = false; 
        $scope.currentPage  = 1; 
*/
        UniversityFactory.fetch().then(function(data)
        {
            $scope.results = data["results"];
        });
    }]);

myApp.controller('UniversitySpecificCtrl',
    ['$scope', '$routeParams', 'UniversityFactory',
    function($scope, $routeParams, UniversityFactory) {
        UniversityFactory.fetchAt($routeParams['id']).then(function(data)
        {
            $scope.results = data;
        });
    }]);

myApp.controller('StateCtrl',
    ['$scope', 'StateFactory',
    function($scope) {
        /*$scope.sortType     = 'title';
        $scope.sortReverse  = false; 
        $scope.currentPage  = 1; 
*/
        data = 
        {"results":[
        {"id":1, "average_public_cost":35987,"name": "Texas","average_private_cost":67234,"schools":98,"region":"SouthWest"},
        {"id":2, "average_public_cost":40726,"name": "Florida","average_private_cost":57873,"schools":54,"region":"SouthEast"},
        {"id":3, "average_public_cost":35733,"name": "Utah","average_private_cost":61283,"schools":10,"region":"Rocky Mountains"}]}
        $scope.results = data["results"]
    }]);

myApp.controller('StateSpecificCtrl',
    ['$scope',
    function($scope) {
        $scope.hello = 'hello from state specific!'
        
    }]);

myApp.controller('DegreeCtrl',
    ['$scope', 'DegreeFactory',
    function($scope) {
        /*$scope.sortType     = 'title';
        $scope.sortReverse  = false; 
        $scope.currentPage  = 1; 
*/
        data = 
        {"results":[
        {"id":1, "name": "Education","numPub":3423,"numPriv":1231,"AwardedPub":"10%","AwardedPriv":"25%" },
        {"id":2, "name": "Engineering","numPub":4213,"numPriv":2349,"AwardedPub":"17%","AwardedPriv":"12%"},
        {"id":3, "name": "Psychology","numPub":1023,"numPriv":976,"AwardedPub":"11%","AwardedPriv":"5%"}]}
        $scope.results = data["results"]
    }]);

myApp.controller('DegreeSpecificCtrl',
    ['$scope',
    function($scope) {
        $scope.hello = 'hello from degree specific'
        
    }]);