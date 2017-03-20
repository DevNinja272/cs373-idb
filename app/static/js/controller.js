myApp.controller('UniversityCtrl',
    ['$scope',
    function($scope) {
        /*$scope.sortType     = 'title';
        $scope.sortReverse  = false; 
        $scope.currentPage  = 1; 
*/
        data = 
        {"metadata":{"total":88,"page":2,"per_page":3},"results":[
        {"id":1, "cost":22544,"school.name":"Stephen F Austin State University","school.ownership":1,"school.school_url":"www.sfasu.edu","size":10692},
        {"id":2, "cost":37444,"school.name":"Texas Lutheran University","school.ownership":2,"school.school_url":"www.tlu.edu","size":1270},
        {"id":3, "cost":18039,"school.name":"West Texas A & M University","school.ownership":1,"school.school_url":"www.wtamu.edu","size":7121}]}
        for(var i = 0; i < data.results.length; i++) {
            if (data.results[i]["school.ownership"] == 1){
                data.results[i]["school.ownership"] = "Public";
            }
            else{
                data.results[i]["school.ownership"] = "Private";
            }
        }
        $scope.results = data["results"]
    }]);

myApp.controller('UniversitySpecificCtrl',
    ['$scope',
    function($scope) {
        $scope.hello = 'hello from university specific!'
        
    }]);

myApp.controller('StateCtrl',
    ['$scope',
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
    ['$scope',
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