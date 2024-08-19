function setupCharacterCounter(inputId, counterId, maxLength) {
    const inputElement = document.getElementById(inputId);
    const counterElement = document.getElementById(counterId);

    // Actualiza el contador inicialmente
    updateCounter();

    // Escucha el evento 'input' para actualizar el contador y manejar el límite
    inputElement.addEventListener('input', updateCounter);

    function updateCounter() {
        let currentLength = inputElement.value.length;

        // Si se supera el límite, truncar el texto
        if (currentLength > maxLength) {
            inputElement.value = inputElement.value.substring(0, maxLength);
            currentLength = maxLength; // Actualizar la longitud después de truncar
        }

        // Actualizar el contador de caracteres
        counterElement.textContent = `${currentLength}/${maxLength} caracteres`;

        // Cambiar el color del contador si se excede el límite
        if (currentLength >= maxLength) {
            counterElement.style.color = 'red';
        } else {
            counterElement.style.color = 'inherit';
        }
    }
}
