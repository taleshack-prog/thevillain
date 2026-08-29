HACK TECH FARM

**O VILÃO — PRD ****&**** GDD ATUALIZADOS (REVISÃO 2.0 — PIVÔ PARA ENIGMAS)**

*Documento consolidado com as inovações de core loop e arquitetura de enigmas lógicos*

29 de agosto de 2026

## CONTEXTO E PREMISSA ESTRATÉGICA

O projeto **O Vilão** passou por um pivô estratégico e estrutural de game design e engenharia de produto. O core loop original, fundamentado em um construtor manual de armadilhas em grid ortogonal bidimensional (4x5) com blocos mecânicos (serra, fogo, gelo, mola e laser), revelou-se insuficiente para sustentar a tese de retenção e viralização orgânica do produto. A fricção cognitiva e motora na criação de armadilhas manuais gerava conteúdos de baixa qualidade média por parte do usuário (User-Generated Content - UGC), demandava tempo excessivo de autoria e entregava baixo valor de autoexpressão intelectual ou *status-signal* social aos jogadores.

A nova premissa central redefine a experiência: a transição de **construtor de armadilhas** para **curador e orquestrador de enigmas**. O Vilão não desenha obstáculos mecânicos em uma matriz espacial; ele seleciona temas inteligentes, orienta a geração algorítmica e personaliza a provocação social. Por sua vez, o Herói não navega espacialmente por células perigosas, mas decifra mistérios intelectuais, charadas lógicas, deduções analíticas e enigmas estruturados sob pressão de tempo e penalidades de precisão.

Mantém-se intocável a tese de distribuição do produto: *"**O convite é o jogo**"*. O motor de crescimento do produto apoia-se inteiramente no coeficiente de viralidade (*K-factor*), no qual o compartilhamento de um enigma resolvido ou de um desafio pendente opera como a própria peça jogável e o canal de aquisição de novos usuários.

"O novo core loop substitui a manipulação de blocos físicos pela esgrima mental entre mentes. O Vilão escolhe a armadilha do pensamento; a Inteligência Artificial modela o calabouço lógico; o Herói arrisca sua reputação para escapar."

## PARTE 1 — PRODUCT REQUIREMENTS DOCUMENT (PRD) ATUALIZADO

### 1.1 Objetivo do Produto

O objetivo primário do produto **O Vilão** é estabelecer um ecossistema social assíncrono de desafios lógicos, no qual o valor percebido reside na sofisticação intelectual e no embate de astúcia entre pares. O aplicativo posiciona-se na interseção entre micro-jogos de raciocínio lógico, desafios de dedução e plataformas de autoexpressão competitiva.

O produto viabiliza que qualquer usuário assuma o papel do Vilão em menos de trinta segundos, escolhendo temas curados e ativando a geração por Inteligência Artificial (IA) de cenários imersivos, charadas elegantes, trilhas de passos lógicos e pistas codificadas. Para o Herói destinatário, o produto fornece uma experiência curta, focada e intensa de decifração (1 a 3 minutos por sessão), na qual o consumo de pistas reduz a pontuação e os erros incorrem em penalidades severas, culminando em relatórios comparativos de astúcia e oportunidades imediatas de revanche.

### 1.2 Público-Alvo e Personas

A definição do público-alvo reflete a sofisticação do pivô, estruturando quatro personas complementares distribuídas entre a fase inicial e as expansões planejadas do ciclo de vida do jogo:

- **Persona 1 — O Curador (O Vilão / Fase 1):** Jogador competitivo e socialmente expressivo (20 a 35 anos). Não deseja perder dez minutos posicionando blocos em telas pequenas; busca impactar amigos com provocações cultas, desafios elegantes e cartas de convite compartilháveis no WhatsApp e Instagram. Motivado pelo orgulho de ver adversários falharem em suas escolhas temáticas.

- **Persona 2 — O Decifrador (O Herói / Fase 1):** Entusiasta de quebra-cabeças lógicos, jogos de tabuleiro, palavras cruzadas e enigmas (18 a 45 anos). Joga em intervalos curtos de rotina diária (transporte, pausas de trabalho). Motivado pela satisfação intrínseca da resolução dedutiva rápida, pela conquista do "Bônus de Gênio" (acerto sem uso de pistas) e pela superação de tempos de resposta no ranking de sua coorte.

- **Persona 3 — O Detetive (Modo Solo e Diário / Fase 2):** Jogador analítico focado em sequências diárias (*streaks*) de casos não resolvidos. Valoriza narrativas de dedução lógica e restrições formais com solução única e verificável matematicamente.

- **Persona 4 — O Intelectual Erudito (Tier Filosófico / Fase Premium):** Estudante universitário, acadêmico ou leitor assíduo de filosofia, literatura clássica e história das ideias (22 a 55 anos). Busca desafios de alta densidade conceitual envolvendo escolas de pensamento (Estoicismo, Racionalismo, Existencialismo) e pensadores canônicos, disposto a assinar o escalão premium para acessar o repertório erudito.

### 1.3 Escopo do MVP (In/Out Atualizado)

O escopo do MVP (Fase 1) foi rigorosamente delimitado para validar a tração do novo core loop sem desperdício de esforço em engenharia periférica:

Escopo Incluído (IN — Fase 1):

- Seleção de temas a partir de um catálogo pré-gerado e rotativo abastecido por IA;

- Geração algorítmica de cenários imersivos, charadas lógicas, trilhas de dedução em 2 a 4 passos e 3 pistas progressivas;

- Validação simbólica determinística no backend garantindo unicidade de solução e ausência de vazamento antecipado de respostas nas pistas;

- Mecanismo de trajetória de decifração do Herói com penalidade de tempo, precisão e consumo de pistas;

- Geração de Cartas de Convite compartilháveis com deep link e provocação contextual do Vilão;

- Sistema de ranking por coortes semanais com latência inferior a 300 milissegundos;

- Infraestrutura própria conteinerizada em PostgreSQL 16 puro, sem qualquer dependência de plataformas proprietárias do tipo Backend-as-a-Service (zero-Supabase).

Escopo Excluído (OUT — Adiado para Fases Posteriores):

- Tier Filosófico avançado e vertentes doutrinárias complexas (postergado para a Fase Premium);

- Guildas, ligas colaborativas e temas em equipes (Fase 3);

- Modo Detetive com geração procedural de casos criminais completos (Fase 2);

- Editores manuais de texto livre de enigmas por parte do usuário comum (evita moderação pesada e quebra de unicidade lógica no MVP);

- Transações monetárias pay-to-win ou compra de vantagens mecânicas no ranking.

### 1.4 Requisitos Funcionais (FR)

| **ID** | **Módulo** | **Descrição Funcional do Requisito** | **Prioridade** |
| --- | --- | --- | --- |
| **FR-001** | Curadoria | O sistema deve apresentar ao Vilão uma lista de temas de enigmas categorizados, renovada periodicamente via job assíncrono. | P0 |
| **FR-002** | Geração IA | O backend deve gerar, via modelo de linguagem leve (SLM), cenário contextual, charada lógica, trilha de 2 a 4 passos e 3 pistas progressivas com base no tema escolhido. | P0 |
| **FR-003** | Validação | O validador determinístico deve comprovar a existência de exatamente uma resposta correta e verificar que nenhuma pista revela prematuramente a resposta final. | P0 |
| **FR-004** | Distratores | O sistema deve produzir 3 a 5 opções de respostas falsas (distratores) que apresentem plausibilidade lógica para o Herói. | P0 |
| **FR-005** | Convites | O sistema deve gerar uma Carta de Convite gráfica com deep link exclusivo (o_vilao://challenge/{token}) e provocação gerada por IA. | P0 |
| **FR-006** | Trajetória | A interface do Herói deve processar a resolução passo a passo, registrando o estado de cada etapa da trilha de dedução. | P0 |
| **FR-007** | Pistas | O Herói pode solicitar até 3 pistas por enigma; cada pista reduz a precisão final e aplica penalidade na pontuação global da sessão. | P0 |
| **FR-008** | Temporizador | A sessão de decifração deve impor um cronômetro regressivo de 1 a 3 minutos; o esgotamento resulta em derrota imediata. | P0 |
| **FR-009** | Revanche | Ao término da partida, o Herói pode disparar uma revanche imediata, invertendo os papéis ou contra-atacando na mesma coorte. | P0 |
| **FR-010** | Ranking | O sistema deve computar e exibir rankings competitivos segmentados por coortes (país, plataforma, semana), com resposta < 300 ms. | P0 |
| **FR-011** | Telemetria | O sistema deve registrar eventos granulares de funil (abertura, uso de pistas, erros, vitórias, compartilhamentos) com separação estrita de PII (LGPD). | P0 |
| **FR-012** | Pool Rotativo | Um processo batch em Celery deve gerar e validar previamente novos modelos de enigmas mantendo um buffer ativo no banco de dados. | P1 |
| **FR-013** | Bônus Gênio | O motor de pontuação deve atribuir multiplicador extra de 1.5x aos jogadores que decifrarem sem acionar nenhuma pista. | P1 |
| **FR-014** | Monetização | O sistema deve controlar acesso a temas adicionais via rewarded ads voluntários e compras in-app de pacotes de temas sem alterar equilíbrio competitivo. | P1 |
| **FR-015** | Modo Detetive | Mecanismo de enigma diário procedural acessível a todos os usuários globalmente com ranking consolidado de sequência de vitórias. | P2 |
| **FR-016** | Tier Filosófico | Base de conhecimento com citações e conceitos canônicos eruditos curados para o escalão premium com validação em duas camadas. | P2 |

### 1.5 Requisitos Não-Funcionais (NFR)

- **NFR-001 (Latência de Ranking e APIs):** Consultas de leaderboard e validação de tokens de desafio devem retornar tempo de resposta $P95 < 250\text{ ms}$ e $P99 < 500\text{ ms}$.

- **NFR-002 (Custo Marginal de IA Próximo a Zero):** O pipeline de IA deve utilizar Small Language Models (SLMs de 3B parâmetros) executados em instâncias locais ou serverless dedicadas, complementados por caching agressivo em Redis e validações simbólicas determinísticas prévias, mantendo o custo de geração abaixo de R$ 0,001 por enigma.

- **NFR-003 (Arquitetura de Dados Zero-Supabase):** O sistema deve operar estritamente em PostgreSQL 16 padrão sobre infraestrutura conteinerizada (Docker Compose / Kubernetes), utilizando SQLAlchemy 2.0 assíncrono e migrações controladas por Alembic. É vetada a utilização de Supabase Auth, Supabase Realtime, Supabase Storage ou extensões acopladas a serviços proprietários.

- **NFR-004 (Privacidade e LGPD):** Separação arquitetural mandatória entre Informações Pessoais Identificáveis (PII) e dados de telemetria/analíticos. Os dados sensíveis devem residir no schema isolado pii_data com criptografia colunar via extensão pgcrypto.

- **NFR-005 (Disponibilidade e Concorrência):** O backend deve suportar no mínimo 1.500 requisições simultâneas por segundo com taxa de erro menor que 0,01%, mantendo integridade transacional de resultados via locks otimistas e workers Celery assíncronos.

### 1.6 Métricas e Gates de Lançamento

A passagem entre as etapas de desenvolvimento e o investimento continuado obedecem aos seguintes critérios quantitativos auditados pela telemetria:

- **North Star Metric:** Desafios Aceitos por Dia (*Accepted Challenges per Day - ACD*).

- **Gate de Retenção D1:** $\ge 25%$ dos novos jogadores retornando no dia seguinte.

- **Gate de Retenção D7:** $\ge 9%$ de retenção ativa no sétimo dia pós-instalação.

- **Gate de Retenção D30:** $\ge 3%$ de retenção consolidada no trigésimo dia.

- **Taxa de Conclusão de Enigmas:** $\ge 60%$ das sessões iniciadas devem ser levadas até a conclusão (vitória ou derrota).

- **Coeficiente Viral (K-factor):** $\ge 15%$ ($K \ge 0,15$), medido pela proporção entre convites gerados e convertidos em novos jogadores ativos.

- **Métrica de Qualidade do Design:** Taxa de "Bônus de Gênio" (resoluções perfeitas sem pistas) estabilizada entre $15%$ e $25%$ do total de conclusões bem-sucedidas, atestando calibragem ideal de dificuldade.

### 1.7 Critérios de Lançamento (Definition of Done)

O lançamento do MVP da Fase 1 exige conformidade com os seguintes parâmetros técnicos e operacionais:

- Conjunto de 500 modelos de enigmas lógicos previamente gerados, validados por prova matemática de unicidade e indexados no banco de dados;

- Tempo médio de geração e resposta do backend inferior a 800 milissegundos para novas solicitações;

- Cobertura de testes automatizados superior a 85% nos módulos de validação simbólica, cálculo de pontuação e rotas de segurança;

- Zero dependências externas de serviços BaaS proprietários;

- Dashboard de telemetria operacional com atualização em tempo real dos gates D1, D7, K-factor e funil de desafios.

## PARTE 2 — GAME DESIGN DOCUMENT (GDD) ATUALIZADO

### 2.1 Visão Geral

**O Vilão** é um jogo social assíncrono em plataforma mobile e web de duelos dedutivos. Em vez de confrontos de reflexos mecânicos ou posicionamento de obstáculos espaciais, o título foca na manipulação de dilemas lógicos, pistas fragmentadas e pressão psicológica sob a temática *Dark Fantasy Chiaroscuro*. O Vilão atua como o arquiteto do dilema e o Herói como o decifrador sob o olhar provocador do adversário.

### 2.2 Elevator Pitch

*"**Wordle encontra Sherlock Holmes através do teatro de um vilão refinado: desafie seus amigos com enigmas lógicos desenhados por inteligência artificial onde cada pista custa seu orgulho e cada erro alimenta a glória do seu rival.**"*

### 2.3 Core Loop Revisado

O fluxo de jogo abandona a construção manual de cenários e estabelece uma espiral de provocação contínua dividida em seis etapas:

[1. ESCOLHER TEMA] ──> [2. IA GERA ENIGMA] ──> [3. PROVOCAR & DESAFIAR]
         ▲                                                │
         │                                                ▼
[6. VINGAR / REVANCHE] <── [5. RESULTADO & RANKING] <── [4. DECIFRAR TRAJETÓRIA]

- **Escolher Tema:** O Vilão navega por uma lista temática pré-curada e renovada pela IA (ex.: *"**Criptografia dos Alquimistas**"*, *"**O Mistério dos Relógios Mortos**"*, *"**Paradoxos da Corte**"*);

- **IA Gera Enigma:** Em fração de segundo, o SLM estrutura um cenário narrativo curto, uma charada lógica de dedução rigorosa, 3 pistas graduadas e 4 respostas plausíveis (1 correta e 3 distratores);

- **Provocar e Desafiar:** O Vilão seleciona ou aprova a provocação gerada pela IA, gerando uma Carta de Convite personalizada com link direto e compartilhando-a via mensageiros ou redes sociais;

- **Decifrar Trajetória:** O Herói aceita o desafio, ingressa na sessão sob um cronômetro de 1 a 3 minutos, analisa o cenário e avança na trilha de passos, decidindo quando comprar pistas e arriscar a resposta;

- **Resultado e Ranking:** A sessão é concluída; o sistema calcula o tempo gasto, a precisão e as deduções de pistas, gerando a ficha de performance que atualiza a posição dos jogadores na coorte semanal;

- **Vingar / Revanche:** O Herói derrotado recebe a provocação final do Vilão e o botão imediato de contra-ataque, invertendo os papéis e iniciando um novo ciclo com um enigma de tema antagônico.

### 2.4 Mecânicas Centrais

Anatomia do Enigma (As 5 Camadas)

Cada enigma gerado no sistema possui rigorosamente cinco componentes interdependentes:

- **Camada 1 — Cenário:** Texto de ambientação imersiva com 2 a 3 frases, fornecendo o contexto narrativo e as premissas lógicas fundamentais;

- **Camada 2 — Charada (Enigma Central):** A proposição formal do problema, estruturada para permitir deduções lógicas estritas e garantir solução matematicamente única;

- **Camada 3 — Trilha de Dedução:** Sequência linear de 2 a 4 premissas encadeadas que conduzem necessariamente à conclusão verdadeira;

- **Camada 4 — Pistas Progressivas:** Três dicas escalonadas. A Pista 1 fornece orientação contextual (elimina incerteza ampla); a Pista 2 quebra uma das hipóteses falsas; a Pista 3 revela a penúltima conexão da trilha de dedução sem dizer a resposta explícita;

- **Camada 5 — Resposta e Distratores:** Uma resposta correta inquestionável e três alternativas falsas construídas com base em armadilhas lógicas comuns (falácia formal, interpretação literal inadequada ou erro de cálculo).

Trajetória de Sucesso e Fracasso

O avanço do Herói na resolução é modelado por um sistema de pontuação dinâmica baseado na seguinte formulação:

$$\text{Pontuação Base} = 1000 \times \mathbb{I}(\text{vitória})$$

$$\text{Penalidade de Tempo} = \max\left(0, \frac{\text{Tempo Limite} - \text{Tempo Gasto}}{\text{Tempo Limite}}\right) \times 300$$

$$\text{Penalidade de Pistas} = \text{Número de Pistas Usadas} \times 150$$

$$\text{Penalidade de Tentativas Incorretas} = \text{Erros Cometidos} \times 200$$

$$\text{Pontuação Final} = \max\left(0, \text{Pontuação Base} + \text{Penalidade de Tempo} - \text{Penalidade de Pistas} - \text{Penalidade de Tentativas Incorretas}\right)$$

$$\text{Se Pistas} = 0 \text{ e Vitória} = 1 \implies \text{Pontuação Final} = \text{Pontuação Final} \times 1.5 \quad (\text{Bônus de Gênio})$$

O cometimento de um erro antes do término do tempo não finaliza o jogo; aplica a dedução de precisão e devolve o Herói à análise com o cronômetro em execução, estimulando a recuperação sob tensão.

Tipos de Enigmas na Fase 1

- **Charada Clássica:** Jogos de definição precisa e duplo sentido elegante, nos quais uma propriedade singular identifica o objeto/conceito sem ambiguidades;

- **Enigma Lógico-Dedutivo:** Restrições cruzadas entre entidades (ex.: ordem de chegada, posse de chaves, veracidade de declarações);

- **Enigma Numérico-Sequencial:** Relações de proporcionalidade, balanço de pesos ou padrões aritméticos disfarçados em contexto narrativo medieval/fantástico;

- **Enigma de Palavras e Criptografia Leve:** Anagramas contextuais, cifras de substituição simples e decodificação de inscrições rúnicas.

### 2.5 Pipeline de IA de Custo Marginal Zero

Para garantir viabilidade operacional sem dependência de APIs com precificação proibitiva por token, o pipeline do Vilão opera em cinco estágios automatizados:

[1. Gerador SLM] ──> [2. Validador Simbólico] ──> [3. Validador de Pistas]
                            │ (Se reprovado: descarte)       │
                            ▼                                ▼
                     [5. Rotação Batch] <─── [4. Calibrador de Dificuldade]

- **Gerador de Enigmas (SLM Local):** Modelos compactos (Llama 3.2 3B / Mistral NeMo 3B) executados via Ollama local ou instâncias dedicadas. O prompt estruturado exige a saída em formato JSON estrito contendo cenário, charada, passos, pistas e distratores;

- **Validador Simbólico Determinístico:** Algoritmo em Python que realiza a checagem formal do grafo de restrições do enigma. Se houver mais de uma solução possível ou se o grafo apresentar contradição interna, o enigma é sumariamente descartado antes de alcançar o banco de dados;

- **Validador de Pistas:** Checagem algorítmica de vazamento de informação por análise semântica e correspondência de padrões, assegurando que o texto das pistas 1 e 2 não contenha a cadeia de caracteres da resposta final nem reduza as opções a menos de duas;

- **Calibrador de Dificuldade (Playtester IA):** O SLM simula 30 a 50 execuções com temperatura $\tau = 0.7$, simulando variabilidade humana de raciocínio. A taxa de sucesso dos agentes sintéticos define o índice de dificuldade $D \in [0.0, 1.0]$;

- **Rotação Batch Diária:** Workers Celery executam durante a madrugada para gerar um buffer de 200 a 500 novos enigmas validados por tema, gravando no PostgreSQL e liberando instâncias para consumo em cache no Redis durante os horários de pico.

### 2.6 Monetização Premium-First

A economia do jogo rejeita modelos invasivos ou pay-to-win, estruturando-se em quatro pilares comerciais:

- **Acesso Gratuito Pleno:** Todos os jogadores têm direito ao enigma do dia, aos desafios recebidos de amigos e à criação diária de até 3 novos desafios gratuitamente sem interrupção de anúncios obrigatórios;

- **Compra Única (Pacotes de Temas / Temporadas):** Venda avulsa de cadernos temáticos de enigmas (ex.: *"**Mistérios da Inquisição**"*, *"**Criptas de Alexandria**"*) por valores entre R$ 9,90 e R$ 19,90;

- **Assinatura Mensal (Clube do Vilão / R$ 14,90/mês):** Desbloqueia criação ilimitada de convites, insígnias de perfil, cosméticos para as Cartas de Convite, relatórios analíticos avançados de astúcia e acesso antecipado ao Modo Detetive;

- **Rewarded Ads Estritamente Voluntários:** Possibilidade de assistir a um anúncio em vídeo para desbloquear um desafio extra no dia ou recuperar uma chave temática, sem qualquer influência em pontuações de ranking competitivo.

### 2.7 KPIs e Gates do Game Design

O monitoramento de design apoia-se em indicadores de equilíbrio:

- **Taxa de Conclusão por Faixa de Dificuldade:** Enigmas fáceis ($D < 0.3$) devem apresentar taxa de sucesso de $75% \text{ a } 85%$; médios ($0.3 \le D \le 0.7$) entre $50% \text{ a } 65%$; difíceis ($D > 0.7$) entre $20% \text{ a } 35%$;

- **Tempo Médio de Sessão:** Estabilizado entre 90 e 150 segundos;

- **Índice de Revanche Imediata:** Meta de $\ge 22%$ dos Heróis derrotados emitindo um novo convite dentro de 5 minutos após o resultado;

- **Taxa de Compartilhamento da Carta de Convite:** $\ge 35%$ dos desafios criados sendo compartilhados com sucesso para aplicativos externos de mensageria.

### 2.8 Plataforma e Arquitetura Técnica (Zero-Supabase)

A infraestrutura técnica opera com separação de responsabilidades em stack moderna e de baixo custo operacional:

┌┐
│              FRONTEND (Next.js 14 / React Native)           │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTPS / WSS
┌──────────────────────────────▼──────────────────────────────┐
│                  BACKEND (FastAPI / Python)                 │
│  ┌───────────────┐ ┌───────────────────┐ ┌───────────────┐  │
│  │  Auth & JWT   │ │  Enigma Engine    │ │ WebSocket Hub │  │
│  └───────────────┘ └───────────────────┘ └───────────────┘  │
│  ┌┐  │
│  │      Services Layer: Validator | Solver | Telemetry   │  │
│  └┘  │
└──────┬───────────────────────┬───────────────────────┬──────┘
       │                       │                       │
┌──────▼──────┐         ┌──────▼──────┐         ┌──────▼──────┐
│ PostgreSQL  │         │    Redis    │         │   Celery    │
│     16      │         │ 7 (Cache /  │         │ (Batch IA & │
│ (pgcrypto / │         │   PubSub)   │         │ Telemetria) │
│   JSONB)    │         └─────────────┘         └──────┬──────┘
└─────────────┘                                        │
                                                ┌──────▼──────┐
                                                │   Ollama    │
                                                │ (Llama 3.2) │
                                                └─────────────┘

Novas Entidades do Schema Relacional:

O modelo relacional do PostgreSQL incorpora as entidades necessárias para o suporte ao novo ciclo de enigmas:

- riddle_themes: Tabela de categorias temáticas com colunas id, slug, nome, descricao, icone, is_premium, created_at;

- riddle_templates: Armazena o enigma completo validado com colunas id, id_tema (FK), cenario (TEXT), charada (TEXT), resposta_correta (TEXT), distratores (JSONB), trilha_deducao (JSONB), dificuldade_estimada (FLOAT), hash_solucao (VARCHAR 64), status (ENUM: draft, active, archived), rotacao_data (DATE);

- clues: As três pistas atreladas ao template com id, id_template (FK), ordem (INT: 1 a 3), texto (TEXT), penalidade_pontos (INT);

- riddle_attempts: Registro detalhado da execução do Herói contendo id, id_desafio (FK), id_heroi (FK), tempo_ms (INT), pistas_consumidas (INT), erros_cometidos (INT), respostas_tentadas (JSONB), vitoria (BOOLEAN), precisao (FLOAT), created_at (TIMESTAMPTZ);

- challenges, results, ranking_entries, telemetry_events: Preservados e desacoplados, apontando para as novas entidades de enigma.

### 2.9 Roadmap Atualizado

| **Fase** | **Nome / Marcos** | **Entregáveis de Design e Engenharia** | **Critério de Saída (Gate)** |
| --- | --- | --- | --- |
| **Fase 0** | Protótipo Web | Web app com 5 charadas lógicas curadas autorais, sem IA no runtime, 3 temas básicos, links de desafio compartilháveis e cronômetro simples. | Validação de interesse com 100 usuários de teste; conclusão > 70%. |
| **Fase 1** | MVP Enigmas IA | Geração de enigmas por SLM em batch, validação determinística, 3 pistas graduadas, trajetória de resposta, ranking de coortes, zero-Supabase. | D1 ≥ 25%, D7 ≥ 9%, K-factor ≥ 15%, 5.000 desafios aceitos. |
| **Fase 2** | Modo Detetive | Enigma diário procedural global, mecânica de streaks de dedução, expansão da biblioteca de distratores, compartilhamento de cards dinâmicos. | D30 ≥ 3%, retenção de streaks diários ≥ 40% em D14. |
| **Fase 3** | Escala & Guildas | Temas colaborativos em equipe, ligas universitárias/regionais, sistema de recompensas cosméticas do Vilão, integração de eventos sazonais. | 100k MAU, K-factor ≥ 25% sustentado por 3 meses. |
| **Fase Filosófica** | Escalão Premium | Tier Filosófico completo com repertório erudito (Platão, Sêneca, Kant, Nietzsche), curadoria em 2 camadas (IA + Tales), conversão de receita via assinatura. | Taxa de conversão para assinatura ≥ 4.5% da base ativa; MRR ≥ R$ 50.000. |

### 2.10 Tier Filosófico (Escalão Premium)

O Tier Filosófico constitui a experiência topo de funil para monetização e engajamento erudito. Diferente das charadas lógicas gerais do MVP, o conteúdo filosófico exige rigor conceitual absoluto e resolução objetiva, eliminando subjetividades hermenêuticas na atribuição de pontos:

- **Vertentes Contempladas:** Estoicismo Romano, Racionalismo Cartesiano, Empirismo Britânico, Iluminismo e Ética Deontológica Kantiana, Existencialismo, Teoria Política Clássica e Niilismo/Crítica da Moral;

- **Repertório de Pensadores:** Citações textuais estritas de autores em domínio público (Platão, Aristóteles, Sêneca, Marco Aurélio, Espinosa, Descartes, Kant, Nietzsche, Dostoiévski, Victor Hugo). Autores com direitos patrimoniais vigentes (Yuval Noah Harari, Mario Vargas Llosa) são abordados exclusivamente por meio de *referências conceituais* e problematizações estruturadas sem reprodução literal de trechos protegidos;

- **Processo de Curadoria Editorial em 2 Camadas:***Camada Algorítmica:* O SLM monta a proposta de enigma unindo citação textual autêntica, definição técnica de conceito canônico e três distratores formalmente falsos mas historicamente relevantes;

- *Camada de Curadoria Humana (Tales / Curador-Chefe):* Aprovação editorial individual no painel administrativo antes da publicação no banco de produção. Nenhum enigma filosófico entra no catálogo premium sem chancela humana.

### 2.11 Identidade Visual e Estética

A direção de arte apoia-se no conceito **Dark Fantasy Chiaroscuro**, combinando atmosfera gótica refinada, iluminação dramática inspirada em pinturas a óleo barrocas e acabamento de interface digital moderno:

- **Paleta de Cores:***Carvão Profundo (#1A1A1A):* Cor de fundo principal de todas as interfaces;

- *Carvão Escuro (#121212):* Fundo de cards, grids e áreas elevadas;

- *Carvão Médio (#2A2A2A):* Botões secundários e divisores de seção;

- *Dourado Primário (#D4AF37):* Acentos principais, botões de ação primária, coroas de ranking e bordas ativas;

- *Dourado Claro (#F0D98C):* Textos de destaque, títulos secundários e ícones acesos;

- *Roxo Real (#6A3FA0):* Elementos de mistério, botões de pistas e identificação do Vilão;

- *Roxo Profundo (#3D1F6E):* Fundo de balões de fala do adversário e estados pressionados;

- *Texto Primário (#F5F5F5):* Leitura principal em alta legibilidade;

- *Texto Secundário (#9E9E9E):* Metadados, legendas e rótulos de status;

- *Sinalizadores:* Sucesso (#27AE60) e Erro/Alerta (#C0392B);

- **Tipografia Oficial:***Display e Títulos:***Cinzel** (serifada clássica, transmitindo autoridade e antiguidade);

- *Corpo de Texto e Interface:***Inter** (sem serifa, neutra, calibrada para telas móveis);

- *Cronômetros, Índices e Números:***Roboto Mono** (monoespaçada, garantindo estabilidade visual em contagens regressivas).

### 2.12 Design de Telas do Novo Fluxo

1. Tela do Curador (O Vilão — Criação do Desafio)

- **Cabeçalho:** Logotipo em Cinzel dourado, perfil do Vilão e contador de desafios ativos;

- **Carrossel de Temas:** Cards visuais ilustrados com moldura gótica representando temas (*"**Alquimia **&** Venenos**"*, *"**Paradoxos Temporais**"*, *"**Crimes na Abadia**"*);

- **Preview do Enigma Gerado:** Título temático, nível de dificuldade calibrado pela IA (1 a 10 caveiras) e prévia da provocação do adversário;

- **Botão de Ação Primária:** "FORJAR DESAFIO & PROVOCAR" (dourado sólido com glow suave).

2. Tela de Decifração (O Herói — Gameplay)

- **Barra Superior (HUD):** Cronômetro central em destaque (02:45), vidas restantes (❤️ ❤️ ❤️) e botão de acionamento de pistas (💡 PISTA (3));

- **Painel Central do Cenário:** Bloco escuro com textura de pergaminho antigo exibindo a ambientação e a charada central;

- **Trilha de Dedução Visual:** Linha de nós circulares interligados marcando os passos resolvidos (Passo 1 ✓ $\to$ Passo 2 $\to$ Conclusão);

- **Balão do Vilão (Overlay Lateral):** Retrato estilizado da silhueta do Vilão com olhos dourados brilhantes emitindo frases contextuais e reações animadas a cada ação do Herói;

- **Grelha de Respostas:** Quatro cards verticais clicáveis contendo as alternativas de resposta sob tipografia elegante e feedback imediato de seleção.

3. Card de Convite Compartilhável

- **Composição Gráfica:** Retrato vertical centralizado do Vilão em chiaroscuro ladeado por tochas;

- **Moldura Ornamental:** Cantos dourados clássicos com linhas duplas de contorno;

- **Área de Texto:** Nome do Desafiante, Nome do Enigma e a citação provocatória gerada pela IA;

- **Botões Inferiores:** "ACEITAR DESAFIO" (redirecionamento deep link) e linha de compartilhamento nativo para WhatsApp, Instagram Stories e Telegram.

4. Tela de Ranking e Coorte

- **Seletor de Período:** Abas Semana Atual, Diário e Melhores da Temporada;

- **Destaque do Líder:** Card superior com coroa dourada, moldura brilhante e métricas de velocidade e taxa de Bônus de Gênio;

- **Lista de Posições:** Listagem vertical com posição, avatar, nome do jogador, pontuação consolidada e botão de desafio direto.

## PARTE 3 — ANEXO: EXEMPLOS DE ENIGMAS F1

### Exemplo 1: O Relógio da Governanta

**Tema:** Mistérios da Mansão Vitoriana | **Categoria:** Enigma Lógico-Dedutivo | **Dificuldade Estimada:** 0.45 (Média)

**Cenário:** Na biblioteca da mansão de Blackwood, o pêndulo parou exatamente no instante do crime. A governanta jura que o relógio adianta 10 minutos a cada hora cheia. O mordomo afirma que ele foi acertado exatamente ao meio-dia. Agora, os ponteiros congelados marcam exatamente 15 horas e 30 minutos.

**Charada Central:** Considerando que o relógio funcionou continuamente desde o meio-dia até o momento do disparo sem ser violado, qual era a hora exata real em que o crime foi cometido?

- **Trilha de Dedução (3 Passos):***Passo 1:* Identificar a razão de velocidade do relógio. Se adianta 10 minutos a cada 60 minutos reais, ele percorre 70 minutos de mostrador para cada 60 minutos de tempo real (razão $7/6$);

- *Passo 2:* Calcular o tempo total decorrido no mostrador desde as 12:00 até as 15:30. O mostrador avançou 3 horas e 30 minutos, o que equivale a $210\text{ minutos}$ no relógio;

- *Passo 3:* Determinar o tempo real decorrido ($T_{\text{real}}$) aplicando a razão inversa: $T_{\text{real}} = 210 \times \left(\frac{6}{7}\right) = 30 \times 6 = 180\text{ minutos}$.

- **Pistas Progressivas:***Pista 1 (Contextual):* "O relógio corre mais rápido do que a realidade; portanto, o crime aconteceu antes das 15h30 reais."

- *Pista 2 (Operacional):* "Para cada 7 minutos que os ponteiros deste relógio avançam, apenas 6 minutos de vida real transcorreram."

- *Pista 3 (Conclusiva):* "Três horas e meia de mostrador correspondem a 210 minutos acelerados. Divida esse valor pela proporção correta."

- **Resposta Correta:****15 horas em ponto (15:00)**.

- **Distratores Plausíveis:***Distrator A:* 15 horas e 00 minutos (Correta);

- *Distrator B:* 14 horas e 55 minutos (Erro de dedução linear sem proporção);

- *Distrator C:* 15 horas e 15 minutos (Subtração ingênua de 10 minutos por hora);

- *Distrator D:* 15 horas e 20 minutos (Consideração de apenas meia hora de atraso).

### Exemplo 2: Os Três Baús de Alabastro

**Tema:** Criptas dos Cruzados | **Categoria:** Lógica Proposicional e Inscrições | **Dificuldade Estimada:** 0.60 (Média-Alta)

**Cenário:** Diante do túmulo do Grão-Mestre repousam três baús idênticos de alabastro: Ouro, Ferro e Ébano. Apenas um deles guarda a chave da cripta; os outros dois abrigam armadilhas de gás letal. Na tampa de cada baú há uma inscrição esculpida. O testamento do cavaleiro alerta: *'**No máximo uma das três inscrições diz a verdade; as outras são mentiras deliberadas.**'*

**Charada Central:** Analisando as inscrições abaixo, em qual dos baús está a chave da cripta?

• **Inscrição no Baú de Ouro:***"**A chave não está no baú de Ferro.**"*
• **Inscrição no Baú de Ferro:***"**A chave não está neste baú.**"*

• **Inscrição no Baú de Ébano:***"**A chave está neste baú.**"*

- **Trilha de Dedução (3 Passos):***Passo 1:* Analisar a regra mestra: existe **no máximo uma verdade** (pode haver zero ou uma verdade, ou seja, pelo menos duas inscrições são necessariamente falsas);

- *Passo 2:* Testar a hipótese de a chave estar no Baú de Ferro. Se a chave está no Ferro: Inscrição de Ouro é FALSA ("não está no ferro"); Inscrição de Ferro é FALSA ("não está neste baú"); Inscrição de Ébano é FALSA ("está neste baú"). Todas as três são falsas. Isso satisfaz a regra 'no máximo uma verdade' (0 verdades $\le 1$);

- *Passo 3:* Testar as outras posições para comprovar a unicidade. Se a chave estivesse no Ouro: Inscrição do Ouro seria VERDADEIRA e a do Ferro seria VERDADEIRA (duas verdades — viola a regra). Se a chave estivesse no Ébano: Inscrição do Ouro seria VERDADEIRA, a do Ferro seria VERDADEIRA e a do Ébano seria VERDADEIRA (três verdades — viola a regra). Portanto, a chave só pode estar no Ferro.

- **Pistas Progressivas:***Pista 1 (Contextual):* "Se duas inscrições concordarem em um cenário, esse cenário só será válido se ambas forem falsas."

- *Pista 2 (Operacional):* "Repare nas frases de Ouro e Ferro. Se a chave estiver no Ouro ou no Ébano, ambas as frases se tornam verdadeiras simultaneamente."

- *Pista 3 (Conclusiva):* "A única forma de não violar a regra de no máximo uma verdade é encontrar o local onde todas as três frases sejam mentirosas."

- **Resposta Correta:****Baú de Ferro**.

- **Distratores Plausíveis:***Distrator A:* Baú de Ouro (Suposição intuitiva tradicional);

- *Distrator B:* Baú de Ferro (Correta);

- *Distrator C:* Baú de Ébano (Interpretação literal da declaração afirmativa);

- *Distrator D:* Nenhum dos baús (Conclusão precipitada de inconsistência).

Documento elaborado em 29 de agosto de 2026. As informações são de responsabilidade da Hack Tech Farm.

**TALES**
Curador e Líder de Produto
Hack Tech Farm