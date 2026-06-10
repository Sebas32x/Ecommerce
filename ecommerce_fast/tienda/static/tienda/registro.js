document.getElementById("formRegistro").addEventListener("submit", function(e){

    e.preventDefault();

    const usuario = {
        nombre: document.getElementById("nombre").value,
        apellido: document.getElementById("apellido").value,
        curso: document.getElementById("curso").value,
        usuario: document.getElementById("usuario").value,
        password: document.getElementById("password").value
    };

    localStorage.setItem("usuarioRegistrado", JSON.stringify(usuario));

    alert("Usuario registrado correctamente");

    window.location.href = "index.html";

});