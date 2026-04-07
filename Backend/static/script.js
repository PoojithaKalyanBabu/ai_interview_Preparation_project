let currentQuestion = ""

async function generateQuestion(){

let topic = document.getElementById("topic").value

const res = await fetch("/generate_question",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({topic:topic})
})

const data = await res.json()

currentQuestion = data.question

document.getElementById("question").innerText = currentQuestion
}

async function submitAnswer(){

let answer = document.getElementById("answer").value

const res = await fetch("/evaluate",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
question:currentQuestion,
answer:answer
})
})

const data = await res.json()

document.getElementById("result").innerText = data.feedback
}