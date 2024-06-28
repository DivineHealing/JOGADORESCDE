function alterar() {
    const forca = parseFloat(document.getElementById('forca').value) || 0; // Status Força


    fetch('/atrstatus', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ forca: forca})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('forcat').textContent = `${data.javaforca.toLocaleString('pt-BR')}`;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}