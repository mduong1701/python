const food_result = document.getElementById('food_result');
const food_btn = document.getElementById('food_btn');

food_btn.addEventListener('click', getRandomFood);

function getRandomFood() {
    fetch('https://foodish-api.herokuapp.com/api/')
        .then(res => res.json())
        .then(data => {
            food_result.innerHTML = `<img src="${data.image}"/>`
        })
}