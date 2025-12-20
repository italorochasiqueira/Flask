function iniciarCadastro() {
    const form = document.querySelector("#form-cadastro");
    if (!form) return;

    form.addEventListener("submit", e => {
        e.preventDefault();

        const cadastro = {
            cdc: document.querySelector("#cdc").value,
            descricao: document.querySelector("#descricao").value,
            nome: document.querySelector("#nome").value,
            email: document.querySelector("#email").value
        };

        fetch("/salvar-cadastro", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(cadastro)
        })
        .then(res => res.json())
        .then(() => {
            alert("Cadastro salvo com sucesso!");
            form.reset();
        });
    });
}
