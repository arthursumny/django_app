document.addEventListener("DOMContentLoaded", function () {
    const addQuestaoButton = document.getElementById("add-questao-btn");
    const questaoContainer = document.getElementById("questao-container");
    const addQuestaoButton1 = document.getElementById("add-questao-btn1");
    const questaoContainer1 = document.getElementById("questao-container1");
    const removeQuestaoButton = document.getElementById("remove-questao-btn");
    const removeQuestaoButton1 = document.getElementById("remove-questao-btn1");
    const imagemContainer = document.getElementById("imagem-container");

    addQuestaoButton1.addEventListener("click", function () {
        const newQuestaoDiv1 = document.createElement("div");
        newQuestaoDiv1.classList.add("questao1");

        const newQuestaoInput1 = document.createElement("input");
        newQuestaoInput1.setAttribute("type", "text");
        newQuestaoInput1.setAttribute("name", "questoes1");
        newQuestaoInput1.setAttribute("placeholder", "Título do Nível");

        const newAlternativasInput1 = document.createElement("input");
        newAlternativasInput1.setAttribute("type", "text");
        newAlternativasInput1.setAttribute("name", "alternativas1");
        newAlternativasInput1.setAttribute("placeholder", "Ex: Explicação do Nível");

        const pontuacaoInput1 = document.createElement("input");
        pontuacaoInput1.setAttribute("type", "text");
        pontuacaoInput1.setAttribute("name", "pontuacao");
        pontuacaoInput1.setAttribute("placeholder", "Pontuação");

        pontuacaoInput1.addEventListener("change", function () {
            const pontuacao = pontuacaoInput1.value || 0;
            const alternativaTexto = newAlternativasInput1.value.split("#")[0];
            newAlternativasInput1.value = `${alternativaTexto}#${pontuacao}`;
        })

        pontuacaoInput1.addEventListener("blur", function () {
            if (pontuacaoInput1.value.trim() === "") {
                const alternativaTexto = newAlternativasInput1.value.split("#")[0];
                newAlternativasInput1.value = alternativaTexto;
            }
        })



        newQuestaoDiv1.appendChild(newQuestaoInput1);
        newQuestaoDiv1.appendChild(newAlternativasInput1);
        newQuestaoDiv1.appendChild(pontuacaoInput1);
        questaoContainer1.appendChild(newQuestaoDiv1);
    })
      
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

    removeQuestaoButton.addEventListener("click", function () {
        const ultimaQuestao = questaoContainer.lastChild;
    
        if (ultimaQuestao && ultimaQuestao.classList.contains("questao")) {
            questaoContainer.removeChild(ultimaQuestao);
        }
    });
    removeQuestaoButton1.addEventListener("click", function () {
       const ultimoNivel = questaoContainer1.lastChild;

       if (ultimoNivel && ultimoNivel.classList.contains("questao1")) {
           questaoContainer1.removeChild(ultimoNivel);
       }
    });

    const form = document.getElementById("questionario-form");
        form.addEventListener("submit", function (event) {
            event.preventDefault();
            const questoesDivs = document.querySelectorAll(".questao");
            const questoesDivs1 = document.querySelectorAll(".questao1");
            const imagemDiv = document.querySelector(".name");
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

        const questoesAlternativasInput = document.getElementById("questoes-alternativas-input");
        questoesAlternativasInput.value = JSON.stringify(dadosQuestoesAlternativas);
        const questoesAlternativasInput1 = document.getElementById("questoes-alternativas-input1");
        questoesAlternativasInput1.value = JSON.stringify(dadosQuestoesAlternativas1);
        const imagemInput = document.getElementById("image");
        imagemInput.value = JSON.stringify(imagem);

        console.log("Formulário enviado!");
        form.submit();
    });

});