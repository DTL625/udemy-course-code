let output = document.querySelector('.output')
let dashboard = document.querySelector('.dashboard')
let btn = document.querySelector('button')

let player1 = {
    'name': 'Sean',
    'score': 0
}
let player2 = {
    'name': 'Computer',
    'score': 0
}
dashboard.innerHTML = `${player1.name}: ${player1.score} pts | ${player2.name}: ${player2.score} pts`

btn.addEventListener('click', function (item) {
    let playerRoll = 0;
    let computerRoll = 0;
    output.innerHTML = ''
    player1.score = player2.score = 0
    for (let i = 0; i < getRnd(10); i++) {
        playerRoll = getRnd(6)
        computerRoll = getRnd(6)
        output.innerHTML += `[${i + 1}] ${player1.name} get: [${playerRoll}] and ${player2.name} get [${computerRoll}] -- ${gameResult(playerRoll, computerRoll)} <br>`
    }
})

function gameResult(player1Roll, player2Roll) {
    if (player1Roll > player2Roll) {
        player1.score += 1
        res = player1.name + ' win'
    } else if (player1Roll < player2Roll) {
        player2.score += 1
        res = player2.name + ' win'
    } else {
        res = 'tie game'
    }
    dashboard.innerHTML = `${player1.name}: ${player1.score} pts | ${player2.name}: ${player2.score} pts`

    return res
}

function getRnd(max) {
    return Math.floor(Math.random() * max) + 1
}