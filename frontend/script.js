document.getElementById("generateBtn").addEventListener("click", generatePassword);
document.getElementById("saveBtn").addEventListener("click", savePassword);
window.onload = displaySavedPasswords;

async function generatePassword() {
    const length = document.getElementById("length").value;
    const uppercase = document.getElementById("uppercase").checked;
    const lowercase = document.getElementById("lowercase").checked;
    const digits = document.getElementById("digits").checked;
    const special_chars = document.getElementById("special_chars").checked;

    const response = await fetch(`http://localhost:8000/generate-password?length=${length}&uppercase=${uppercase}&lowercase=${lowercase}&digits=${digits}&special_chars=${special_chars}`);
    const data = await response.json();

    if(data.password){
        document.getElementById("password").value = data.password;
    }else{
        alert(data.error);
    }
}

// Salvar senha no Local Storage
function savePassword() {
    const password = document.getElementById("password").value;
    if(!password){
        alert("Gere uma senha antes de salvar!");
        return;
    }
    const saved = JSON.parse(localStorage.getItem("passwords")) || [];
    saved.push(password);
    localStorage.setItem("passwords", JSON.stringify(saved));
    displaySavedPasswords();
}

// Exibir senhas salvas
function displaySavedPasswords() {
    const saved = JSON.parse(localStorage.getItem("passwords")) || [];
    const passwordList = document.getElementById("passwordList");
    passwordList.innerHTML = saved.map(p => `<li>${p}</li>`).join("");
}
document.getElementById("generateBtn").addEventListener("click", generatePassword);
document.getElementById("saveBtn").addEventListener("click", savePassword);
window.onload = displaySavedPasswords;

async function generatePassword() {
    const length = document.getElementById("length").value;
    const uppercase = document.getElementById("uppercase").checked;
    const lowercase = document.getElementById("lowercase").checked;
    const digits = document.getElementById("digits").checked;
    const special_chars = document.getElementById("special_chars").checked;

    const response = await fetch(`http://localhost:8000/generate-password?length=${length}&uppercase=${uppercase}&lowercase=${lowercase}&digits=${digits}&special_chars=${special_chars}`);
    const data = await response.json();

    if(data.password){
        document.getElementById("password").value = data.password;
    }else{
        alert(data.error);
    }
}

// Salvar senha no Local Storage
function savePassword() {
    const password = document.getElementById("password").value;
    if(!password){
        alert("Gere uma senha antes de salvar!");
        return;
    }
    const saved = JSON.parse(localStorage.getItem("passwords")) || [];
    saved.push(password);
    localStorage.setItem("passwords", JSON.stringify(saved));
    displaySavedPasswords();
}

// Exibir senhas salvas
function displaySavedPasswords() {
    const saved = JSON.parse(localStorage.getItem("passwords")) || [];
    const passwordList = document.getElementById("passwordList");
    passwordList.innerHTML = saved.map(p => `<li>${p}</li>`).join("");
}
