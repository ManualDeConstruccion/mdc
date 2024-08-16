function autoResizeTextarea(textareaId) {
    const textarea = document.getElementById(textareaId);

    function adjustHeight() {
        textarea.style.height = 'auto'; // Resetea la altura para calcular correctamente
        textarea.style.height = (textarea.scrollHeight) + 'px'; // Ajusta la altura al contenido
    }

    // Ajustar la altura cuando se introduce texto
    textarea.addEventListener('input', adjustHeight);

    // Ajustar la altura al cargar la página
    window.addEventListener('load', adjustHeight);

    // Llama a adjustHeight inicialmente para ajustar el tamaño en caso de contenido precargado
    adjustHeight();
}

// Llama a la función para el textarea específico
autoResizeTextarea('inputtitle');
