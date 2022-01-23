let button = document.querySelector('button')

let getbutton = document.querySelector('.getbutton')
let postbutton = document.querySelector('.postbutton')


getbutton.addEventListener('click', () => {
    let player_list = []

    let numberPlayer = prompt('Enter number of players:', '')

    for (let index = 0; index < numberPlayer; index++) {
        let namePlayer = prompt('Enter name player', "")
        player_list.push(namePlayer)

    }

    fetch("/setPlayer", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            player_list: player_list
        })
    }).then((res) => {
        return res.json();
    }).then(function(data) {
        alert('Turn #'+ data.turn +' '+ 'Player :' + data.name );

    //     fetch("/playerPlay", {
    //     method: "POST",
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //         player: data
    //     })
    // })
    });

});