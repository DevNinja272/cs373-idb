myApp.controller('SmashdbCtrl',
    ['$scope', 'PFactory',
    function($scope, PFactory) {
          
          PFactory.fetchP().success(function(data){
                results = data['participants'];
                var map = {}
                for (var i = 0; i < results.length; i++){
                    if (map.hasOwnProperty(results[i]['location'] )){
                        map[results[i]['location']] +=  1;
                    }else if (results[i]['location'].length > 0){
                        map[results[i]['location']] = 1;
                    }
                }
                $scope.labels = [];
                $scope.data = [];
                $scope.options = {
                    legend: {display: true},
                    title: {display: true, text: "Most Popular Countries/States/Provinces", fontSize: 20}
                };
                for (var key in map){
                    if (map.hasOwnProperty(key) && map[key] > 100) {
                        $scope.labels.push(key);
                        $scope.data.push(map[key]);
                    }      
                }


                var map3 = {}
                for (var i = 0; i < results.length; i++){
                    if (map3.hasOwnProperty(results[i]['main'] )){
                        map3[results[i]['main']] +=  1;
                    }else if (results[i]['main'].length > 0){
                        map3[results[i]['main']] = 1;
                    }
                }
                $scope.labels3 = [];
                $scope.data3 = [];
                $scope.options3 = {
                    legend: {display: false},
                    title: {display: true, text: "Most Popular Characters", fontSize: 20}
                };
                for (var key in map3){
                    if (map3.hasOwnProperty(key) && map3[key] > 120) {
                        $scope.labels3.push(key);
                        $scope.data3.push(map3[key]);
                    }      
                }

          });

          PFactory.fetchT().success(function(data){
                results = data['tournaments'];
                var map2 = {}
                for (var i = 0; i < results.length; i++){
                    if (map2.hasOwnProperty(results[i]['location'] )){
                        map2[results[i]['location']] +=  1;
                    }else if (results[i]['location'].length > 0){
                        map2[results[i]['location']] = 1;
                    }
                }
                $scope.labels2 = [];
                $scope.data2 = [];
                $scope.options2 = {
                    legend: {display: true},
                    title: {display: true, text: "Most Popular Tournament Locations", fontSize: 20}
                };
                for (var key in map2){
                    if (map2.hasOwnProperty(key)) {
                        $scope.labels2.push(key);
                        $scope.data2.push(map2[key]);
                    }      
                }

                var map4 = {}
                for (var i = 0; i < results.length; i++){
                    var date = results[i]['date'].split(" ");
                    var month = date[1];
                    if (map4.hasOwnProperty(month )){
                        map4[month] +=  1;
                    }else if (month.length >= 0){
                        map4[month] = 1;
                    }
                }
                $scope.labels4 = [];
                $scope.data4 = [];
                $scope.options4 = {
                    legend: {display: false},
                    title: {display: true, text: "Most Popular Months for Tournaments", fontSize: 20}
                };
                for (var key in map4){
                    if (map4.hasOwnProperty(key)) {
                        $scope.labels4.push(key);
                        $scope.data4.push(map4[key]);
                    }      
                }
          });

          PFactory.fetchC().success(function(data){
                results = data['characters'];
                var map5 = {};
                var map5Weight = {}
                for (var i = 0; i < results.length; i++){
                    if (map5.hasOwnProperty(results[i]['tier'] )){
                        map5[results[i]['tier']] +=  1;
                        map5Weight[results[i]['tier']] +=  0;
                    }else if (results[i]['tier'].length > 0){
                        map5[results[i]['tier']] = 1;
                        map5Weight[results[i]['tier']] = 0;
                    }
                }
                for (var i = 0; i < results.length; i++){
                    var tier = results[i]["tier"];
                    var weight = results[i]["weight"];
                    map5Weight[tier] += weight;
                }

                for (var key in map5){
                    map5Weight[key] = map5Weight[key] / map5[key]; 
                }
                console.log(map5Weight);
                console.log(map5);
                $scope.labels5 = [];
                $scope.data5 = [];
                $scope.options5 = {
                    legend: {display: true},
                    title: {display: true, text: "Average Character Weight Per Tier", fontSize: 20}
                };
                for (var key in map5Weight){
                    if (map5Weight.hasOwnProperty(key)) {
                        $scope.labels5.push(key);
                        $scope.data5.push(map5Weight[key]);
                    }      
                }
                
          });
    }]);


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