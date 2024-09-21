(function($) {
	document.querySelector('#bannerClose').addEventListener('click',function() {
		document.querySelector('#proBanner').classList.add('d-none');
	});
	'use strict';
	$(function() {
		if ($(".dashboard-progress-1").length) {
			$('.dashboard-progress-1').circleProgress({
				value: 0.70,
				size: 125,
				thickness: 7,
				startAngle: 80,
				fill: {
					gradient: ["#7922e5", "#1579ff"]
				}
			});
		}
		if ($(".dashboard-progress-1-dark").length) {
			$('.dashboard-progress-1-dark').circleProgress({
				value: 0.70,
				size: 125,
				thickness: 7,
				startAngle: 10,
				emptyFill: '#eef0fa',
				fill: {
					gradient: ["#7922e5", "#1579ff"]
				}
			});
		}

		if ($(".dashboard-progress-2").length) {
			$('.dashboard-progress-2').circleProgress({
				value: 0.60,
				size: 125,
				thickness: 7,
				startAngle: 10,
				fill: {
					gradient: ["#429321", "#b4ec51"]
				}
			});
		}
		if ($(".dashboard-progress-2-dark").length) {
			$('.dashboard-progress-2-dark').circleProgress({
				value: 0.60,
				size: 125,
				thickness: 7,
				startAngle: 10,
				emptyFill: '#eef0fa',
				fill: {
					gradient: ["#429321", "#b4ec51"]
				}
			});
		}

		if ($(".dashboard-progress-3").length) {
			$('.dashboard-progress-3').circleProgress({
				value: 0.90,
				size: 125,
				thickness: 7,
				startAngle: 10,
				fill: {
					gradient: ["#f76b1c", "#fad961"]
				}
			});
		}
		if ($(".dashboard-progress-3-dark").length) {
			$('.dashboard-progress-3-dark').circleProgress({
				value: 0.90,
				size: 125,
				thickness: 7,
				startAngle: 10,
				emptyFill: '#eef0fa',
				fill: {
					gradient: ["#f76b1c", "#fad961"]
				}
			});
		}

		if ($(".dashboard-progress-4").length) {
			$('.dashboard-progress-4').circleProgress({
				value: 0.45,
				size: 125,
				thickness: 7,
				startAngle: 10,
				fill: {
					gradient: ["#9f041b", "#f5515f"]
				}
			});
		}
		if ($(".dashboard-progress-4-dark").length) {
			$('.dashboard-progress-4-dark').circleProgress({
				value: 0.45,
				size: 125,
				thickness: 7,
				startAngle: 10,
				emptyFill: '#eef0fa',
				fill: {
					gradient: ["#9f041b", "#f5515f"]
				}
			});
    }
    
		
    
	


		
    
    
		


    
    
	});
})(jQuery);