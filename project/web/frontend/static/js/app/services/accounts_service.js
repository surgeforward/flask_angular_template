angular.module('app.services')
    .service('AccountsService', ['$http', function AccountsService($http){
        this.current = function(){
            return $http.get('/api/accounts/current');
        };
    }]);
