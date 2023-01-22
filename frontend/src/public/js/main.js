// Reference: https://github.com/bradtraversy/nodejs-openai-image/blob/main/public/js/main.js

function onSubmit(e) {
    e.preventDefault();

    document.querySelector(".msg").textContent = "";

    const source = document.querySelector("#source").value;

    if (source === "") {
        alert("Please add some text");
        return;
    }

    translateRequest(source);
}

async function translateRequest(source) {
    try {
        showSpinner();

        const response = await fetch("/translate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                source,
            }),
        });

        if (!response.ok) {
            removeSpinner();
            throw new Error("Something went wrong");
        }

        const data = await response.json();
        // console.log(data);

        const translation = data.translation;

        document.querySelector("#translation").value = await translation;

        removeSpinner();
    } catch (error) {
        document.querySelector(".msg").textContent = error;
    }
}

function showSpinner() {
    document.querySelector(".spinner").classList.add("show");
}

function removeSpinner() {
    document.querySelector(".spinner").classList.remove("show");
}

document.querySelector("#source-form").addEventListener("submit", onSubmit);
