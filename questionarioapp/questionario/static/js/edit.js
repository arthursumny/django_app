document.addEventListener("DOMContentLoaded", function () {
    const addQuestaoButton = document.getElementById("add-questao-btn");
    const questaoContainer = document.getElementById("questao-container");

    addQuestaoButton.addEventListener("click", function () {
        const newQuestaoDiv = document.createElement("div");
        newQuestaoDiv.classList.add("questao");

        const newQuestaoInput = document.createElement("input");
        newQuestaoInput.setAttribute("type", "text");
        newQuestaoInput.setAttribute("name", "questoes");
        newQuestaoInput.setAttribute("placeholder", "Título da Questão");

        const newAlternativasInput = document.createElement("input");
        newAlternativasInput.setAttribute("type", "text");
        newAlternativasInput.setAttribute("name", "alternativas");
        newAlternativasInput.setAttribute("placeholder", "Alternativas separadas por ;");

        newQuestaoDiv.appendChild(newQuestaoInput);
        newQuestaoDiv.appendChild(newAlternativasInput);
        questaoContainer.appendChild(newQuestaoDiv);
    });

     // Novo evento para salvar os dados das questões e alternativas
    const form = document.getElementById("questionario-form");
    form.addEventListener("submit", function () {
        const questoesDivs = document.querySelectorAll(".questao");
        const dadosQuestoesAlternativas = [];

        questoesDivs.forEach(function (questaoDiv) {
            const questaoTitulo = questaoDiv.querySelector("[name='questoes']").value.trim(); 
            const alternativasTexto = questaoDiv.querySelector("[name='alternativas']").value.trim(); 

            
            if (questaoTitulo !== "") {
                
                const alternativasArray = alternativasTexto.split(";");

                const questaoAlternativas = {
                    questao: questaoTitulo,
                    alternativas: alternativasArray,
                };

                dadosQuestoesAlternativas.push(questaoAlternativas);
            }
        });

        // Converter os dados em JSON e definir no campo oculto
        const questoesAlternativasInput = document.getElementById("questoes-alternativas-input");
        questoesAlternativasInput.value = JSON.stringify(dadosQuestoesAlternativas);
    });
});