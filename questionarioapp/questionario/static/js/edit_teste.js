function criarAlternativaInput() {
    const alternativaContainer = document.createElement("div");
    alternativaContainer.classList.add("input-container");

    const pontuacaoInput = document.createElement("input");
    pontuacaoInput.setAttribute("type", "text");
    pontuacaoInput.setAttribute("name", "pontuacao");
    pontuacaoInput.setAttribute("placeholder", "Pontuação");

    const newAlternativasInput = document.createElement("input");
    newAlternativasInput.setAttribute("type", "text");
    newAlternativasInput.setAttribute("name", "alternativas");
    newAlternativasInput.setAttribute("placeholder", "Alternativa");

    const removeAlternativaIcon = document.createElement("span");
    removeAlternativaIcon.textContent = "❌";
    removeAlternativaIcon.style.cursor = "pointer";
    removeAlternativaIcon.setAttribute("name", "remove-Alternativa-icon");
    removeAlternativaIcon.addEventListener("click", function () {
        alternativaContainer.removeChild(newAlternativasInput);
        alternativaContainer.removeChild(pontuacaoInput);
        alternativaContainer.removeChild(removeAlternativaIcon);
    });

    function atualizarAlternativa() {
        const pontuacao = pontuacaoInput.value || 0;
        const alternativaTexto = newAlternativasInput.value.split("#")[0];
        newAlternativasInput.value = `${alternativaTexto}#${pontuacao}`;
    }

    pontuacaoInput.addEventListener("input", atualizarAlternativa);

    pontuacaoInput.addEventListener("blur", function () {
        if (pontuacaoInput.value.trim() === "") {
            const alternativaTexto = newAlternativasInput.value.split("#")[0];
            newAlternativasInput.value = alternativaTexto;
        }
    });

    newAlternativasInput.addEventListener("input", atualizarAlternativa);

    alternativaContainer.appendChild(pontuacaoInput);
    alternativaContainer.appendChild(newAlternativasInput);
    alternativaContainer.appendChild(removeAlternativaIcon);
    alternativasDiv.appendChild(alternativaContainer);
}
