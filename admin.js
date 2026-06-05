let productos = JSON.parse(localStorage.getItem("productos")) || [];

const form = document.getElementById("formProducto");
const lista = document.getElementById("listaProductos");

mostrarProductos();

form.addEventListener("submit", function(e){

    e.preventDefault();

    const nuevoProducto = {
        nombre: document.getElementById("nombre").value,
        precio: document.getElementById("precio").value,
        imagen: document.getElementById("imagen").value
    };

    productos.push(nuevoProducto);

    localStorage.setItem(
        "productos",
        JSON.stringify(productos)
    );

    form.reset();

    mostrarProductos();

});

function mostrarProductos(){

    lista.innerHTML = "";

    productos.forEach((producto, index)=>{

        lista.innerHTML += `
            <div class="producto">
                <strong>${producto.nombre}</strong><br>
                $${producto.precio}<br>
                ${producto.imagen}
                <br><br>

                <button onclick="eliminarProducto(${index})">
                    Eliminar
                </button>
            </div>
        `;
    });
}

function eliminarProducto(index){

    productos.splice(index,1);

    localStorage.setItem(
        "productos",
        JSON.stringify(productos)
    );

    mostrarProductos();
}