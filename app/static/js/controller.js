myApp.controller('UniversityCtrl',
    ['$scope', 'UniversityFactory',
    function($scope, UniversityFactory) {
        $scope.results = UniversityFactory.fetch();
        $scope.itemsByPage=15;
    }]);

myApp.controller('UniversitySpecificCtrl',
    ['$scope', '$routeParams', 'UniversityFactory', '$sce',
    function($scope, $routeParams, UniversityFactory, $sce) {
        $scope.results = UniversityFactory.fetchAt($routeParams['id']);
        $scope.map = $sce.trustAsResourceUrl($scope.results.map);
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
    ['$scope', '$http', 'GithubFactory', 'IssueFactory', 'AboutFactory',
    function($scope, $http, GithubFactory, IssueFactory, AboutFactory) {

        stats               = {issues:0, tests:0, commits:0};
        github              = {};
        totalCommit         = 0;

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

            github[sean.login].issues = 3
            github[jin.login].issues = 6
            github[aye.login].issues = 3
            github[ben.login].issues = 8
            github[ald.login].issues = 4
            stats.issues = github[sean.login].issues + github[jin.login].issues + github[aye.logins] + github[ben.login] + github[ald.login];
        });

/*        IssueFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                github[data[i].user.login].issues += 1;
                stats.issues   += 1;
            }
        });*/

        $scope.members      = AboutFactory.fetchMember();
        for(var i = 0; i < $scope.members.length; i++) {
            stats.tests     += $scope.members[i].tests;
        }
        $scope.dataUsed     = AboutFactory.fetchAPI();
        $scope.tools        = AboutFactory.fetchTool();
        $scope.information  = AboutFactory.fetchInformation();
        $scope.github       = github;
        $scope.stats        = stats;

    }]);