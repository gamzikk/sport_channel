let jsVariable = JSON.parse(document.getElementById('djangoData').textContent);

new Vue ({
	el: '#app',
	data: {
		title: "Hello World"
	}
})