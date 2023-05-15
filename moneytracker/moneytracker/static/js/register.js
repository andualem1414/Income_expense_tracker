const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".invalid-feedback");
const usernameSuccess = document.querySelector(".usernameSuccess");

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameSuccess.style.display = "block";
    usernameSuccess.textContent = `Checking ${usernameVal} ...`;

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch("/authentication/validate-username", {
            body: JSON.stringify({
                username: usernameVal,
            }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                usernameSuccess.style.display = "none";
                if (data.username_error) {
                    usernameField.classList.add("is-invalid");
                    feedbackArea.style.display = "block";
                    feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
                }
            });
    } else {
        usernameSuccess.style.display = "none";
    }
});

const emailField = document.querySelector("#emailField");
const emailFeedbackArea = document.querySelector(".emailFeedbackArea");
const emailSuccess = document.querySelector(".emailSuccess");

emailField.addEventListener("keyup", (e) => {
    emailVal = e.target.value;

    emailSuccess.style.display = "block";
    emailSuccess.textContent = `Checking ${emailVal} ...`;

    emailField.classList.remove("is-invalid");
    emailFeedbackArea.style.display = "none";

    if (emailVal.length > 0) {
        fetch("/authentication/validate-email", {
            body: JSON.stringify({
                email: emailVal,
            }),

            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                emailSuccess.style.display = "none";
                if (data.email_error) {
                    emailField.classList.add("is-invalid");
                    emailFeedbackArea.innerHTML = "<p>Email not correct </p>";
                    emailFeedbackArea.style.display = "block";
                }
            });
    } else {
        emailSuccess.style.display = "none";
    }
});

showPasswordToggle = document.querySelector(".showPasswordToggle");
passwordField = document.querySelector("#passwordField");

const handelToggleInput = (e) => {
    if (showPasswordToggle.textContent == "SHOW") {
        showPasswordToggle.textContent = "HIDE";
        passwordField.setAttribute("type", "text");
    } else {
        showPasswordToggle.textContent = "SHOW";
        passwordField.setAttribute("type", "password");
    }
};
showPasswordToggle.addEventListener("click", handelToggleInput);
