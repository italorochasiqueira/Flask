document.querySelectorAll(".table-cadastros th[data-col]").forEach((th) => {
    let asc = true;

    th.addEventListener("click", () => {
        const table = th.closest("table");
        const tbody = table.querySelector("tbody");
        const rows = Array.from(tbody.querySelectorAll("tr"));
        const index = th.dataset.col;

        // Resetar ícones dos outros cabeçalhos
        document.querySelectorAll(".sort-icon").forEach(icon => {
            icon.className = "bi bi-arrow-down-up sort-icon";
        });

        rows.sort((a, b) => {
            const A = a.children[index].innerText.toLowerCase();
            const B = b.children[index].innerText.toLowerCase();
            return asc ? A.localeCompare(B) : B.localeCompare(A);
        });

        // Atualizar ícone do cabeçalho clicado
        const icon = th.querySelector(".sort-icon");
        icon.className = asc
            ? "bi bi-arrow-down sort-icon"
            : "bi bi-arrow-up sort-icon";

        asc = !asc;
        rows.forEach(tr => tbody.appendChild(tr));
    });
});

document.addEventListener("click", function (e) {

    const btn = e.target.closest(".btn-editar");
    if (!btn) return;

    // Preenche o formulário
    document.getElementById("id_cadastro").value = btn.dataset.id;
    document.getElementById("cdc").value = btn.dataset.cdc;
    document.getElementById("descricao").value = btn.dataset.descricao;
    document.getElementById("nome").value = btn.dataset.nome;
    document.getElementById("email").value = btn.dataset.email;

    // Muda botão salvar
    const btnSalvar = document.querySelector(".btn-salvar-edit");
    btnSalvar.innerHTML = `<i class="bi bi-check2"></i> Atualizar`;
    btnSalvar.classList.add("modo-edicao");

});

document.addEventListener("click", function (e) {
    if (e.target.classList.contains("btn-excluir")) {
        const id = e.target.dataset.id;

        

        if (!confirm("Deseja realmente excluir este registro?")) return;

        fetch(`/cadastro/excluir/${id}`, {
            method: "DELETE"
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                e.target.closest("tr").remove();
            } else {
                alert("Erro ao excluir");
            }
        })
        .catch(() => alert("Erro de comunicação com o servidor"));
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const btnLimpar = document.querySelector(".btn-limpar");

    if (!btnLimpar) return;

    btnLimpar.addEventListener("click", () => {
        document.querySelector("#cdc").value = "";
        document.querySelector("#descricao").value = "";
        document.querySelector("#nome").value = "";
        document.querySelector("#email").value = "";
    });
});

