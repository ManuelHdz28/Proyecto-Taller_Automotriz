$("#formulario-repuesto").validate({
  rules: {
    nombre_repuesto: {
      required: true,
      minlength: 3,
      maxlength: 100,
    },
    descripcion: {
      required: true,
      minlength: 5,
    },
    precio: {
      required: true,
      number: true,
      min: 0.01,
    },
    cantidad_disponible: {
      required: true,
      digits: true, //* ← esto valida enteros
      min: 1,
    },
    nombre_mantenimiento: {
      required: true,
      minlength: 3,
      maxlength: 100,
    },

    precio_mantenimiento: {
      required: true,
      number: true,
      min: 0.01,
    },
  },
  messages: {
    nombre_repuesto: {
      required: "Por favor, ingrese el nombre del repuesto.",
      minlength: "Debe tener al menos 3 caracteres.",
      maxlength: "No debe exceder 100 caracteres.",
    },
    descripcion: {
      required: "Por favor, ingrese una descripción.",
      minlength: "La descripción debe tener al menos 5 caracteres.",
    },
    precio: {
      required: "Por favor, ingrese el precio.",
      number: "Debe ser un número válido.",
      min: "El precio debe ser mayor que 0.",
    },
    cantidad_disponible: {
      required: "Por favor, ingrese la cantidad disponible.",
      digits: "Debe ser un número entero.",
      min: "Debe ser al menos 1.",
    },
    nombre_mantenimiento: {
      required: "Por favor, ingrese el nombre del tipo de mantenimiento.",
      minlength: "Debe tener al menos 3 caracteres.",
      maxlength: "No debe exceder 100 caracteres.",
    },
    precio_mantenimiento: {
      required: "Por favor, ingrese un precio.",
      number: "El precio debe ser un número.",
      min: "El precio debe ser al menos 0.01.",
    },
  },
  errorClass: "invalid-feedback",
  errorElement: "div",
  highlight: function (element) {
    $(element).addClass("is-invalid");
  },
  unhighlight: function (element) {
    $(element).removeClass("is-invalid");
  },
  submitHandler: function (form) {
    form.submit(); // * Si todo está validado correctamente
  },
});

$("#formulario-tipos").validate({
  rules: {
    nombre_mantenimiento: {
      required: true,
      maxlength: 100,
      minlength: 3,
      uniqueTipoMantenimiento: true, // * Validación personalizada para nombres únicos
    },
    precio_mantenimiento: {
      required: true,
      number: true,
      min: 0.01,
    },
    
  },
  messages: {
    nombre_mantenimiento: {
      required: "Por favor, ingrese el nombre del tipo de mantenimiento.",
      minlength: "Debe tener al menos 3 caracteres.",
      maxlength: "No debe exceder 100 caracteres.",
    },
    precio_mantenimiento: {
      required: "Por favor, ingrese un precio.",
      number: "El precio debe ser un número.",
      min: "El precio debe ser al menos 0.01.",
    }
    
  },
  errorClass: "invalid-feedback",
  errorElement: "div",
  highlight: function (element) {
    $(element).addClass("is-invalid");
  },
  unhighlight: function (element) {
    $(element).removeClass("is-invalid");
  },
  submitHandler: function (form) {
    form.submit(); // * Si todo está validado correctamente
  },
});

$("#formulario-vehiculo").validate({
  rules: {
    placa_vehiculo: {
      required: true,
      minlength: 9,
      maxlength: 9,
    },
    nombre_propietario: {
      required: true,
      minlength: 3,
      maxlength: 100,
    },
    marca: {
      required: true,
      minlength: 2,
      maxlength: 90,
    },
    modelo: {
      required: true,
      minlength: 2,
      maxlength: 50,
    },
    anio: {
      required: true,
      digits: true,
      min: 1886, // Año del primer automóvil
      max: new Date().getFullYear(), // Año actual
    },
    fotos: {
      required: true,
      extension: "jpg|jpeg|png|gif",
      exactlyFourFiles: true,
    },
  },
  messages: {
    placa_vehiculo: {
      required: "Por favor, ingrese la placa del vehículo.",
      minlength: "La placa debe tener exactamente 9 caracteres.",
      maxlength: "La placa no debe exceder 9 caracteres.",
    },
    nombre_propietario: {
      required: "Por favor, ingrese el nombre del propietario.",
      minlength: "El nombre del propietario debe tener al menos 3 caracteres.",
      maxlength: "El nombre del propietario no debe exceder 100 caracteres.",
    },
    marca: {
      required: "Por favor, ingrese la marca del vehículo.",
      minlength: "Debe tener al menos 2 caracteres.",
      maxlength: "No debe exceder 50 caracteres.",
    },
    modelo: {
      required: "Por favor, ingrese el modelo del vehículo.",
      minlength: "Debe tener al menos 2 caracteres.",
      maxlength: "No debe exceder 50 caracteres.",
    },
    anio: {
      required: "Por favor, ingrese el año del vehículo.",
      digits: "Debe ser un número entero.",
      min: "El año no puede ser anterior a 1886.",
      max: "El año no puede ser mayor que el año actual.",
    },
    fotos: {
      required: "Por favor, suba al menos una foto del vehículo.",
      extension: "Solo se permiten archivos de imagen (jpg, jpeg, png, gif).",
    },
  },
  errorClass: "invalid-feedback",
  errorElement: "div",
  highlight: function (element) {
    $(element).addClass("is-invalid");
  },
  unhighlight: function (element) {
    $(element).removeClass("is-invalid");
  },
  submitHandler: function (form) {
    form.submit(); // * Si todo está validado correctamente
  },
});

$.validator.addMethod(
  "exactlyFourFiles",
  function (value, element) {
    return element.files.length === 4;
  },
  "Debes subir exactamente 4 imágenes."
);

$("#formulario-mantenimiento").validate({
  rules: {
    fecha_mantenimiento: {
      required: true,
      date: true,
    },
    tipo_mantenimiento: {
      required: true,
    },
    vehiculo: {
      required: true,
    },
    repuestos: {
      required: true,
    },
    
  },
    messages: {
        fecha_mantenimiento: {
        required: "Por favor, ingrese la fecha del mantenimiento.",
        date: "Por favor, ingrese una fecha válida.",
        },
        tipo_mantenimiento: {
        required: "Por favor, seleccione un tipo de mantenimiento.",
        },
        vehiculo: {
        required: "Por favor, seleccione un vehículo.",
        },
        repuestos: {
        required: "Por favor, seleccione al menos un repuesto.",
       },
    },
    errorClass: "invalid-feedback",
  errorElement: "div",
  highlight: function (element) {
    $(element).addClass("is-invalid");
  },
  unhighlight: function (element) {
    $(element).removeClass("is-invalid");
  },
  submitHandler: function (form) {
    form.submit(); // * Si todo está validado correctamente
  },
});
