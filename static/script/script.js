document.addEventListener("DOMContentLoaded", function () {
    var modal = document.getElementById('myModal');
    var closeModalBtn = document.querySelector('.close');

    function openModal() {
        modal.style.display = 'block';
        closeModalBtn.addEventListener('click', closeModal);
    }
    function closeModal() {
        modal.style.display = 'none';
        closeModalBtn.removeEventListener('click', closeModal);
    }
    window.openModal = openModal;
});

let button = document.querySelector("#check")

async function checkContent() {
    console.log("Hello")
    var userInput = document.getElementById('userInput').value;
    try {
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: userInput }),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        document.getElementById('modalResult').innerText = data.result;
        openModal();
    } catch (error) {
        console.error('Error:', error);
    }
}

button.addEventListener("click", checkContent())