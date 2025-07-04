const eliminarFila = (url, nombreTabla) => {
    iziToast.question({
    timeout: 20000,
    close: false,
    overlay: true,
    displayMode: 'once',
    id: 'question',
    zindex: 999,
    title: 'CONFIRMACIÓN!',
    message: 'Estas seguro de eliminar el registro de la tabla ' + nombreTabla + '?',
    position: 'center',
    buttons: [
        ['<button><b>SI</b></button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
            window.location.href = url;
 
        }, true],
        ['<button>NO</button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
 
        }],
    ],
    onClosing: function(instance, toast, closedBy){
        console.info('Closing | closedBy: ' + closedBy);
    },
    onClosed: function(instance, toast, closedBy){
        console.info('Closed | closedBy: ' + closedBy);
    }
});
}

const eliminarFilaVehiculo = (url, nombreTabla) => {
    iziToast.question({
    timeout: 20000,
    close: false,
    overlay: true,
    displayMode: 'once',
    id: 'question',
    zindex: 999,
    title: 'CONFIRMACIÓN!',
    message: 'Estas seguro de eliminar el registro de la tabla ' + nombreTabla + '?',
    position: 'center',
    buttons: [
        ['<button><b>SI</b></button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
            window.location.href = url;
 
        }, true],
        ['<button>NO</button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
 
        }],
    ],
    onClosing: function(instance, toast, closedBy){
        console.info('Closing | closedBy: ' + closedBy);
    },
    onClosed: function(instance, toast, closedBy){
        console.info('Closed | closedBy: ' + closedBy);
    }
});
}

const eliminarTipoMantenimiento = (url, nombreTabla) => {
    iziToast.question({
    timeout: 20000,
    close: false,
    overlay: true,
    displayMode: 'once',
    id: 'question',
    zindex: 999,
    title: 'CONFIRMACIÓN!',
    message: 'Estas seguro de eliminar el registro de la tabla ' + nombreTabla + '?',
    position: 'center',
    buttons: [
        ['<button><b>SI</b></button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
            window.location.href = url;
 
        }, true],
        ['<button>NO</button>', function (instance, toast) {
 
            instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
 
        }],
    ],
    onClosing: function(instance, toast, closedBy){
        console.info('Closing | closedBy: ' + closedBy);
    },
    onClosed: function(instance, toast, closedBy){
        console.info('Closed | closedBy: ' + closedBy);
    }
});
}