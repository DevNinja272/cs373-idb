myApp.controller('UniversityCtrl',
    ['$scope',
    function($scope) {
        /*$scope.sortType     = 'title';
        $scope.sortReverse  = false; 
        $scope.currentPage  = 1; 
*/
        data = {"metadata":{"total":88,"page":2,"per_page":3},"results":[{"cost":22544,"school.name":"Stephen F Austin State University","school.ownership":1,"school.school_url":"www.sfasu.edu","size":10692},{"cost":37444,"school.name":"Texas Lutheran University","school.ownership":2,"school.school_url":"www.tlu.edu","size":1270},{"cost":18039,"school.name":"West Texas A & M University","school.ownership":1,"school.school_url":"www.wtamu.edu","size":7121}]}
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

myApp.controller('StateCtrl',
    ['$scope',
    function($scope) {
        /*$scope.sortType     = 'title';
        $scope.sortReverse  = false; 
        $scope.currentPage  = 1; 
*/
        data = {"results":[{"average_public_cost":35987,"name": "Texas","average_private_cost":67234,"schools":98,"region":"SouthWest"},{"average_public_cost":40726,"name": "Florida","average_private_cost":57873,"schools":54,"region":"SouthEast"},{"average_public_cost":35733,"name": "Utah","average_private_cost":61283,"schools":10,"region":"Rocky Mountains"}]}
        $scope.results = data["results"]
    }]);