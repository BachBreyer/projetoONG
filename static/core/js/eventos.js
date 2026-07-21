document.addEventListener("DOMContentLoaded", function () {
    const botoesDetalhes = document.querySelectorAll(".btn-detalhes-evento");

    botoesDetalhes.forEach(botao => {
        botao.addEventListener("click", function () {
            const titulo = this.getAttribute("data-titulo");
            const descricao = this.getAttribute("data-descricao");
            const local = this.getAttribute("data-local");
            const data = this.getAttribute("data-data");

            document.getElementById("modalEventoTitulo").innerText = titulo;
            document.getElementById("modalEventoDescricao").innerText = descricao;
            document.getElementById("modalEventoLocal").innerText = local;
            document.getElementById("modalEventoData").innerText = data;

            const modal = new bootstrap.Modal(document.getElementById("modalDetalhesEvento"));
            modal.show();
        });
    });
});
