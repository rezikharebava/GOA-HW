function postComment(button) {
    const post = button.parentElement;
    const input = post.querySelector(".comment-input");
    const commentsSection = post.querySelector(".comments-section");
    const commentText = input.value.trim();

    if (commentText !== "") {
        const comment = document.createElement("p");
        comment.textContent = commentText;
        commentsSection.appendChild(comment);
        input.value = "";
    } else {
        alert("Write a comment before posting!");
    }
}

const body = document.querySelector("body")
const btn1 = document.getElementById("btn1")
const h1 = document.querySelector("h1")
const post = document.getElementsByClassName("post")

btn1.addEventListener("change", () => {
    body.classList.toggle("dark")
})

btn1.addEventListener("change", () => {
    h1.classList.toggle("text-white")
})

btn1.addEventListener("change", () => {
    p.classList.toggle("text-white")
})

btn1.addEventListener("change", () => {
    post[0].classList.toggle("lighter")
})

btn1.addEventListener("change", () => {
    post[1].classList.toggle("lighter")
})

btn1.addEventListener("change", () => {
    post[2].classList.toggle("lighter")
})

btn1.addEventListener("change", () => {
    post[3].classList.toggle("lighter")
})

btn1.addEventListener("change", () => {
    post[4].classList.toggle("lighter")
})