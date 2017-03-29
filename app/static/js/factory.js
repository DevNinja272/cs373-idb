myApp.factory('UniversityFactory', function() { 
  universities = 
  {"results":[
  {"entry_id":0, "cost":22544,"school.name":"Stephen F Austin State University","school.ownership":1,"school.school_url":"www.sfasu.edu","size":10692, "state": "Texas", "state_id": 0, 

  "degrees":[
  {"degree_id":0, "degree_name": "Education"},
  {"degree_id":1, "degree_name": "Engineering"},
  {"degree_id":2, "degree_name": "Psychology"},
  ]

},{"entry_id":3, "cost":22544,"school.name":"Stephen F Austin State University","school.ownership":1,"school.school_url":"www.sfasu.edu","size":10692, "state": "Texas", "state_id": 0, 

  "degrees":[
  {"degree_id":0, "degree_name": "Education"},
  {"degree_id":1, "degree_name": "Engineering"},
  {"degree_id":2, "degree_name": "Psychology"},
  ]

},

{"entry_id":1, "cost":37444,"school.name":"Texas Lutheran University","school.ownership":2,"school.school_url":"www.tlu.edu","size":1270, "state": "Texas", "state_id": 0, 
"degrees":[
{"degree_id":0, "degree_name": "Education"},
{"degree_id":1, "degree_name": "Engineering"},
{"degree_id":2, "degree_name": "Psychology"},
]},

{"entry_id":2, "cost":18039,"school.name":"West Texas A & M University","school.ownership":1,"school.school_url":"www.wtamu.edu","size":7121, "state": "Texas", "state_id": 0, 
"degrees":[
{"degree_id":0, "degree_name": "Education"},
{"degree_id":1, "degree_name": "Engineering"},
{"degree_id":2, "degree_name": "Psychology"},
]}

]};

function compare(a,b) {
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
  universities.results[i]["map"] = "https://www.google.com/maps/embed/v1/place?key=AIzaSyCM8BIbDS3-fO09MF7_bz1p3QJgidR9kfc&q=" + universities.results[i]["school.name"].replace('&', '');;
}
return {
  fetch: function () {
    return universities.results;
  },
  fetchAt: function (id) {
    return universities.results[id];
  },
};
});

myApp.factory('StateFactory', function() { 

  states = 
  {"results":[
  {"entry_id":0, "average_public_cost":35987,"name": "Texas","average_private_cost":67234,"schools":98,"region":"SouthWest",
  "universities":[
  {"university_id": 0, "university_name": "Stephen F Austin State University"},
  {"university_id": 1, "university_name": "Texas Lutheran University"},
  {"university_id": 2, "university_name": "West Texas A & M University"},
  ]},
  {"entry_id":1, "average_public_cost":40726,"name": "Florida","average_private_cost":57873,"schools":54,"region":"SouthEast"},
  {"entry_id":2, "average_public_cost":35733,"name": "Utah","average_private_cost":61283,"schools":10,"region":"Rocky Mountains"}]}

  function compare(a,b) {
  if (a.entry_id < b.entry_id)
    return -1;
  if (a.entry_id > b.entry_id)
    return 1;
  return 0;
  }

  states.results.sort(compare);

  for (var i = 0; i < states.results.length; i++){
    states.results[i]["map_url"] = "http://www.50states.com/maps/" + states.results[i]["name"] + ".gif";
  }

  return {
    fetch: function () {
      return states.results;
    },
    fetchAt: function (id) {
      return states.results[id];
    },
  };
});

myApp.factory('DegreeFactory', function() { 

  degrees = 
  {"results":[
  {"entry_id":0, "name": "Education","numPub":3423,"numPriv":1231,"AwardedPub":10,"AwardedPriv":25, 
  "universities":[
  {"university_id": 0, "university_name": "Stephen F Austin State University"},
  {"university_id": 1, "university_name": "Texas Lutheran University"},
  {"university_id": 2, "university_name": "West Texas A & M University"},
  ]},

  {"entry_id":1, "name": "Engineering","numPub":4213,"numPriv":2349,"AwardedPub":17,"AwardedPriv":12,
  "universities":[
  {"university_id": 0, "university_name": "Stephen F Austin State University"},
  {"university_id": 1, "university_name": "Texas Lutheran University"},
  {"university_id": 2, "university_name": "West Texas A & M University"},
  ]},
  {"entry_id":2, "name": "Psychology","numPub":1023,"numPriv":976,"AwardedPub":11,"AwardedPriv":5,
  "universities":[
  {"university_id": 0, "university_name": "Stephen F Austin State University"},
  {"university_id": 1, "university_name": "Texas Lutheran University"},
  {"university_id": 2, "university_name": "West Texas A & M University"},]},

  {"entry_id":3, "name": "Psychology","numPub":1023,"numPriv":976,"AwardedPub":11,"AwardedPriv":5,
  "universities":[
  {"university_id": 0, "university_name": "Stephen F Austin State University"},
  {"university_id": 1, "university_name": "Texas Lutheran University"},
  {"university_id": 2, "university_name": "West Texas A & M University"},]},

  {"entry_id":4, "name": "Psychology","numPub":1023,"numPriv":976,"AwardedPub":11,"AwardedPriv":5,
  "universities":[
  {"university_id": 0, "university_name": "Stephen F Austin State University"},
  {"university_id": 1, "university_name": "Texas Lutheran University"},
  {"university_id": 2, "university_name": "West Texas A & M University"},]}
  ]}

  function compare(a,b) {
  if (a.entry_id < b.entry_id)
    return -1;
  if (a.entry_id > b.entry_id)
    return 1;
  return 0;
  }

  degrees.results.sort(compare);

  return {
    fetch: function () {
      return degrees.results;
    },
    fetchAt: function (id) {
      return degrees.results[id];
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

  var informationCache = [
    { name: 'Apiary',               link: 'http://docs.collegedb.apiary.io/#'},
    { name: 'Github Issue Tracker', link: 'https://github.com/JinwookKim/cs373-idb/issues'},
    { name: 'Github Repository',    link: 'https://github.com/JinwookKim/cs373-idb'},
    { name: 'Github Wiki',          link: 'https://github.com/JinwookKim/cs373-idb/wiki'}
  ];

  var toolCache = [
    { name: 'AngularJS',   link: 'https://angularjs.org/'},
    { name: 'BootstrapJS', link: 'http://getbootstrap.com/'},
    { name: 'Flask',       link: 'http://flask.pocoo.org/'},
    { name: 'SQLAlchemy',  link: 'http://www.sqlalchemy.org/'},
    { name: 'yUML',        link: 'http://yuml.me/'}
  ];

  var apiCache = [
    { name: 'College API',      link: 'https://collegescorecard.ed.gov/data/documentation/'},
    { name: 'API Sign Up Key',  link: 'https://api.data.gov/signup/'},
    { name: 'College Logos',    link: 'https://clearbit.com/logo'},
    { name: 'State Photos',     link: 'http://www.50states.com/maps/'}
  ];

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
    name: 'Nabil Ahmed', 
    login: 'ayenabil',
    description:"My name is Ahmed and I'm a sophomore studying computer science with a business certificate. Some of my interests include dancing, drawing, and going on adventures.",
    responsibilities: 'Backend', 
    tests: 5
  },
  ];
  return {
    fetchAPI: function () {
      return apiCache;
    },
    fetchInformation: function () {
      return informationCache;
    },
    fetchTool: function () {
      return toolCache;
    },
    fetchMember: function () {
      return memberCache;
    }
  };
});