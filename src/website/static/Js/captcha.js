operators = [' + ', ' - ', ' * '];

operator = secondNumber = Math.floor(Math.random() * 3);

firstNumber = Math.floor(Math.random() * 10) + 1;

secondNumber = Math.floor(Math.random() * 10) + 1;

do {
	secondNumber = Math.floor(Math.random() * 10) + 1;
} while (secondNumber > firstNumber);

switch (operator) {
	case 0:
		result = firstNumber + secondNumber;
		break;
	case 1:
		result = firstNumber - secondNumber;
		break;
	default:
		result = firstNumber * secondNumber;
		break;
}

captcha = firstNumber.toString() + operators[operator] + secondNumber.toString();

window.onload = (event) => {
	document.getElementById("submit_btn").disabled = true;
	document.getElementById('formule_captcha').innerHTML = captcha;
};

document.getElementById('Resultat_captcha').addEventListener('change', function () {
    if (document.getElementById('Resultat_captcha').value === result.toString()){
        document.getElementById("submit_btn").disabled = false;
    }
});
