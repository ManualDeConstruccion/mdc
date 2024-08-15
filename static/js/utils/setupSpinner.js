function setupSpinner(inputId, indicatorId, errorId) {
    const input = document.getElementById(inputId);
    const indicator = document.getElementById(indicatorId);
    const errorContainer = document.getElementById(errorId);

    // Mostrar spinner cuando el usuario modifica el input
    input.addEventListener('input', function () {
        if (!indicator.style.display || indicator.style.display === 'none') {
            indicator.style.display = 'block';
            indicator.innerHTML = `<div class="inline-block">
                                      <svg class="animate-spin h-5 w-5 text-green-700" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                      </svg>
                                    </div>`;
            // Ocultar mensaje de error si está visible
            errorContainer.style.display = 'none';
        }
    });

    // Manejar la respuesta después de la petición
    input.addEventListener('htmx:afterRequest', function (event) {
        try {
            var response = JSON.parse(event.detail.xhr.response);
            if (event.detail.successful) {
                indicator.innerHTML = `<div class="inline-block">
                                          <svg class="h-5 w-5 text-green-700" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                                            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                                          </svg>
                                        </div>`;
                setTimeout(() => indicator.style.display = 'none', 1500);
                errorContainer.style.display = 'none'; // Asegurarse que el mensaje de error también está oculto
            } else {
                indicator.style.display = 'none'; // Ocultar spinner
                var errorMessage = response.name ? response.name[0] : 'Error desconocido al guardar'; // Asume que los errores vienen en un array por campo
                errorContainer.textContent = errorMessage;
                errorContainer.style.display = 'block'; // Mostrar mensaje de error
            }
        } catch (e) {
            console.error('Error parsing response:', e);
            indicator.style.display = 'none'; // Ocultar spinner en caso de error al parsear
            errorContainer.textContent = 'Error de formato en la respuesta del servidor.';
            errorContainer.style.display = 'block'; // Mostrar mensaje de error de formato
        }
    });
}
