const start = document.getElementById("start");
const quiz = document.getElementById("quiz");
const question = document.getElementById("question");
const choiceY = document.getElementById("Y");
const choiceN = document.getElementById("N");
const counter = document.getElementById("counter");
const timeGauge = document.getElementById("timeGauge");
const progress = document.getElementById("progress");
const scoreDiv = document.getElementById("scoreContainer")

let runningQuestion = 0;
let count = 0;
const questionTime = 10;
const gaugeWidth = 150;
const gaugeUnit = gaugeWidth / questionTime;
let TIMER;
let score = 0;

function renderQuestion() {
    fetch('quiz/')
    .then(res => res.json())
    .then(data => {
        const questions = JSON.parse(data);
        let q = questions[runningQuestion];
        question.innerHTML = "<p>" + q.fields.question_content + "</p>";
        choiceY.innerHTML = 'Yes';
        choiceN.innerHTML = 'No';
    })
}

start.addEventListener("click", startQuiz)

function startQuiz() {
    start.style.display = "none";
    renderQuestion();
    quiz.style.display = "block";
    renderProgress();
    renderCounter();
    TIMER = setInterval(renderCounter, 1000);
}

function renderProgress() {
    fetch('quiz/')
    .then(res => res.json())
    .then(data => {
        const questions = JSON.parse(data);
        const lastQuestion = questions.length - 1;
        for (let qIndex = 0; qIndex <= lastQuestion; qIndex++) {
            progress.innerHTML += "<div class='prog' id=" + qIndex + "></div>";
        }
    })
}

function renderCounter() {
    if (count <= questionTime) {
        counter.innerHTML = count;
        timeGauge.style.width = count * gaugeUnit + "px";
        count++
    } else {
        count = 0;
        answerIsWrong();
        if (runningQuestion < lastQuestion) {
            runningQuestion++;
            renderQuestion();
        } else {
            clearInterval(TIMER);
            scoreRender();
        }
    }
}

function checkAnswer(answer) {
    fetch('quiz/')
    .then(res => res.json())
    .then(data => {
        const questions = JSON.parse(data);
        const lastQuestion = questions.length - 1;
        if (answer == questions[runningQuestion].fields.quiz_correct_answer) {
            score++
            answerIsCorrect();
        } else {
            answerIsWrong();
        }
        count = 0;
        if (runningQuestion < lastQuestion) {
            runningQuestion++;
            renderQuestion();
        } else {
            clearInterval(TIMER);
            scoreRender();
        }
    })
}

function answerIsCorrect() {
    document.getElementById(runningQuestion).style.backgroundColor = "green";
}

function answerIsWrong() {
    document.getElementById(runningQuestion).style.backgroundColor = "red";
}

function scoreRender() {
    fetch('quiz/')
    .then(res => res.json())
    .then(data => {
        const questions = JSON.parse(data);
        scoreDiv.style.display = "block";
        const scorePerCent = Math.round(100 * score / questions.length);

        let img = (scorePerCent >= 80) ? imgVeryGood :
            (scorePerCent >= 60) ? imgGood :
            (scorePerCent >= 40) ? imgNormal :
            (scorePerCent >= 20) ? imgBad :
            imgVeryBad

        scoreDiv.innerHTML = "<img src=" + img + ">";
        scoreDiv.innerHTML += "<p>" + scorePerCent + "%</p>";
    })
}