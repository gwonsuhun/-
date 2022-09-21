const button = document.querySelector("#lotto-choice")
button.addEventListener("click",function(){
    const ballContainer = document.createElement("div")
    ballContainer.classList.add("ball-container")
    const ball = document.createElement("div")
    ball.classList.add("ball")
    ball.innerText = 5
    ballContainer.appendChild(ball)
    const result = document.querySelector("#result")
    result.appendChild(ballContainer)
})

