angular.module('app.controllers')
.controller('LoginCtrl', ['$scope', '$location', 'AuthService', function($scope, $location, AuthService){
    $scope.login = {
        email: '',
        password: ''
    };

    $scope.submitted = false;

    $scope.submitForm = function(){
        $scope.submitted = true;

        AuthService.login({ username: $scope.login.email, password: $scope.login.password}).then(function(result){
            $location.path('/profile');
        }, function(error){
            console.log('error');
        });
    };
}]);
