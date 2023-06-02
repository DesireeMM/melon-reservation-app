const deleteButtons = document.querySelectorAll('.delete-btn');

for (const button of deleteButtons) {
    button.addEventListener('click', () => {
        const deleteResponse = confirm("Are you sure you want to cancel this reservation?")

        if (deleteResponse == true) {

            const formInputs = {
                "res_id": button.id
            }

            fetch('/cancel-res', {
                method:'POST',
                body: JSON.stringify(formInputs),
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then((response) => response.json())
            .then((responseJson) => {
                alert(responseJson.status);
                window.location.replace(responseJson.redirect);
            })
        }
    })
}