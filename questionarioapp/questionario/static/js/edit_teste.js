addQuestaoButton.addEventListener("click", function () {
    const newQuestaoDiv = document.createElement("div");
    newQuestaoDiv.classList.add("questao");

    const newQuestaoInput = document.createElement("input");
    newQuestaoInput.setAttribute("type", "text");
    newQuestaoInput.setAttribute("name", "questoes");
    newQuestaoInput.setAttribute("placeholder", "Título da Questão");

    const addAlternativaButton = document.createElement("span");
    addAlternativaButton.innerHTML = '<i class="fas fa-plus-circle"></i>';
    addAlternativaButton.style.cursor = "pointer";
    addAlternativaButton.classList.add("add-Alternativa-icon");
    addAlternativaButton.addEventListener("click", criarAlternativaInput);

    const alternativasDiv = document.createElement("div");
    alternativasDiv.classList.add("input-container");

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
    
        pontuacaoInput.addEventListener("change", atualizarAlternativa);

        pontuacaoInput.addEventListener("blur", function () {
            if (pontuacaoInput.value.trim() === "") {
                const alternativaTexto = newAlternativasInput.value.split("#")[0];
                newAlternativasInput.value = alternativaTexto;
            }
        });

        alternativaContainer.appendChild(newAlternativasInput);
        alternativaContainer.appendChild(removeAlternativaIcon);
        alternativaContainer.appendChild(pontuacaoInput);
        alternativasDiv.appendChild(alternativaContainer);
    }

    addAlternativaButton.addEventListener("click", criarAlternativaInput);

    criarAlternativaInput(); 

    newQuestaoDiv.appendChild(newQuestaoInput);
    newQuestaoDiv.appendChild(addAlternativaButton);
    newQuestaoDiv.appendChild(alternativasDiv);
    questaoContainer.appendChild(newQuestaoDiv);
});