//view change
textAreaBtn = document.getElementById('textarea_btn');
uploadInputBtn = document.getElementById('upload_btn');

textAreaBtn.addEventListener('click', function () {
    document.getElementsByClassName('file_input')[0].style.display = 'none';
    document.getElementsByClassName('textarea_div')[0].style.display = 'block';
    document.getElementsByClassName('input_zone')[0].value = '';
});

uploadInputBtn.addEventListener('click', function () {
    document.getElementsByClassName('file_input')[0].style.display = 'block';
    document.getElementsByClassName('textarea_div')[0].style.display = 'none';
    document.getElementById('emails').value = '';
});

//loading animation
document.getElementById('submit_btn').addEventListener('click', function (){
    form = document.getElementById('form').style.display = 'none'
    animation = document.getElementById('animation').style.display = 'block'
})

document.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("submit_btn").click();
  }
});
