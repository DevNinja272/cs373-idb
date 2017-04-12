myApp.controller('SplashCtrl',
    ['$scope', '$location',
    function($scope, $location) {



        $scope.stringSearch = function(searchString)
        {
            var parsedStringArray = searchString.split(" ");
            var currentString = "";

            for (var i = 0; i < parsedStringArray.length; i++)
            {
                currentString = parsedStringArray[i];

                currentString = parsedStringArray[i];
                console.log(parsedStringArray);
                $location.search('param'+i, currentString);
            }
            var paramString = '/search' + $location.url();
            console.log(paramString);
        };

    }]);

myApp.controller('UniversityCtrl',
    ['$scope', 'UniversityFactory',
    function($scope, UniversityFactory) {
        UniversityFactory.fetch().success(function(data){
            results = data['universities'];

            for(var i = 0; i < results.length; i++){
                if (results[i]['is_public'] == true){
                    results[i]['is_public'] = 'Public';
                }
                else{
                    results[i]['is_public'] = 'Private';
                }
            }
            $scope.results = results;
        });

        $scope.itemsByPage=15;
    }]);

myApp.controller('UniversitySpecificCtrl',
    ['$scope', '$routeParams', 'UniversityFactory', '$sce',
    function($scope, $routeParams, UniversityFactory, $sce) {
        UniversityFactory.fetchAt($routeParams['id']).success(function(data){
            results = data['university'];

            if (results['is_public'] == true){
                results['is_public'] = 'Public';
            }
            else{
                results['is_public'] = 'Private';
            }
            results['logo_url'] = "//logo.clearbit.com/" + results["website_URL"];
            map = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAA3kVukykkAMpTnVPdV4cnM-C0c4NqitE  &q=" + results["name"].replace('&', '');
            $scope.map = $sce.trustAsResourceUrl(map);
            $scope.results = results;
        });
    }]);

myApp.controller('StateCtrl',
    ['$scope', 'StateFactory',
    function($scope, StateFactory) {
        StateFactory.fetch().success(function(data){
            results = data['states'];

            for (var i = 0; i < results.length; i++){
                results[i]["map_url"] = "http://www.50states.com/maps/" + results[i]["name"].toLowerCase()+ ".gif";
            }

            $scope.results = results;
        });
    }]);

myApp.controller('StateSpecificCtrl',
    ['$scope', '$routeParams', 'StateFactory',
    function($scope, $routeParams, StateFactory) {
        StateFactory.fetchAt($routeParams['id']).success(function(data){
            results = data['state'];
            results["map_url"] = "http://www.50states.com/maps/" + results["name"].toLowerCase().replace(/ /g,"_") + ".gif";
            $scope.results = results;
        });    
    }]);

myApp.controller('DegreeCtrl',
    ['$scope', 'DegreeFactory',
    function($scope, DegreeFactory) {
        DegreeFactory.fetch().success(function(data){
            results = data['degrees'];
            $scope.results = results;
        });
    }]);

myApp.controller('DegreeSpecificCtrl',
    ['$scope', '$routeParams', 'DegreeFactory',
    function($scope, $routeParams, DegreeFactory) {
        DegreeFactory.fetchAt($routeParams['id']).success(function(data){
            results = data['degree'];
            $scope.results = results;
        });
    }]);

myApp.controller('AboutCtrl',
    ['$scope', '$http', 'GithubFactory', 'IssueFactory', 'AboutFactory',
    function($scope, $http, GithubFactory, IssueFactory, AboutFactory) {

        stats               = {issues:0, tests:0, commits:0};
        github              = {};

        GithubFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                author = data[i]['author']
                github[author.login] = {};
                github[author.login].avatar_url    = author.avatar_url;
                github[author.login].url           = author.html_url;
                github[author.login].contributions = data[i].total;
                //github[author.login].issues        = 0;
                stats.commits   += data[i].total;
            }
        });

        GithubFactory.success(function(data) {
            sean = data[0]['author'];
            jin = data[1]['author'];
            aye = data[2]['author'];
            ben = data[3]['author'];
            ald = data[4]['author'];

            github[sean.login].issues = 6
            github[jin.login].issues = 6
            github[aye.login].issues = 6
            github[ben.login].issues = 8
            github[ald.login].issues = 5
            stats.issues = github[sean.login].issues + github[jin.login].issues + github[aye.login].issues + github[ben.login].issues + github[ald.login].issues; 
        });

$scope.members      = AboutFactory.fetchMember();

for(var i = 0; i < $scope.members.length; i++) { stats.tests     += $scope.members[i].tests;}

    $scope.github       = github;
    $scope.stats        = stats;

$scope.runUnittests = function () {
    $http.get('/runtests').success(function(data) {
        $scope.tests = data
    });
}
}]);