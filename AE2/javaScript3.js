function sumar()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;
    let resultado = parseInt(n1) + parseInt(n2); 
    alert("El resultado es: " + resultado);
}