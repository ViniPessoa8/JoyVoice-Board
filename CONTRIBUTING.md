# Contribuindo para JoyVoice Board
A seguir há uma lista de diretrizes para contribuir com o projeto. São regras e recomendações para facilitar o entendimento da sua contribuição. Lembre-se de ser descritivo e fique a vontade para fazer um pull request.

## Sumário

### [Formas de contribuir](#formas-de-contribuir)
- [Reportando Bugs](#reportando-bugs)
- [Implementando Melhorias](#implementando-melhorias)
- [Sugestão de melhorias](#sugerindo-melhorias)

### [Guia para contribuir](#guia-para-contribuir)

### [Padrões](#padrões)
- [Mensagens de Commit](#mensagens-de-commit)
- [Pull Requests](#pull-requests)
- [Labels](#labels)

# Formas de contribuir
## Reportando Bugs
Se você encontrou algum bug, [crie uma issue](https://github.com/ViniPessoa8/JoyVoice-Board/issues/new) utilizando a label `bug`.

Se estiver inspirado, pode fazer um [pull request](#pull-requests) corrigindo o erro. :) 

Só não esqueça de referenciar a issue criada, para que possamos saber qual o problema você está resolvendo com aquele pull request.

## Implementando Melhorias
Há uma lista de [issues](https://github.com/ViniPessoa8/JoyVoice-Board/issues) que você pode resolver. Além disso, na documentação do projeto há mais tarefas a serem desenvolvidas.

Escolha uma e atribua-se à ela.
- Se for uma **Issue**, atribua seu usuário do github à ela.
- Se for uma **tarefa na documentação do projeto**, mova-a para a coluna 'Fazendo' e, se posssível, atribua-se à tarefa. 

## Sugerindo Melhorias
Acha que falta alguma coisa no projeto? Viu algo que pode ser melhorado?

[Crie uma issue](https://github.com/ViniPessoa8/JoyVoice-Board/issues/new), utilizando a label `melhoria`, e informe sua sugestão.

# Guia para contribuir
### **1. Faça um Fork do projeto**
Para poder trabalhar na função sem atrabalhar outros contribuíntes, faça um `fork` do projeto. 

(TODO: Imagem ilustrativa)
### **2. Crie uma branch para a sua contribuição.**
A partir da branch mais recente do desenvolvimento, crie a branch da sua função ou melhoria. O nome da branch deve refletir o que será adicionado.

Por exemplo:
- `feat/tocar_som`
- `hotfix/remover_delay`

Para um referência melhor sobre branches, acesse [esse link](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=O%20conjunto%20de%20ferramentas%20git,tem%20um%20processo%20de%20instala%C3%A7%C3%A3o.).
### **3. Faça os devidos commits**
Adicione sua contribuição através de commits na sua nova branch. Não se sequeceça de usar o [padrão de mensagens de commit](#mensagens-de-commit)
### **4. Faça um Pull Request para o repositório.**
Ao [criar um Pull Request](https://github.com/ViniPessoa8/JoyVoice-Board/compare), você deve descrever bem aquilo que foi adicionado, pontuando o que está sendo resolvido e como está sendo resolvido.

Quanto mais descrição, melhor ;)

### **Pronto!**
Sua contribuição já está em revisão e será analisada pelo nosso time. 

Muito obrigado!

# Padrões
## Mensagens de Commit
- Use o **tempo presente** ("Adiciona função..." e não "Adicionei função...")
- **Não** coloque **ponto final** (.)
- Deve-se utilizar **prefixos** antes de todo commit.
- **Prefixos**:
  - feat     : Nova função
  - fix      : Resolução de bugs
  - docs     : Mundanças em documentação
  - style    : Formatação do código (ex. identar, remover linhas em branco)
  - refactor : Refatoração de código em produção (ex. renomear variável)
  - test     : Adição de testes
  - clean    : Remoção de código morto/arquivos 
  
  *Obs: Os prefixos estão em inglês por conta da pouca quantidade de caracteres utilizada. 
  
  Exemplos: 
  - `feat: adiciona botão iniciar`
  - `fix: corrige erro na conversão do valor`
  - `docs: adiciona sessão 'Contribuição' no README.md`
  - `style: corrige identação da classe 'Soundboard'.`
  - `refactor: renomeia varáveis da classe 'Efeito'.`
  - `test: cria teste de tocar som.`
  - `clean: remove arquivo 'teste.py'`

## Pull Requests
Ao fazer um pull request, deve-se atentar para a branch a qual você quer mesclar, e também qual issue você está resolvendo.

Você pode (e deve) fazer um _pull request_ (PR) referenciando uma issue. Para isso deve-se adicionar o id da issue (#). Isso pode ser feito tanto no título do PR, quanto na descrição. 

Exemplo: 
- `Resolve problema da issue #20`
- `Adiciona a função xxxx ref #9` 

Outro ponto importante é utilizar as [labels](https://github.com/ViniPessoa8/JoyVoice-Board/labels) apropriadas.

## Labels
As labels disponíveis para utilização estão [aqui](https://github.com/ViniPessoa8/JoyVoice-Board/labels).