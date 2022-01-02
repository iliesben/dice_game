let button = document.querySelector('button')


button.addEventListener('click', () => {
    fetch('/my-link/').then(function (response) {
        response.text().then(function (text) {
            alert(text)
        });
    });
});