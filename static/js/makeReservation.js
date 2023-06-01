const resButtons = document.querySelectorAll('.book-btn');

for (const button of resButtons) {
    button.addEventListener('click', () => {

        const resDateTime = button.id;
        console.log(button.id);

        const formInputs = {
            "res_datetime": resDateTime
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