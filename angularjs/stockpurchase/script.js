function OrderFormController($scope){

	$scope.services = [
		{
			name: 'Reliance',
			price: 500.36,
			active:true
		},{
			name: 'TCS',
			price: 15.36,
			active:false
		},{
			name: 'NEROLAC',
			price: 250.96,
			active:false
		},{
			name: 'ITC',
			price: 45.6,
			active:false
		},{
			name: 'Axis Bank',
			price: 540.10,
			active:false
		},{
			name: 'Bajaj Auto',
			price: 3217.45,
			active:false
		},{
			name: 'Bharti Airtel',
			price: 541.25,
			active:false
		},{
			name: 'Cipla',
			price: 640.10,
			active:false
		}
	];

	$scope.toggleActive = function(s){
		s.active = !s.active;
	};

	$scope.total = function(){

		var total = 0;


		angular.forEach($scope.services, function(s){
			if (s.active){
				total+= s.price;
			}
		});

		return total;
	};
}
