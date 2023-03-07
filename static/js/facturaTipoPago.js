const fechaPagoInput = document.getElementById('id_fecha_pago');
    const fechaVencimientoInput = document.getElementById('id_fecha_vencimiento');
    const tipoPagoSelect = document.querySelector('.tipo-pago-select');

    const toggleFechaCampos = () => {
      const tipoPago = tipoPagoSelect.value;
      if (tipoPago === 'Mensualidad') {
        fechaPagoInput.style.display = 'block';
        fechaVencimientoInput.style.display = 'block';
      } else {
        fechaPagoInput.style.display = 'none';
        fechaVencimientoInput.style.display = 'none';
      }
    }

    tipoPagoSelect.addEventListener('change', toggleFechaCampos);
    toggleFechaCampos(); // ejecutar una vez al cargar la página