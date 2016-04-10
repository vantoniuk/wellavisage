var CarouselPlugin = {
	wrapper_selector: ".carousel-picture-wrapper",
	inner_selector: ".picture-app-carousel-inner",
	register : function(config) {
		var $carousel = $(config.sel);
		var $currentEl = $carousel.find(".carousel-show");
		var $inner = $carousel.find(CarouselPlugin.inner_selector);
		var $wrapper = $carousel.find(CarouselPlugin.wrapper_selector);
		var $images = $carousel.find('img');

		$images.each(function(a, el){
			$(el).css({
				width: config.width + "px"
				// maxHeight: config.height + "px",
			});
		});	

		CarouselPlugin.get_init_func(config.change_effect)($carousel, $wrapper);

		if($images.length > 1) {	
			// setInterval(function(){
			// 	$currentEl.hide();
			// 	$currentEl = CarouselPlugin.get_next($currentEl, CarouselPlugin.wrapper_selector);
			// 	$currentEl.fadeIn();	
			// }, config.interval * 1000);
			setInterval(function(){

				CarouselPlugin.adjust_images(config, $carousel, $images);	
				var $nextEl = CarouselPlugin.get_next($currentEl, CarouselPlugin.wrapper_selector);
				CarouselPlugin.change_picture(config.change_effect, $inner, $currentEl, $nextEl);	
				$currentEl = $nextEl
			}, config.interval * 1000);
		}
	},

	adjust_images: function(config, $carousel, $images) {
		$images.each(function(a, el){
			$(el).css({
				width: (config.width > $carousel.width() ? $carousel.width() : config.width) + "px"
				// maxHeight: config.height + "px",
			});
		});
	},

	get_next: function(el, selector) {
		var next = el.next();
		return next.length > 0 ? next : $(selector).first();
	},

	change_picture: function(effect, $wrapper, $current, $next) {
		CarouselPlugin.get_effect_func(effect)($wrapper, $current, $next);	
	},

	get_effect_func: function(effect){
		var change_func = function(){};
		switch(effect) {
			case 'S':
				change_func = CarouselPlugin.__slide;
				break;
			case 'SE':
				change_func = CarouselPlugin.__slideExclusive;
				break;
			case 'FI':
				change_func = CarouselPlugin.__fadeIn;
				break;
			case 'FO':
				change_func = CarouselPlugin.__fadeOut;
				break;		
		};
		return change_func;
	},

	get_init_func: function(effect){
		var change_func = function(){};
		switch(effect) {
			case 'S':
				change_func = function($carousel, $pictureWrapper){
					$pictureWrapper.css("width", $carousel.width());
					$pictureWrapper.css("margin-right", parseInt($carousel.css("padding-right")));
				};
				break;
			case 'SE':
				break;
			case 'FI':
				break;
			case 'FO':
				break;		
		};
		return change_func;
	},
	__slide: function($wrapper, $current, $next) {
		var currentMargin = parseInt($current.css("margin-left"));
		var currentMarginRight = parseInt($current.css("margin-right"));
		var currentWidth = $current.innerWidth();
		$current.animate({
			marginLeft: -currentMargin - currentWidth - currentMarginRight
		}, 1000, function(){	
			$current.css("margin-left", currentMargin);		
			CarouselPlugin.__append($wrapper, $current);
			// $current.remove();
		});
	},
	__slideExclusive: function($wrapper, $current, $next) {
		var currentMargin = parseInt($current.css("margin-left"));
		var currentWidth = $current.innerWidth();

		CarouselPlugin.__append($wrapper, $current);
		$current.animate({
			marginLeft: -currentMargin - currentWidth
		}, 1000, function(){
			$current.remove();
		});
	},
	__fadeOut: function($wrapper, $current, $next) {
		$current.fadeOut(function(){
			$next.show();
		});
	},
	__fadeIn: function($wrapper, $current, $next) {
		$current.hide();
		$next.fadeIn();
	},
	__append: function($wrapper, $element) {
		var $div = $("<div>");
		$div.html($element);
		$wrapper.append($div.html());
	}
	/*
	('S', 'Slide'), 
	('SE', 'Slide Exclusive (show only one picture at a time)'), 
	('FI', 'Fade In'), 
	('FO', 'Fade Out')
	*/
}