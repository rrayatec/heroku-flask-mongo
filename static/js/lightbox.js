const imagenes = document.querySelectorAll(".img-galeria");
const imageneslight = document.querySelector(".agregar-imagen");

const contenedorlight = document.querySelector(".imagen-light");

//last
const hamburger1 = document.querySelector(".hamburger");

// console.log(imagenes);
// console.log(imageneslight);
// console.log(contenedorlight);

imagenes.forEach((imagen) => {
  imagen.addEventListener("click", () => {
    aparecerImagen(imagen.getAttribute("src"));
    //console.log(imagen.getAttribute('src'))
    //validar el compoente de imagen
  });
});

const aparecerImagen = (imagen) => {
  imageneslight.src = imagen;
  contenedorlight.classList.toggle("show");
  imageneslight.classList.toggle("showImage");
  
  //last
  hamburger1.style.opacity = "0";
};

contenedorlight.addEventListener("click", (e) => {
  //console.log(e.target)
  if (e.target != imageneslight) {
    contenedorlight.classList.toggle("show");
    imageneslight.classList.toggle("showImage");
    
    //last
    hamburger1.style.opacity = "1";
  }
});
