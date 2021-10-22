document.getElementById('return').addEventListener('click', function () {
	document.location.href = '/home';
});

document.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("return").click();
  }
});