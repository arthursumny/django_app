document.addEventListener("DOMContentLoaded", function () {
    const addQuestaoButton = document.getElementById("add-questao-btn");
    const questaoContainer = document.getElementById("questao-container");
    const addQuestaoButton1 = document.getElementById("add-questao-btn1");
    const questaoContainer1 = document.getElementById("questao-container1");

    // Função para adicionar uma nova questão e suas alternativas
    function addQuestao(container) {
        const newQuestaoDiv = document.createElement("div");
        newQuestaoDiv.classList.add("questao");

        const newQuestaoInput = document.createElement("input");
        newQuestaoInput.setAttribute("type", "text");
        newQuestaoInput.setAttribute("name", "questoes");
        newQuestaoInput.setAttribute("placeholder", "Título da Questão");

        const addAlternativaButton = document.createElement("button");
        addAlternativaButton.textContent = "Adicionar Alternativa";

        const alternativasDiv = document.createElement("div");

        addAlternativaButton.addEventListener("click", function () {
            const newAlternativasInput = document.createElement("input");
            newAlternativasInput.setAttribute("type", "text");
            newAlternativasInput.setAttribute("name", "alternativas");
            newAlternativasInput.setAttribute("placeholder", "Alternativa");

            alternativasDiv.appendChild(newAlternativasInput);
        });

        newQuestaoDiv.appendChild(newQuestaoInput);
        newQuestaoDiv.appendChild(addAlternativaButton);
        newQuestaoDiv.appendChild(alternativasDiv);
        container.appendChild(newQuestaoDiv);
    }

    // Lidar com o clique no botão "Adicionar Questão"
    addQuestaoButton.addEventListener("click", function () {
        addQuestao(questaoContainer);
    });

    // Lidar com o clique no botão "Adicionar Nível"
    addQuestaoButton1.addEventListener("click", function () {
        addQuestao(questaoContainer1);
    });

    const form = document.getElementById("questionario-form");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Impedir o envio padrão do formulário
        const questoesDivs = document.querySelectorAll(".questao");
        const questoesDivs1 = document.querySelectorAll(".questao1");
        const dadosQuestoesAlternativas1 = [];
        const dadosQuestoesAlternativas = [];

        questoesDivs1.forEach(function (questaoDiv1) {
            const questaoTitulo1 = questaoDiv1.querySelector("[name='questoes1']").value.trim(); 
            const alternativasTexto1 = questaoDiv1.querySelector("[name='alternativas1']").value.trim();

            if (questaoTitulo1 !== "") {

                const questaoAlternativas1 = {
                    questao1: questaoTitulo1,
                    alternativas1: alternativasTexto1,
                };

                dadosQuestoesAlternativas1.push(questaoAlternativas1);
            }
        })

    questoesDivs.forEach(function (questaoDiv) {
        const questaoTitulo = questaoDiv.querySelector("[name='questoes']").value.trim(); 
        const alternativasInputs = questaoDiv.querySelectorAll("[name='alternativas']");
        const alternativasArray = [];

        alternativasInputs.forEach(function (alternativaInput) {
            const alternativaTexto = alternativaInput.value;
                if (alternativaTexto !== "") 
                    alternativasArray.push(alternativaTexto);
            
        });

        if (questaoTitulo !== "" && alternativasArray.length > 0) {
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
    const questoesAlternativasInput1 = document.getElementById("questoes-alternativas-input1");
    questoesAlternativasInput1.value = JSON.stringify(dadosQuestoesAlternativas1);

    console.log("Formulário enviado!");
    form.submit();
    });
});