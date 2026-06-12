let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

const botonesAgregar = document.querySelectorAll(".producto-agregar");
const numerito = document.querySelector(".numerito");

actualizarNumerito();

botonesAgregar.forEach(boton => {

    boton.addEventListener("click", () => {

        const producto = boton.closest(".producto");

        const idProducto = boton.dataset.id;

        fetch("/agregar_carrito/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                id: idProducto
            })
        })
        .then(res => res.json())
        .then(data => {
            alert("Producto agregado");
            actualizarNumerito();
        });

    });

});

function actualizarNumerito() {
    numerito.textContent = carrito.length;
}

const btnBebidas = document.getElementById("btn-bebidas");
const btnSnacks = document.getElementById("btn-snacks");
const btnGolosinas = document.getElementById("btn-golosinas");

const bebidas = document.getElementById("bebidas");
const snacks = document.getElementById("snacks");
const golosinas = document.getElementById("golosinas");

const tituloBebidas = document.getElementById("titulo-bebidas");
const tituloSnacks = document.getElementById("titulo-snacks");
const tituloGolosinas = document.getElementById("titulo-golosinas");

function ocultarTodo() {

    bebidas.style.display = "none";
    snacks.style.display = "none";
    golosinas.style.display = "none";

    tituloBebidas.style.display = "none";
    tituloSnacks.style.display = "none";
    tituloGolosinas.style.display = "none";

}

btnBebidas.addEventListener("click", () => {

    ocultarTodo();

    bebidas.style.display = "flex";
    tituloBebidas.style.display = "block";

});

btnSnacks.addEventListener("click", () => {

    ocultarTodo();

    snacks.style.display = "flex";
    tituloSnacks.style.display = "block";

});

btnGolosinas.addEventListener("click", () => {

    ocultarTodo();

    golosinas.style.display = "flex";
    tituloGolosinas.style.display = "block";

});

ocultarTodo();

bebidas.style.display = "flex";
tituloBebidas.style.display = "block";