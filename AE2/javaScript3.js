function sumar()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;
    let resultado = parseInt(n1) + parseInt(n2); 
    alert("El resultado es: " + resultado);
}
function restar()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;
    let resultado = parseInt(n1) - parseInt(n2); 
    alert("El resultado es: " + resultado);
}
function multiplicar()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;
    let resultado = parseInt(n1) * parseInt(n2); 
    alert("El resultado es: " + resultado);
}
function dividir()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;

    if(parseInt(n2) == 0)
    {
        alert("No se puede dividir por cero");
        return;
    }
    let resultado = parseInt(n1) / parseInt(n2); 
    alert("El resultado es: " + resultado);
}
function exponente()
{
    let n1 = document.getElementById("txtNumero1").value;
    let n2 = document.getElementById("txtNumero2").value;
    let resultado = parseInt(n1) ** parseInt(n2); 
    alert("El resultado es: " + resultado);
}

function factorial()
{
    let n1 = document.getElementById("txtNumero1").value;
    let resultado = 1;
    for(let i = 1; i <= parseInt(n1); i++)
    {
        resultado *= i;
    } 
    alert("El resultado es: " + resultado);
}
function sumatoria()
{
    let n1 = document.getElementById("txtNumero1").value;
    let resultado = 0;
    for(let i = 1; i <= parseInt(n1); i++)
    {
        resultado += i;
    } 
    alert("El resultado es: " + resultado);
}