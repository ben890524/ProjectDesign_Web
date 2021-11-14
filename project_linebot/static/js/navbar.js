let burger = document.getElementById('burger'),
	nav    = document.getElementById('main-nav'),
	container = document.getElementById('mobile_container');
	nav_li = document.querySelectorAll('#navbar #mobile_container li');

burger.addEventListener('click', function(e){
	this.classList.toggle('is-open');
	nav.classList.toggle('is-open');
	container.classList.toggle('is-open');
});
nav_li.forEach(element => {
	element.addEventListener('click', function(e){
		burger.classList.toggle('is-open');
		nav.classList.toggle('is-open');
		container.classList.toggle('is-open');
	});
});