const main = document.querySelector('#main');
const warning = document.querySelector('#warning');
const img = document.getElementById('img');
const text = document.querySelector('#warning p');

function start() {
  main.style.WebkitAnimation = 'fadeOut 1s';
  main.style.animation = 'fadeOut 1s';
  setTimeout(() => {
    warning.style.WebkitAnimation = 'fadeIn 1s';
    warning.style.animation = 'fadeIn 1s';
    setTimeout(() => {
      main.style.display = 'none';
      warning.style.display = 'block';
    }, 450);
    let qIdx = 0;
    goNext(qIdx);
  }, 450);
}

function hoverImg() {
  img.src = './images/startBtn2.png';
}

function unhoverImg() {
  img.src = './images/startBtn.png';
}

function changeText() {
  text.innerHTML =
    '당신은 입장하실 수 없습니다! <br> 오직 여성만이 입장할 수 있습니다.';
}
