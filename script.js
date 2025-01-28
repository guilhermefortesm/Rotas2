document.getElementById('form-rota').addEventListener('submit', async (e) => {
    e.preventDefault();

    const pontoInicio = document.getElementById('ponto-inicio').value;
    const enderecos = document.getElementById('enderecos').value.split('\n').filter(endereco => endereco.trim() !== '');

    try {
        const response = await fetch('/criar-rota', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ponto_inicio: pontoInicio, enderecos: enderecos }),
        });

        const data = await response.json();

        // Exibir o QR Code e o link da rota
        document.getElementById('qr-code').src = data.qr_code_url;
        document.getElementById('route-link').href = data.route_url;
        document.getElementById('resultado').style.display = 'block';
    } catch (error) {
        alert('Erro ao criar a rota. Tente novamente.');
        console.error(error);
    }
});