myApp.factory('UniversityFactory', function($http) { 

/*function compare(a,b) {
  if (a.entry_id < b.entry_id)
    return -1;
  if (a.entry_id > b.entry_id)
    return 1;
  return 0;
}

universities.results.sort(compare);

for(var i = 0; i < universities.results.length; i++) {
  if (universities.results[i]["school.ownership"] == 1){
    universities.results[i]["school.ownership"] = "Public";
  }
  else{
    universities.results[i]["school.ownership"] = "Private";
  }
  universities.results[i]["logo_url"] = "//logo.clearbit.com/" + universities.results[i]["school.school_url"];
  universities.results[i]["map"] = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAA3kVukykkAMpTnVPdV4cnM-C0c4NqitE  &q=" + universities.results[i]["school.name"].replace('&', '');;
}*/
return {
  fetch: function () {
    return $http.get('/api/universities')
  },
  fetchAt: function (id) {
    return $http.get('/api/universities/' + id)
  },
};
});

myApp.factory('StateFactory', function() { 

  // function compare(a,b) {
  // if (a.entry_id < b.entry_id)
  //   return -1;
  // if (a.entry_id > b.entry_id)
  //   return 1;
  // return 0;
  // }

  // states.results.sort(compare);

  // for (var i = 0; i < states.results.length; i++){
  //   states.results[i]["map_url"] = "http://www.50states.com/maps/" + states.results[i]["name"].toLowerCase() + ".gif";
  // }

  return {
    fetch: function () {
      return $http.get('/api/states');
    },
    fetchAt: function (id) {
      return $http.get('/api/states/' + id);
    },
  };
});

myApp.factory('DegreeFactory', function() { 

  // function compare(a,b) {
  // if (a.entry_id < b.entry_id)
  //   return -1;
  // if (a.entry_id > b.entry_id)
  //   return 1;
  // return 0;
  // }

  // degrees.results.sort(compare);

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
    responsibilities: 'Frontend', 
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