let carrito = JSON.parse(localStorage.getItem("carrito")) || [];

const botonesAgregar = document.querySelectorAll(".producto-agregar");
const numerito = document.querySelector(".numerito");

// Mostrar cantidad al cargar la página
actualizarNumerito();

botonesAgregar.forEach(boton => {

    boton.addEventListener("click", () => {

        const producto = boton.closest(".producto");

        const nombre = producto.querySelector(".producto-bebida").textContent;

        carrito.push(nombre);

        localStorage.setItem(
            "carrito",
            JSON.stringify(carrito)
        );

        actualizarNumerito();

    });

});

function actualizarNumerito() {
    numerito.textContent = carrito.length;
}