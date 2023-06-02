const resButtons = document.querySelectorAll('.book-btn');

for (const button of resButtons) {
    button.addEventListener('click', () => {

        const resTime = button.id;
        const resDate = document.querySelector('#res-date').value;

        const formInputs = {
            "res_date": resDate,
            "res_time": resTime
        }

        fetch('/make-reservation', {
            method: 'POST',
            body: JSON.stringify(formInputs),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(responseJson => {
            alert(responseJson.status);
            window.location.replace(responseJson.redirect)
        })

    })
}