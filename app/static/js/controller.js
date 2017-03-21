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

myApp.controller('AboutCtrl',
    ['$scope', '$http', 'GithubFetchFactory', 'IssueFetchFactory', 'MetadataFetchFactory',
    function($scope, $http, GithubFetchFactory, IssueFetchFactory, MetadataFetchFactory) {

        stats               = {issues:0, tests:0, commits:0};
        refineData          = {};
        totalCommit         = 0;

        GithubFetchFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                author = data[i]['author']
                refineData[author.login] = {};
                refineData[author.login].avatar_url    = author.avatar_url;
                refineData[author.login].url           = author.html_url;
                refineData[author.login].contributions = data[i].total;
                refineData[author.login].issues        = 0;
                stats.commits   += data[i].total;
            }
        });

        IssueFetchFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                refineData[data[i].user.login].issues += 1;
                stats.issues   += 1;
            }
        });

        $scope.members      = MetadataFetchFactory.fetchMember();
        for(var i = 0; i < $scope.members.length; i++) {
            stats.tests     += $scope.members[i].tests;
        }
        $scope.tools        = MetadataFetchFactory.fetchTool();
        $scope.information  = MetadataFetchFactory.fetchInformation();
        $scope.github       = refineData;
        $scope.stats        = stats;

    }]);