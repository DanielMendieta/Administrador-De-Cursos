const $formularioCurso = document.getElementById ('formularioCurso');
const $txtNombre= document.getElementById('txtNombre');
const btnsEliminacion=document.querySelectorAll('.btnEliminacion');

(function (){
    $formularioCurso.addEventListener('submit', function(e){
        let nombre = String ($txtNombre.value).trim()
        if (nombre.length ==0){
            alert ("El nombre del curso no puede ir vacio");
            e.preventDefault();
        }
    });

    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function (e){
            let confirmacion = confirm("¿Esta seguro que desea eliminar este curso?");
            if (!confirmacion){
                e.preventDefault();

            }
        });
    });
})();







