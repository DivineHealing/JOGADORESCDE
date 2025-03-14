$(document).ready(function() {

    //Ao submeter o formulário
    $('#conjuntoForm').submit(function(event){
        //Valida se todos campos estão preenchidos
        let formValido = true;

        $('.peca-form:not(.hidden)').each(function(){ //Para cada peça visivel, verifica se os forms estão preenchidos
            $(this).find('input, select, textarea').each(function(){
                if (!$(this).val()){ //Se não preencheu
                    formValido = false;
                    $(this).addClass('invalid'); //Adiciona a classe para mostrar que é inválido
                } else {
                    $(this).removeClass('invalid');
                }
            });
        });

        if(!formValido){
            alert('Preencha todos os campos das peças visíveis.');
            event.preventDefault(); // Impede o envio do formulário
            return; //Para a execução
        }

        // Se chegou até aqui, o formulário é válido e será submetido
    });

    //Ao clicar na imagem
    $('area.map-link').click(function(e) {
        e.preventDefault(); // Impede o comportamento padrão do link

        const targetId = $(this).data('target'); // Pega o ID do alvo (data-target)
        console.log("Target ID:", targetId);


        // Esconde todos os formulários de peças
        $('.peca-form').addClass('hidden');


        // Remove a classe 'active' de todas as áreas
        $('area').removeClass('active');

        if(targetId != 'conjunto-form'){
             // Mostra o formulário da peça correspondente
            const $targetForm = $('#' + targetId);
            $targetForm.removeClass('hidden');


            // Define o nome da peça no título do formulário
            const nomePeca = $(this).attr('alt'); // Pega o nome da peça do atributo 'alt'
            $targetForm.find('.nome-peca').text(nomePeca);

            // Adiciona a classe 'active' à área clicada
            $(this).addClass('active');
             $('#form-oculto').show();
        } else {
            $('#form-oculto').hide();
        }
    });
});