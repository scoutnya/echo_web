let firstTime = true;
function getRandomPost() {

    const box = document.getElementById("randomPost");

    fetch("/random")
        .then(response => response.json())
        .then(data => {

            if (firstTime) {

                box.classList.remove("hidden"); 

                void box.offsetWidth;

                box.innerHTML = data.content;

                box.classList.add("show");

                firstTime = false;

            } else {

                box.classList.remove("show");

                void box.offsetWidth;

                box.innerHTML = data.content;

                box.classList.add("show");
            }

        })

}
function checkPost() {

    let text = document.getElementById("content").value

    if (text.trim() === "") {
        alert("Please enter something")
        return false
    }

    return true
}
