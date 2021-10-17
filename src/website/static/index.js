
textAreaBtn = document.getElementById('textarea_btn')
uploadInputBtn = document.getElementById('upload_btn')

textAreaBtn.addEventListener('click', function (){
    document.getElementsByClassName('file_input')[0].style.display = 'none';
    document.getElementsByClassName('textarea')[0].style.display = 'block';
    document.getElementsByClassName('input_zone')[0].value = ''
})

uploadInputBtn.addEventListener('click', function (){
    document.getElementsByClassName('file_input')[0].style.display = 'block';
    document.getElementsByClassName('textarea')[0].style.display = 'none';
    document.getElementsByClassName('text_zone')[0].value = ''
})