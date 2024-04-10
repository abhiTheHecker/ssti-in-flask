const click_handler = () => {
    const base64_string = document.querySelector("#base64_string").value;
    const h2 = document.querySelector(".plaintext");
    const plaintext_string = atob(base64_string);
    h2.innerHTML = plaintext_string;
    console.log("Completed")
}
