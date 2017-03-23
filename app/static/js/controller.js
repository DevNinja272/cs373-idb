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
                github[author.login].issues        = 0;
                stats.commits   += data[i].total;
            }
        });

        IssueFactory.success(function(data) {
            for(var i = 0; i < data.length; i++) {
                github[data[i].user.login].issues += 1;
                stats.issues   += 1;
            }
        });

        $scope.members      = AboutFactory.fetchMember();

        for(var i = 0; i < $scope.members.length; i++) { stats.tests     += $scope.members[i].tests;}
            
        $scope.dataUsed     = AboutFactory.fetchAPI();
        $scope.tools        = AboutFactory.fetchTool();
        $scope.information  = AboutFactory.fetchInformation();
        $scope.github       = github;
        $scope.stats        = stats;

    }]);