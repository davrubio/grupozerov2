
redireccionar = (id) => {
  console.log('ASDASD')
  const seccionDestino = id;
  /* seccionDestino.id.scrollIntoView({ behavior: 'smooth' }); */
  /* console.log(seccionDestino);si 
  console.log(seccionDestino.id); */
  let test = ('http://127.0.0.1:8000/tienda/galeria#'+seccionDestino);
   window.location.href = test
  console.log(test)
};