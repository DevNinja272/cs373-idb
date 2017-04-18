myApp.factory('PFactory', function($http) { 

return {
  fetchP: function () {
    return $http.get('/smash/participants')
  },

  fetchT: function () {
    return $http.get('/smash/tournaments')
  },

  fetchC: function () {
    return $http.get('/smash/characters')
  },
};
});



myApp.factory('UniversityFactory', function($http) { 

return {
  fetch: function () {
    return $http.get('/api/universities')
  },
  fetchAt: function (id) {
    return $http.get('/api/universities/' + id)
  },
};
});

myApp.factory('StateFactory', function($http) { 

  return {
    fetch: function () {
      return $http.get('/api/states');
    },
    fetchAt: function (id) {
      return $http.get('/api/states/' + id);
    },
  };
});

myApp.factory('DegreeFactory', function($http) { 

  return {
    fetch: function () {
      return $http.get('/api/degrees');
    },
    fetchAt: function (id) {
      return $http.get('/api/degrees/' + id);
    },
  };
});

myApp.factory('GithubFactory', function($http) { 
  return $http.get('https://api.github.com/repos/JinwookKim/cs373-idb/stats/contributors');
});

myApp.factory('IssueFactory', function($http) { 
  return $http.get('https://api.github.com/repos/JinwookKim/cs373-idb/issues?per_page=500&state=all');
});

myApp.factory('AboutFactory', function() {

  var memberCache = [
  {
    name: 'Jinwook Kim', 
    login: 'JinwookKim',
    description: "Hi, I'm Jin. I am a senior at UT Austin. I like to learn foreign & programming languages.",
    responsibilities: 'Frontend', 
    tests: 0
  },
  {
    name:'Ben Nguyen', 
    login: 'bpn252',
    description: "I'm Ben, I am a junior and will hopefully graduate Fall 2017. I enjoy playing Rocket League and reading awful fanfiction.",
    responsibilities: 'Full Stack', 
    tests: 0
  },
  {
    name: 'Faisal Aldilaijan', 
    login: 'aldilaff', 
    description: "My name is Faisal and I am a senior studying Computer Science at UT Austin. I like to bike around Austin",
    responsibilities:'Backend', 
    tests: 5
  },
  {
    name:'Sean Wang',
    login: 'seanyusa',
    description: "I'm Sean and I am a Junior Computer Science major at the University of Texas at Austin. In my free time I like to hang out with friends, go swimming, and study the Bible.",
    responsibilities:'Backend',
    tests: 5
  },
  {
    name: 'Ahmed Al Nabil', 
    login: 'ayenabil',
    description:"My name is Ahmed and I'm a sophomore studying computer science with a business certificate. Some of my interests include dancing, drawing, and going on adventures.",
    responsibilities: 'Backend', 
    tests: 5
  },
  ];
  return {
    fetchMember: function () {
      return memberCache;
    }
  };
});