let nombre = document.getElementById('nombre');
    email = document.getElementById('email');
    direccion = document.getElementById('direccion');
    error = document.getElementById('error');
error.style.color = 'red';

function enviarFormulario(){
    var mensajeErr = [];
    if(nombre.value !== null && nombre.value !== '' && email.value !== null && email.value !== ''){
      alert('formulario enviado')
    }
    if(nombre.value === null || nombre.value === ''){
      mensajeErr.push('Debes ingresar tu nombre')
    }
    if(email.value === null || email.value === ''){
      mensajeErr.push('Debes ingresar tu correo')
    }
    error.innerHTML = mensajeErr.join(', ')
    return false;
};