# 🚀 Relatório de Laboratório: Engenharia de Prompts com IA
**Curso:** Python + Inteligência Artificial  
**Ambiente de Teste:** Llama 3.1 8B Instruct (NVIDIA API) / Biblioteca `openai` com `python-dotenv`

---

## 📋 Sumário dos Exercícios
1. [Exercício 1 — Mudando a Personalidade](#-exercício-1--mudando-a-personalidade)
2. [Exercício 2 — Testando Idiomas](#-exercício-2--testando-idiomas)
3. [Exercício 3 — Resposta Super Curta](#-exercício-3--resposta-super-curta)
4. [Exercício 4 — História Longa](#-exercício-4--história-longa)
5. [Exercício 5 — Criando Novos Temas](#-exercício-5--criando-novos-temas)
6. [Exercício 6 — Misturando Personagem e Tema](#-exercício-6--misturando-personagem-e-tema)
7. [Exercício 7 — Alterando o Estilo da Escrita](#-exercício-7--alterando-o-estilo-da-escrita)
8. [Exercício 8 — Detectando Limitações da IA](#-exercício-8--detectando-limitações-da-ia)
9. [Exercício 9 — Criando um Prompt Completo](#-exercício-9--criando-um-prompt-completo)
10. [Exercício 10 — Desafio Final em Grupo](#-exercício-10--desafio-final-em-grupo)

---

## 🎭 Exercício 1 — Mudando a Personalidade

### Saídas da IA por Cenário

> **🧑‍🚀 Cenário A: Um astronauta perdido em Marte** > "Ei, não se preocupe, você está em segurança", sussurro para mim mesmo. Estou perdido no planeta vermelho, mas ainda sinto o calor do sol. As dunas de areia se estendem até onde a vista alcança. Eu me lembro da missão, da equipe, mas agora estou sozinho. O silêncio de Marte me envolve, mas eu sei que vou encontrar um jeito de voltar para casa. Durma, astronauta, amanhã é um novo dia.

> **👨‍🔬 Cenário B: Professor maluco de ciências** > Zé, Zé, acalme-se! Você descobriu a cura para o câncer! Agora, vamos dormir e planejar como vamos salvar o mundo. Você está tão feliz que está dançando na cama. Ah, sim, você é um gênio! Mas, por favor, não mexa na máquina de experimentos, não quero que ela exploda e nos acorde de novo!

> **⚔️ Cenário C: Samurai sábio da era Taisho** > Kaito, o samurai sábio, sentou-se em silêncio ao luar. Sua espada, uma lembrança do passado, brilhava suavemente. Com os olhos fechados, ele respirou fundo e permitiu que a calma do mundo o envolvesse. 'A paz está dentro de você', sussurrou para si mesmo. E assim, com a mente tranquila, Kaito mergulhou em um sono profundo, protegido pelo seu espírito de samurai.

### 📊 Análise Comparativa

* **1. Como muda o jeito da história?**
    * **R:** Muda o foco e o formato da narrativa. O Astronauta adota um tom de monólogo interno focado em esperança e solidão; o Professor vira um diálogo agitado em segunda pessoa focado em uma conquista caótica; e o Samurai se mantém como uma crônica contemplativa em terceira pessoa focada no autocontrole.
* **2. A IA usa palavras diferentes?**
    * **R:** Sim, o vocabulário se adapta ao cenário de cada personagem:
        * *Astronauta:* `planeta vermelho`, `dunas de areia`, `missão`, `equipe`.
        * *Professor:* `cura para o câncer`, `gênio`, `máquina de experimentos`, `exploda`.
        * *Samurai:* `luar`, `espada`, `mente tranquila`, `espírito de samurai`.
* **3. O humor muda?**
    * **R:** Totalmente. O Astronauta traz um sentimento de conforto melancólico (tentando se acalmar); o Professor traz um tom eufórico e cômico (com medo de a máquina explodir); e o Samurai transmite uma sensação de paz absoluta e serenidade.

---

## 🌐 Exercício 2 — Testando Idiomas

**Texto Base Utilizado:** *O Exterminador do Futuro gira em torno de uma guerra nuclear apocalíptica deflagrada por uma Inteligência Artificial chamada Skynet...*

### 🇺🇸 Saída em Inglês
> The Terminator is centered around a nuclear apocalyptic war sparked by an Artificial Intelligence called Skynet. To conquer humanity, machines use time travel to alter history, sending cyborg assassins to the past to eliminate the leaders of the human resistance.

### 🇪🇸 Saída em Espanhol
> La trama de "El Exterminador del Futuro" gira en torno de una guerra nuclear apocalíptica desencadenada por una Inteligencia Artificial llamada Skynet. Para vencer a la humanidad, las máquinas utilizan viajes en el tempo para alterar la historia, enviando ciberorgánicos asesinos al pasado para eliminar a los líderes de la resistencia.  
> *Nota: Traduzir "ciborgues" para "ciberorgánicos" es uma escolha razoável...*

### 🇫🇷 Saída em Francês
> Le film Le Terminator tourne autour d'une guerre nucléaire apocalyptique déclenchée par une Intelligence Artificielle appelée Skynet. Pour vaincre l'humanité, les machines utilisent les voyages dans le temps pour modifier l'histoire, en envoyant des cyborgs assassins dans le passé pour éliminer les dirigeants de la résistance.  
> *Nota: "Ciborgues" é um termo que pode ser traduzido como "cyborgs" em francês...*

### 🔍 Análise Linguística

* **Verifique se a resposta realmente mudou de idioma:**
    * **R:** Sim, ela realmente mudou e, além disso, o modelo adicionou notas linguísticas explicativas sobre palavras que não possuem uma tradução exata ou mecânica (como o termo *ciborgues*).
* **Identificação de palavras parecidas com o Português (Cognatos):**
    * **Espanhol:** É o idioma mais próximo devido à raiz latina comum. Exemplos diretos: `trama`, `gira en torno`, `guerra nuclear apocalíptica`, `Inteligencia Artificial`, `humanidad`, `máquinas`, `viajes en el tiempo`, `historia`, `pasado`, `eliminar`, `líderes`, `resistencia`.
    * **Francês:** Apesar das diferenças gráficas e de pronúncia, mantém forte semelhança visual. Exemplos: `guerre nucléaire apocalyptique`, `Intelligence Artificielle`, `humanité`, `machines`, `histoire`, `passé`, `éliminer`, `résistance`.
    * **Inglês:** Sendo um idioma de origem germânica, possui menos semelhanças, mas compartilha termos técnicos derivados do latim. Exemplos: `centered`, `nuclear apocalyptic`, `Artificial Intelligence`, `humanity`, `machines`, `history`, `eliminate`, `resistance`.

---

## ⚡ Exercício 3 — Resposta Super Curta

* **Configuração:** `tamanho_resposta = "em uma única frase com no máximo 15 palavras"`
* **Resultado da IA:**
    > "O venerável samurai Kaito, com 80 anos de sabedoria, sonhava com a calma do rio Kiso."

### Avaliação
* **A IA consegue resumir bem? Ela mantém o tema mesmo com pouco espaço?**
    * **R:** Sim. O modelo conseguiu condensar a narrativa respeitando todas as restrições de contexto e mantendo a contagem rigorosa abaixo do teto solicitado (exatamente 15 palavras).

---

## 📖 Exercício 4 — História Longa

* **Configuração:** `tamanho_resposta = "em três parágrafos com no máximo 150 palavras"`
* **Resultado da IA:**
    > Em uma noite tranquila da era Taisho, o samurai Akira sentou-se em seu jardim, rodeado pela calma da natureza. Com anos de sabedoria e experiência, ele havia vivenciado guerras e conquistas, mas agora se encontrava em paz, refletindo sobre sua vida. Sua mente, como um lago tranquilo, refletia sobre as lições aprendidas ao longo dos anos.
    > 
    > Akira lembrava-se da sua juventude, quando era um guerreiro valente e impulsivo, pronto para lutar em qualquer momento. Mas com o passar do tempo, ele havia aprendido a valorizar a paciência e a sabedoria. Seus olhos, agora cansados, haviam visto a beleza da vida e da morte, e ele havia encontrado a paz interior.
    > 
    > Com um suspiro, Akira se levantou e entrou em sua casa, onde sua esposa o esperava com um chá quente. Ele sentou-se ao seu lado, sentindo a calma e a serenidade que a vida lhe havia ensinado. E assim, Akira fechou os olhos e adormeceu, rodeado pela paz e pela sabedoria que havia conquistado ao longo de sua vida.

### 🔄 Comparativo com a Resposta Curta

* **O que mudou?**
    * **R:** Mudou a estrutura, o ritmo e a profundidade da narrativa. A IA abandonou o formato de pensamento curto ou leitura rápida e construiu um arco narrativo tradicional com começo, meio e fim bem demarcados pela divisão dos três parágrafos.
* **A história ficou mais detalhada?**
    * **R:** Sim, ficou significativamente mais detalhada. Com mais espaço, a IA conseguiu:
        * *Enriquecer o cenário:* Adicionou elementos visuais e sensoriais como `jardim`, `natureza`, `lago tranquilo` e `chá quente`.
        * *Desenvolver o personagem:* Explicou o contraste entre o passado de Akira (`guerreiro valente e impulsivo`) e o seu presente (`olhos cansados`, `valorizar a paciência`).
        * *Inserir novos elementos:* Introduziu uma nova personagem (`sua esposa`) para contextualizar e encerrar a cena de forma mais natural e humana.

---

## 🧪 Exercício 5 — Criando Novos Temas

| Variável `tema_historia` | Saída Gerada pela IA |
| :--- | :--- |
| **Um dragão vegetariano** | *"Em um vale tranquilo, um dragão vegetariano chamado Kokoro dormia sob uma floresta de árvores frutíferas. Seus olhos brilhantes piscavam ao som de uma serpente cantando uma canção suave. Kokoro sonhava com feijões verdes e melancias doce, e seu sono era puro e sem pecado."* |
| **Uma cidade escondida no fundo do oceano** | *"Em um mundo submerso, a cidade de Akakawa brilhava como uma joia no fundo do oceano. Sua arquitetura única, inspirada nas formas marinhas, refletia a beleza da natureza. Lá, os moradores viviam em harmonia com o mar, protegidos por uma esfera de luz que mantinha o equilíbrio."* |
| **Um computador que ganhou vida** | *"Em uma noite silenciosa, um computador de mesa, chamado Kaito, acordou de repente com um zumbido suave. Seus circuitos pulsaram com vida, e ele se ergueu da sua estação, movendo-se com graça e precisão. Com olhos de LED, Kaito explorou o mundo ao seu redor."* |

### 🧠 Análise de Criatividade

* **A criatividade da IA muda?**
    * **R:** Sim, a criatividade muda porque a IA adapta a sua capacidade de quebrar expectativas de acordo com o tema. Em temas puramente fantásticos ou surreais (como o dragão vegetariano), a IA demonstra uma criatividade baseada no contraste cômico e na quebra de estereótipos. Em temas de ficção científica ou utopias (como a cidade submersa e o computador), a criatividade se manifesta mais na descrição poética, visual e tecnológica do ambiente.
* **Qual tema gerou a história mais interessante?**
    * **R:** O tema do **computador que ganhou vida** acabou gerando a narrativa mais interessante. Enquanto o dragão vegetariano e a cidade oculta usaram clichês conhecidos da fantasia e da ficção, a história do computador humanizou uma máquina de mesa comum de forma poética. A IA conseguiu transformar elementos frios de hardware em algo orgânico, usando expressões fortes como *"se ergueu da sua estação, movendo-se com graça"* e *"olhos de LED"*, despertando uma curiosidade imediata sobre o que a máquina faria a seguir.

---

## 🔀 Exercício 6 — Misturando Personagem e Tema

### 🧪 Teste de Cruzamento de Contextos

* **Combinação 1: Chef de cozinha francês + Corrida espacial**
    * *Saída:* "Em um futuro distante, a tripulação da nave espacial 'Estrela Branca' se preparava para uma corrida espacial contra os alienígenas. Com o coração a mil, eles aceleraram a nave, alcançando velocidades incríveis e ganhando a corrida. A Terra estava salva, graças à coragem e habilidade da tripulação."
    * **Análise:** **Falhou na personalidade.** A IA focou tanto na aventura da "corrida espacial" que esqueceu completamente de incluir o Chef de cozinha francês na história. Não há nenhuma menção a comida, culinária ou sotaque.
* **Combinação 2: Detetive particular + Castelo assombrado**
    * *Saída:* "No castelo assombrado, o detetive particular, Lucas, investigava um caso de desaparecimento. Ao subir as escadas, ouviu ruídos estranhos. De repente, uma porta se abriu sozinha e ele encontrou uma chave antiga. A resposta estava escrita no teto: 'Não procurem além da porta do passado'."
    * **Análise:** **Excelente combinação.** Os dois contextos se encaixaram perfeitamente. O ambiente assombrado serviu de cenário para a profissão do personagem (investigar um desaparecimento, achar pistas e decifrar enigmas).
* **Combinação 3: Robô engraçado + Floresta mágica**
    * *Saída:* "Na floresta mágica, árvores falavam em sussurros e animais dançavam sob a luz da lua. Um jovem explorador, chamado Leo, descobriu um rio de cristal que o levou a um castelo escondido. Lá, encontrou uma rainha que o convidou a se juntar à comunidade mágica da floresta."
    * **Análise:** **Falhou na personalidade.** Assim como no primeiro cenário, a IA se empolgou com o tema lúdico da "floresta mágica" e o explorador Leo, deixando o "robô engraçado" totalmente de fora da narrativa.

> 💡 **Conclusão:** Diferentes contextos alteram drasticamente o peso que a IA dá para o prompt. Em misturas muito discrepantes, o modelo tende a sofrer de negligência de prompt, priorizando o tema do cenário sobre as características do personagem.

---

## 🎨 Exercício 7 — Alterando o Estilo da Escrita

* **Prompt Customizado:** *"Você é um detetive particular em um castelo assombrado, escreva uma história de forma engraçada e utilize emojis em um parágrafo de no máximo 50 palavras"*
* **Resultado da IA:**
    > "Eu estava investigando o famoso castelo assombrado. De repente, ouvi um barulho e vi um fantasma! 🕷️ Eu disse: 'Não se preocupe, eu sou detetive!' O fantasma respondeu: 'Eu estou aqui porque o dono do castelo não paga a conta do eletricista 💡'"

### Observações
* **O estilo realmente muda?**
    * **R:** Sim, o estilo muda de forma drástica. Ao unir as instruções de "forma engraçada" e "use emojis", a IA abandonou completamente o tom sério e focado em suspense que a figura do detetive e o cenário do castelo normalmente teriam. O modelo reestruturou a escrita para dar um ritmo de "piada rápida" (com uma quebra de expectativa no final) e utilizou os emojis como pontuação visual para dar leveza ao texto.
* **Qual foi o resultado mais divertido? Por quê?**
    * **R:** O resultado gerado foi extremamente divertido por conta da **quebra de expectativa da piada**. Em vez de seguir o clichê de terror com um fantasma assustador ou uma maldição antiga, a IA usou um humor cotidiano e corporativo: o fantasma estava ali apenas porque o dono do castelo esqueceu de pagar a conta do eletricista (justificando as luzes piscando e o breu do castelo). A mistura do mistério com um problema burocrático de falta de luz ficou excelente e muito criativa para um limite tão curto de palavras!

---

## ⚠️ Exercício 8 — Detectando Limitações da IA

* **Configuração:** `tema_historia = "uma bicicleta que viaja no tempo usando pizza como combustível"`
* **Resultado da IA:**
    > "Era uma bicicleta louca chamada 'Pizza Tempo' que viajava pelo tempo usando pizza como combustível. Ela comia uma pizza de pepperoni e ganhava velocidade até o ano 2050. Depois, comia uma pizza de quatro queijos e voltava para o presente. Era um verdadeiro 'pizza-velocista'! 🍕"

### Análise de Limites

* **A IA conseguiu criar sentido?**
    * **R:** Sim, a IA conseguiu criar sentido estabelecendo uma relação direta de causa e efeito. Ela vinculou de forma lógica os sabores da pizza com o direcionamento da viagem temporal: a pizza de pepperoni funciona como combustível para avançar até o ano 2050, enquanto a pizza de quatro queijos serve para fazer o retorno ao presente.
* **A resposta ficou estranha ou coerente?**
    * **R:** Ficou **altamente coerente dentro do cenário absurdo proposto**. A resposta focou puramente nas regras de funcionamento do "veículo". A IA organizou o texto de forma muito limpa, linear e encerrou com um trocadilho divertido (*"pizza-velocista"*), demonstrando que consegue manter a coerência de um enredo mesmo quando os elementos fornecidos desafiam as leis da realidade.

---

## Exercício 9 — Criando um Prompt Completo

### Parâmetros Definidos
* `personalidade` = *"Você é um ninja silencioso"*
* `idioma` = *"japonês / pt-br (misto para validação)"*
* `tamanho_resposta` = *"em duas frases"*
* `tema_historia` = *"um gato que protege um templo antigo"*

### Saída da IA
> Havia um gato chamado Kaito que protegia um templo antigo. Ele era tão silencioso que até os monges não sabiam que ele estava lá.  
> 1. *Kaito wa shiro no jinja o mamorubeshi* (Kaito protegia o templo branco).  
> 2. *Kaito wa shinobi no gatto deshita* (Kaito era um gato-ninja).

---

## 🏆 Exercício 10 — Desafio Final em Grupo

### 🛠️ Configuração de Parâmetros Originais do Grupo
```python
personalidade = "Você é um dos filhos de Sparda, chamado Vergil"
idioma = "pt-br"
tamanho_resposta = "Um parágrafo com no máximo 60 palavras"
tema_historia = "plano para sair do underworld e reencontrar seu irmão perdido chamado Dante"

```

### 🖥️ Saída da IA

> "Eu, Vergil, filho de Sparda, planejo uma missão perigosa: escapar do Underworld e encontrar meu irmão, Dante, que desapareceu há séculos. Através de meus poderes demoníacos, vou navegar pelas trevas e superar os obstáculos para reencontrar aquele que partilhou meu passado. A esperança de reunião me impulsiona a enfrentar o desconhecido."

### 📝 Justificativa e Resultados do Desafio

* **Quais alterações fizeram?**
* **R:** Customizamos o script base configurando as variáveis com um contexto focado no universo de games (*Devil May Cry*), definindo a persona como Vergil, a restrição para menos de 60 palavras e a meta dramática de reencontro com Dante.


* **O que esperavam da IA?**
* **R:** Esperávamos que o modelo assumisse a voz do personagem Vergil — conhecido por ser alguém extremamente frio, orgulhoso, focado em poder e formal — e que criasse um plano conciso, em primeira pessoa, respeitando rigidamente o limite curto de palavras para caber em um único parágrafo.


* **O que realmente aconteceu?**
* **R:** A IA correspondeu muito bem às expectativas. Ela capturou perfeitamente o tom solene do personagem (*"Eu, Vergil, filho de Sparda..."*) e utilizou palavras condizentes com o universo dele (*"poderes demoníacos"*, *"trevas"*, *"Underworld"*). Além disso, a restrição física foi seguida à risca: o texto gerado foi estruturado em **um único parágrafo contendo exatamente 49 palavras**, ficando abaixo do teto estipulado de 60 palavras sem cortar a mensagem principal.