const password = document.querySelector("#password")
const password_confirmation = document.querySelector("#password_confirmation")
const buttonClick = document.querySelector("#buttonClick")
buttonClick.addEventListener("click" , function(){
    let password = document.getElementById('password').value;
    let password_confirmation = document.getElementById('password_confirmation').value;
    if(password.length < 8) {
        alert("8글자 이상이여야 합니다!")
    }
    if( password !== password_confirmation){
        alert("비밀번호를 확인해주세요!");
    }else{
        alert("비밀번호가 일치합니다");
    }
}
)