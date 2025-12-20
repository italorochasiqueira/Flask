document.querySelectorAll('[data-page]').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();

        const page = link.dataset.page;

        fetch(`html/${page}.html`)
            .then(response => response.text())
            .then(html => {
                document.getElementById('content').innerHTML = html;
                    if (page === "pag_cadastrar") {
                        iniciarCadastro();
                    }
            })
            .catch(() => {
                document.getElementById('content').innerHTML =
                    '<p>Erro ao carregar o conteúdo.</p>';
            });
    });
});