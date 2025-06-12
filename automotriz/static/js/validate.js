$("#formulario-repuesto").validate({
    rules: {
        nombre_repuesto: {
            required: true,
            minlength: 3,
            maxlength: 100
        },
        descripcion: {
            required: true,
            minlength: 5
        },
        precio: {
            required: true,
            number: true,
            min: 0.01
        },
        cantidad_disponible: {
            required: true,
            digits: true, //* ← esto valida enteros
            min: 1
        }
    },
    messages: {
        nombre_repuesto: {
            required: "Por favor, ingrese el nombre del repuesto.",
            minlength: "Debe tener al menos 3 caracteres.",
            maxlength: "No debe exceder 100 caracteres."
        },
        descripcion: {
            required: "Por favor, ingrese una descripción.",
            minlength: "La descripción debe tener al menos 5 caracteres."
        },
        precio: {
            required: "Por favor, ingrese el precio.",
            number: "Debe ser un número válido.",
            min: "El precio debe ser mayor que 0."
        },
        cantidad_disponible: {
            required: "Por favor, ingrese la cantidad disponible.",
            digits: "Debe ser un número entero.",
            min: "Debe ser al menos 1."
        }
    },
    errorClass: 'invalid-feedback',
    errorElement: 'div',
    highlight: function(element) {
        $(element).addClass('is-invalid');
    },
    unhighlight: function(element) {
        $(element).removeClass('is-invalid');
    },
    submitHandler: function(form) {
        form.submit(); // * Si todo está validado correctamente
    }
});

$("#formulario-vehiculo").validate({
    rules: {
        marca: {
            required: true,
            minlength: 2,
            maxlength: 50
        },
        modelo: {
            required: true,
            minlength: 2,
            maxlength: 50
        },
        anio: {
            required: true,
            digits: true,
            min: 1886, // Año del primer automóvil
            max: new Date().getFullYear() // Año actual
        },
        color: {
            required: true,
            minlength: 3,
            maxlength: 30
        }
    },
    messages: {
        marca: {
            required: "Por favor, ingrese la marca del vehículo.",
            minlength: "Debe tener al menos 2 caracteres.",
            maxlength: "No debe exceder 50 caracteres."
        },
        modelo: {
            required: "Por favor, ingrese el modelo del vehículo.",
            minlength: "Debe tener al menos 2 caracteres.",
            maxlength: "No debe exceder 50 caracteres."
        },
        anio: {
            required: "Por favor, ingrese el año del vehículo.",
            digits: "Debe ser un número entero.",
            min: "El año no puede ser anterior a 1886.",
            max: "El año no puede ser mayor que el año actual."
        },
        color: {
            required: "Por favor, ingrese el color del vehículo.",
            minlength: "Debe tener al menos 3 caracteres.",
            maxlength: "No debe exceder 30 caracteres."
        }
    },
    errorClass: 'invalid-feedback',
    errorElement: 'div',
    highlight: function(element) {
        $(element).addClass('is-invalid');
    },
    unhighlight: function(element) {
        $(element).removeClass('is-invalid');
    },
    submitHandler: function(form) {
        form.submit(); // * Si todo está validado correctamente
    }
}); 

