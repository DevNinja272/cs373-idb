/*{ 
    "stuff": {
        "onetype": [
            {"id":1,"name":"John Doe"},
            {"id":2,"name":"Don Joeh"}
        ],
        "othertype": {"id":2,"company":"ACME"}
    }, 
    "otherstuff": {
        "thing": [[1,42],[2,2]]
     }
}*/

myApp.factory('UniversityFactory', function() { 
  universities = 
        {"results":[
          {"id":0, "cost":22544,"school.name":"Stephen F Austin State University","school.ownership":1,"school.school_url":"www.sfasu.edu","size":10692, "state": "Texas", "state_id": 0, 
          
          "degrees":[
            {"degree_id":0, "degree_name": "Education"},
            {"degree_id":1, "degree_name": "Engineering"},
            {"degree_id":2, "degree_name": "Psychology"},
          ]

        },

        {"id":1, "cost":37444,"school.name":"Texas Lutheran University","school.ownership":2,"school.school_url":"www.tlu.edu","size":1270, "state": "Texas", "state_id": 0, 
        "degrees":[
            {"degree_id":0, "degree_name": "Education"},
            {"degree_id":1, "degree_name": "Engineering"},
            {"degree_id":2, "degree_name": "Psychology"},
          ]},

        {"id":2, "cost":18039,"school.name":"West Texas A & M University","school.ownership":1,"school.school_url":"www.wtamu.edu","size":7121, "state": "Texas", "state_id": 0, 
        "degrees":[
            {"degree_id":0, "degree_name": "Education"},
            {"degree_id":1, "degree_name": "Engineering"},
            {"degree_id":2, "degree_name": "Psychology"},
          ]}]};
        for(var i = 0; i < universities.results.length; i++) {
            if (universities.results[i]["school.ownership"] == 1){
                universities.results[i]["school.ownership"] = "Public";
            }
            else{
                universities.results[i]["school.ownership"] = "Private";
            }
            universities.results[i]["logo_url"] = "//logo.clearbit.com/" + universities.results[i]["school.school_url"];
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
        {"id":0, "average_public_cost":35987,"name": "Texas","average_private_cost":67234,"schools":98,"region":"SouthWest"},
        {"id":1, "average_public_cost":40726,"name": "Florida","average_private_cost":57873,"schools":54,"region":"SouthEast"},
        {"id":2, "average_public_cost":35733,"name": "Utah","average_private_cost":61283,"schools":10,"region":"Rocky Mountains"}]}

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
        {"id":0, "name": "Education","numPub":3423,"numPriv":1231,"AwardedPub":"10%","AwardedPriv":"25%" },
        {"id":1, "name": "Engineering","numPub":4213,"numPriv":2349,"AwardedPub":"17%","AwardedPriv":"12%"},
        {"id":2, "name": "Psychology","numPub":1023,"numPriv":976,"AwardedPub":"11%","AwardedPriv":"5%"}]}

  return {
    fetch: function () {
      return degrees.results;
    },
    fetchAt: function (id) {
      return degrees.results[id];
    },
  };
});

myApp.factory('GithubFetchFactory', function() { 
  return $http.get('https://api.github.com/repos/JinwookKim/cs373-idb/stats/contributors');
});

myApp.factory('IssueFetchFactory', function() { 
  return $http.get('https://api.github.com/repos/JinwookKim/cs373-idb/issues?per_page=500&state=all');
});
