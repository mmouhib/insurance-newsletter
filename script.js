document.querySelector('clear').addEventListener('click', function () {
	inputs = document.getElementsByTagName('input');
	for (let index = 0; index < inputs.length; index++) {
		inputs[index].value = '';
	}
	document.getElementsByTagName('textarea')[0].value = '';
});
