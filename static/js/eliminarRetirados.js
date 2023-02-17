function eliminarRetirados(idEntrada, modo)
{

    $("#confirm-modal").modal('show')
    let borrar = document.getElementById('modal_borrar');
    borrar.href = "/eliminar_retirado/" + modo + "/" + idEntrada

} 


