angular.module('app.controllers')
.controller('ProfileCtrl', ['$scope', '$location', 'AccountsService', function($scope, $location, AccountsService){
    AccountsService.current().then(function(result){
        $scope.account = result.data.data;
    }, function(error){
        console.log('error');
    });
}]);
