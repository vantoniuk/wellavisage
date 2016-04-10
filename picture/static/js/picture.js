PictureApp = {
	img_sel	   : ".picture-app-picture img",
	author_sel : ".picture-app-meta-author",
	date_sel   : ".picture-app-meta-date",
	desc_sel   : ".picture-app-meta-desc",
	button_sel : ".picture-app-list",
	template   : null,

	on_click     : function(el) {
		var show_func = PictureApp.get_pitures(el.attr('href'));
     	if(PictureApp.template == null) {
     		console.log('going to retrieve template');
     		PictureApp.get_template(show_func)
     	} else {
     		console.log('using existing template')
     		show_func();	
     	}
	},
	get_template : function(withTemplate) {
		$.get('/picture/template', function(data){
			PictureApp.template = $(data);
			withTemplate();
		});
	},
	get_pitures  : function(url) { return function() {
		$.get(url, function(data){
			if(data.result) {
				console.log('got pictures');
				PictureApp.display_pictures(data.data);
			} else {
				console.log('error during retrieving pictures');
			}
		});
	}},
	render       : function(json) {
		PictureApp.template.find(PictureApp.img_sel).attr('src', json.url);
		PictureApp.template.find(PictureApp.date_sel).text(json.date);
		PictureApp.template.find(PictureApp.desc_sel).text(json.description);
		return PictureApp.template;
	},
	display_pictures: function(htmlArray) {
		$('body').append('<div id="galw" style="position: absolute; left: 100px; top: 700px; background: white; display:none;"></div>');
		htmlArray.forEach(function(el){ 
			var html = PictureApp.render(el).html();
			$('#galw').append(html)
		});
		$('#galw').append('<div style="clear:both;"></div>');
		$('#galw').fadeIn();
	}	
}

$(document).ready(function(){
	$(PictureApp.button_sel).on('click', function(e){
		e.preventDefault();
		PictureApp.on_click($(this));
	})
})