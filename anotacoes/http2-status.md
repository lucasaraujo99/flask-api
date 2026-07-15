# Status HTTP

Status HTTP são respostas padronizadas que um servidor envia para o cliente, indicando o resultado de sua requisição.

## Categorias

- 1xx (Informativos): O servidor recebeu a requisição e está processando.
- 2xx (Sucesso): A ação foi recebida, compreendida e aceita com êxito (ex.: 200 OK).
- 3xx (Redirecionamento): O cliente deve tomar uma ação adicional para concluir a requisição (ex.: 301 Moved Permanently).
- 4xx (Erro no Cliente): A requisição contém sintaxe incorreta ou não pode ser processada (ex.: 404 Not Found).
- 5xx (Erro no Servidor): O servidor falhou ao atender uma requisição aparentemente válida (ex.: 500 Internal Server Error).

## Sucesso (200)

- **200** (OK)	Consulta ou operação realizada com sucesso.
- **201** (Created)	Um novo recurso foi criado (geralmente em um POST).
- **204** (No Content)	Operação realizada com sucesso, mas sem conteúdo para retornar (comum em DELETE).

## Erro do Cliente (400)

- **400**	(Bad Request) Dados enviados pelo cliente são inválidos ou malformados.
- **401**	(Unauthorized) Usuário não autenticado (token ausente ou inválido).
- **403**	(Forbidden)	Usuário autenticado, mas sem permissão para realizar a ação.
- **404**	(Not Found)	O recurso solicitado não existe.
- **405**	(Method Not Allowed) A URL existe, mas o método HTTP não é permitido.

## Erro do Servidor (500)
- **500**	(Internal Server Error)	Erro inesperado no servidor.