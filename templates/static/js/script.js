$('#schedule-form').submit(function(event) {
    event.preventDefault();

    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(data) {
        console.log(data);
        console.log('Sucesso');
      },
      error: function(xhr, errmsg, err) {
      console.log('Erro');
      }
    });
});

$('#company_supplier_add-form').submit(function(event) {
    event.preventDefault();

    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(data) {
        console.log(data);
        console.log('Sucesso');
      },
      error: function(xhr, errmsg, err) {
      console.log('Erro');
      }
    });
});

$('#company_shipping_new-form').submit(function(event) {
    event.preventDefault();

    $.ajax({
      type: 'POST',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      dataType: 'json',
      success: function(data) {
        console.log(data);
        console.log('Sucesso');
      },
      error: function(xhr, errmsg, err) {
      console.log('Erro' + errmsg);
      }
    });
});

$(document).ready(function() {
  $(".delete-link").on("click", function(e) {
    e.preventDefault();
    var url = $(this).attr("href");

    // Envia a solicitação AJAX para excluir o objeto Schedule
    $.ajax({
      url: url,
      type: "POST",
      data: {
        csrfmiddlewaretoken: "{{ csrf_token }}"
      },
      success: function(response) {
        // Atualize a tabela ou execute outras ações apropriadas após a exclusão bem-sucedida
        // ...
      },
      error: function(xhr, status, error) {
        // Trate erros de solicitação ou execute ações apropriadas em caso de falha na solicitação AJAX
        // ...
      }
    });
  });

     // Tratamento de CEPs e Endereços
     $('#cep').on('input', function() {
      var cep = $(this).val().replace(/\D/g, '');
      if (cep.length === 8) {
        cep = cep.substring(0, 5) + '-' + cep.substring(5);
      }
      $(this).val(cep);
    });
    $('#cep').on('blur', function() {
      var cep = $(this).val().replace(/\D/g, '');
      if (cep !== '') {
        var validacep = /^[0-9]{8}$/;
        if (validacep.test(cep)) {
          obterEndereco(cep);
        } else {
          limparCampos();
          alert('Formato de CEP inválido.');
        }
      } else {
        limparCampos();
      }
    });

    function obterEndereco(cep) {
      var nominatimUrl = 'https://nominatim.openstreetmap.org/search?postalcode=' + cep + '&format=json&limit=1';
      $.getJSON(nominatimUrl, function(data) {
        if (data.length > 0) {
          var latitude = data[0].lat;
          var longitude = data[0].lon;
          $('#latitude').val(latitude);
          $('#longitude').val(longitude);
          obterDetalhesEndereco(cep);
        } else {
          limparCampos();
          alert('Não foi possível obter as informações de latitude e longitude para o CEP fornecido.');
        }
      });
    }

    function obterDetalhesEndereco(cep) {
      var viaCepUrl = 'https://viacep.com.br/ws/' + cep + '/json/';
      $.getJSON(viaCepUrl, function(data) {
        if (!('erro' in data)) {
          $('#logradouro').val(data.logradouro);
          $('#bairro').val(data.bairro);
          $('#cidade').val(data.localidade);
          $('#estado').val(data.uf);
        } else {
          limparCampos();
          alert('CEP não encontrado.');
        }
      });
    }

    function limparCampos() {
      $('#logradouro').val('');
      $('#bairro').val('');
      $('#cidade').val('');
      $('#estado').val('');
      $('#latitude').val('');
      $('#longitude').val('');
    }

        $('#cep').on('input', function() {
      var cep = $(this).val().replace(/\D/g, '');
      if (cep.length === 8) {
        cep = cep.substring(0, 5) + '-' + cep.substring(5);
      }
      $(this).val(cep);
    });
    $('#cep').on('blur', function() {
      var cep = $(this).val().replace(/\D/g, '');
      if (cep !== '') {
        var validacep = /^[0-9]{8}$/;
        if (validacep.test(cep)) {
          obterEndereco(cep);
        } else {
          limparCampos();
          alert('Formato de CEP inválido.');
        }
      } else {
        limparCampos();
      }
    });

    function obterEndereco(cep) {
      var nominatimUrl = 'https://nominatim.openstreetmap.org/search?postalcode=' + cep + '&format=json&limit=1';
      $.getJSON(nominatimUrl, function(data) {
        if (data.length > 0) {
          var latitude = data[0].lat;
          var longitude = data[0].lon;
          $('#latitude').val(latitude);
          $('#longitude').val(longitude);
          obterDetalhesEndereco(cep);
        } else {
          limparCampos();
          alert('Não foi possível obter as informações de latitude e longitude para o CEP fornecido.');
        }
      });
    }

    function obterDetalhesEndereco(cep) {
      var viaCepUrl = 'https://viacep.com.br/ws/' + cep + '/json/';
      $.getJSON(viaCepUrl, function(data) {
        if (!('erro' in data)) {
          $('#logradouro').val(data.logradouro);
          $('#bairro').val(data.bairro);
          $('#cidade').val(data.localidade);
          $('#estado').val(data.uf);
        } else {
          limparCampos();
          alert('CEP não encontrado.');
        }
      });
    }

    function limparCampos() {
      $('#logradouro').val('');
      $('#bairro').val('');
      $('#cidade').val('');
      $('#estado').val('');
      $('#latitude').val('');
      $('#longitude').val('');
    }
});


function recarregarPagina() {
  setTimeout(function() {
    location.assign(location.href);
  }, 100);
}

function toggleMode() {
    var body = document.body;
    if (body.classList.contains("dark-mode")) {
        body.classList.remove("dark-mode");
    } else {
        body.classList.add("dark-mode");
    }
}
