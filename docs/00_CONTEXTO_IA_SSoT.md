Hack Tech Farm

**O VILÃO — DOCUMENTO DE CONTEXTO PARA IA: IDENTIDADE VISUAL, PRD, GDD E TDD**

*Contexto de Sistema e Diretriz Unificada de Produto, Design e Engenharia (Revisão 3.0)*

29 de agosto de 2026

## PARTE 0 — INSTRUÇÃO DE USO PARA A IA (COMO LER ESTE DOCUMENTO)

Este documento constitui a **Fonte Única de Verdade (Single Source of Truth — SSoT)** do projeto *O Vilão* e deve ser injetado como **Contexto de Sistema (System Prompt)** mandatório para qualquer modelo de inteligência artificial (Claude, GPT ou arquiteturas proprietárias) encarregado de gerar código, assets visuais, telas de interface, lógica de banco de dados, prompts de geração procedural ou balanceamento de game design.

**DIRETIVA PRIMÁRIA:** Nenhuma geração subsequente pode violar, flexibilizar ou descaracterizar os quatro pilares unificados neste arquivo. Qualquer ambiguidade na interpretação de solicitações do usuário deve ser arbitrada a favor das especificações literais deste documento.

A IA atuante deve operar sob as quatro obrigações mandatórias a seguir:

- **Adesão Estrita à Identidade Visual (Dark Fantasy Chiaroscuro):** Toda e qualquer menção a interfaces, componentes gráficos, telas ou renderizações 3D/2D deve respeitar a paleta exata (base carvão profunda, iluminação dramática barroca, Vilão em roxo elétrico e Herói em verde esmeralda). É terminantemente proibido o uso de tons pastéis, estética neon cyberpunk genérica (ciano/magenta) ou caricaturas infantilizadas.

- **Conformidade Funcional com o PRD (FR-001 a FR-016):** As jornadas do usuário, arquiteturas de informação e fluxos de criação e resolução de enigmas devem respeitar rigorosamente os requisitos funcionais e as restrições de escopo delimitadas para o MVP e fases subsequentes.

- **Fidelidade Mecânica e Narrativa ao GDD:** O core loop assíncrono de 6 etapas, o sistema de pontuação com Bônus de Gênio, o pipeline de validação de enigmas em 5 camadas e a economia *premium-first* não podem sofrer alterações sem aprovação explícita da liderança.

- **Alinhamento Arquitetural com o TDD:** O código gerado deve refletir o stack oficial (FastAPI, PostgreSQL 16 nativo com particionamento, Redis 7, Celery e modelos locais via Ollama), garantindo latência P95 inferior a 250ms, custo de inferência por enigma abaixo de R$ 0,001, segurança anti-cheat estrita e aderência integral à LGPD.

## PARTE 1 — IDENTIDADE VISUAL (DARK FANTASY CHIAROSCURO)

### 1.1. Manifesto Artístico

A direção visual de *O Vilão* estabelece um universo **Gótico-Futurista Chiaroscuro**. A estética funde a imponência sóbria da arquitetura gótica tradicional (arcos ogivais, abóbadas de nervura, vitrais monocromáticos e pedraria ancestral desgastada) com a sofisticação tecnológica de uma sociedade tecnomágica decadente (circuitos gravados a laser em metal negro, hologramas etéreos e condutores rúnicos de energia). A iluminação obedece ao princípio barroco do claro-escuro: feixes de luz rasantes e direcionais cortam sombras densas e impenetráveis, destacando silhuetas com *rim lights* de alto contraste. Toda composição deve obedecer à **Regra 60-30-10** de distribuição cromática: 60% de fundo em carvão profundo e superfícies tectônicas, 30% de elementos estruturais e sombras secundárias, e 10% de acentos luminescentes funcionais (roxo para o Vilão, verde para o Herói e dourado para prestígio/vitória).

### 1.2. Paleta de Cores Oficial

| **Nome do Token** | **Código HEX** | **Papel e Aplicação na Interface / Arte** |
| --- | --- | --- |
| Carvão Profundo | #1A1A1A | Fundo principal da aplicação, telas de carregamento e canvas base. |
| Carvão Escuro | #121212 | Superfícies de cards elevados, modais, gavetas e menus contextuais. |
| Carvão Médio | #2A2A2A | Linhas divisórias, bordas estruturais de containers e estados inativos. |
| Roxo Real | #6A3FA0 | Identidade do Vilão: cabeçalhos do Curador, bordas de cards e insígnias. |
| Roxo Profundo | #3D1F6E | Fundo de balões de fala do Vilão, banners de desafio e áreas de perigo. |
| Roxo Neon | #8B5CF6 | Circuitos ativos do Vilão, glow de botões de validação e rim light de arte. |
| Verde Esmeralda | #22C55E | Identidade do Herói: trilhas de dedução, botões de ação e HUD de fuga. |
| Verde Neon | #39FF14 | Runas ativas do Herói, confirmações de resposta correta e glow de vitória. |
| Dourado Primário | #D4AF37 | Prestígio, molduras do Tier Filosófico, coroas de ranking e CTAs principais. |
| Dourado Claro | #F0D98C | Títulos de alta hierarquia, destaques de tempo recorde e selos lendários. |
| Texto Primário | #F5F5F5 | Tipografia principal para máxima legibilidade sobre fundos escuros. |
| Texto Secundário | #9E9E9E | Metadados, rótulos de apoio, prazos, legendas e descrições secundárias. |
| Feedback Sucesso | #27AE60 | Indicadores de validação positiva e acerto sem penalidade. |
| Feedback Erro | #C0392B | Dano sofrido, perda de vidas no HUD e mensagens de falha crítica. |

**RESTRIÇÃO MANDATÓRIA:** É estritamente proibido o uso de tons Ciano (#00FFFF) ou Magenta (#FF00FF) fora do sistema de tokens. A saturação excessiva descaracteriza a atmosfera gótica e quebra a consistência do produto.

### 1.3. Tipografia e Hierarquia Visual

O sistema tipográfico é composto por três famílias com funções rígidas e intransferíveis:

- **Cinzel (Serifada / Display):** Utilizada exclusivamente em títulos de seção (H1 a H3), nomes de enigmas, marcas de prestígio e diálogos aristocráticos do Vilão. Transmite autoridade, erudição e monumentalidade gótica.

- **Inter (Sans-Serif / Corpo e UI):** Aplicada em todo o texto corrido, enunciados de desafios, opções de múltipla escolha, descrições de regras e botões de interface. Garante legibilidade técnica imediata em telas mobile de alta e baixa densidade de pixels.

- **Roboto Mono (Monospaçada / Dados e HUD):** Empregada em cronômetros, indicadores numéricos de vidas, pontuação calculada, telemetria de coorte, identificadores de transação e hashes de verificação.

### 1.4. Diretriz de Design dos Personagens

O VILÃO ("O Mestre da Armadilha" / Arquiteto do Dilema)

O Vilão é a personificação da astúcia intelectual e do poder aristocrático decadente. Sua indumentária consiste em uma jaqueta formal longa estilo sobretudo gótico, tecida em fibra negra fosca com finos circuitos integrados que emitem um brilho pulsante em Roxo Neon (#8B5CF6). Sob o sobretudo, veste um colete cinzento abotoado com acabamento milimétrico. Sua face é protegida por uma máscara cibernética poligonal e assimétrica com um visor vertical emissivo em roxo elétrico. O Vilão empunha um **Cajado-Tridente de Três Pontas**, construído em liga metálica escura contendo um cristal central que canaliza pulsos de energia roxa — este item é um prop independente e funcional. Em suas aparições magistrais, senta-se em um trono tecnológico com encosto alto e cantos pontiagudos. Apresenta 4 estados faciais/visuais: máscara cerimonial neutra, máscara com avarias de combate, semblante humano calculista e sorriso sarcástico aristocrático. Sua postura é régia, calculada e imponente, jamais caricata ou desajeitada.

O HERÓI ("O Fugitivo" / Decifrador Ágil)

O Herói representa a agilidade mental, a resiliência física e a juventude combativa. Apresenta-se como um arqueiro e patrulheiro tecnomágico com traços faciais jovens, olhar afiado e focado. Veste um capuz estruturado com caimento sobre uma capa longa em verde-escuro texturizado com física de tecido ativa. Seu peito é protegido por placas de couro reforçado e ombreiras articuladas, ostentando ao centro um broche/emblema circular celta que emite uma suave luminescência verde. Seus antebraços trazem braçadeiras mecânicas com runas esculpidas em Verde Neon (#39FF14). Como armamento principal, carrega um **Arco Composto Tecnorúnico** cuja corda é formada por um filamento de plasma estático, complementado por uma aljava dorsal com flechas de ponta cristalina. O Herói é renderizado em 4 poses de ação principais (mira tática, arrancada em fuga, agachamento analítico e esquiva acrobática) e 4 expressões (foco determinado, surpresa calculada, sorriso desafiador e triunfo contido).

### 1.5. Elementos de UI Derivados dos Personagens

A interface herda sua iconografia diretamente dos traços dos protagonistas. O **Broche Circular Celta** do Herói é reaproveitado como o ícone do indicador de vidas e medalha de conclusão. Os **Padrões Angulares do Cajado** do Vilão fornecem o desenho dos divisores de seção e ícones de validação do Curador. As **Runas Tecnomágicas** são utilizadas como marcadores visuais no progresso das etapas de dedução.

## PARTE 2 — PRD (PRODUCT REQUIREMENTS DOCUMENT)

### 2.1. Objetivo Estratégico do Produto

O objetivo central de *O Vilão* é validar a retenção de longo prazo e a propensão ao pagamento em um ecossistema de jogos sociais assíncronos baseados em duelos intelectuais e dedução lógica. O aplicativo inverte o paradigma dos jogos de trivia tradicionais: o criador (Vilão) atua como curador e arquiteto do dilema, enquanto o desafiado (Herói) precisa superar o desafio sob restrição de tempo, gerando um ciclo contínuo de provocação, vingança e viralidade orgânica.

### 2.2. Matriz de Personas

- **O Curador (Vilão Criador):** Jogador analítico e competitivo que obtém prazer em desafiar a inteligência de colegas, projetando armadilhas lógicas sofisticadas e monitorando as taxas de erro de seus amigos.

- **O Decifrador (Herói Fugitivo):** Jogador dinâmico, focado em alta performance mental, que busca resolver enigmas sob pressão de tempo para provar sua superioridade dedutiva e figurar no topo do ranking.

- **O Detetive (Explorador Narrativo — Fase 2):** Usuário motivado por histórias góticas imersivas, atmosferas de mistério criminal e deduções investigativas estruturadas em múltiplos atos.

- **O Intelectual Erudito (Assinante do Tier Filosófico):** Jogador sênior que busca debates éticos, paradoxos dialéticos clássicos (de Sócrates a Nietzsche) e conteúdo de alto calibre intelectual.

### 2.3. Escopo do MVP: Definição In / Out

- **IN (Escopo Confirmado do MVP):**
Motor de curadoria procedural de enigmas com 4 categorias lógicas.

- Geração e verificação de desafios via Large Language Models locais e regras determinísticas.

- Interface mobile responsiva completa (Curador, Decifrador, Card de Convite e Ranking de Coorte).

- Sistema de compartilhamento de deep links via WhatsApp, Telegram e Instagram Stories.

- Cálculo de pontuação com Bônus de Gênio e ranking normalizado por coortes temporais.

- Infraestrutura de telemetria e anonimização de dados em conformidade com a LGPD.

- **OUT (Postergado para Fases Subsequentes):**
Modo multijogador síncrono em tempo real (duelo tela dividida).

- Chat aberto entre jogadores (para evitar custos de moderação no MVP).

- Sistema de criação livre de assets gráficos pelos usuários (UGC visual irrestrito).

- Dublagem procedural por IA em áudio (mantendo apenas texto estilizado na v1.0).

### 2.4. Requisitos Funcionais do Sistema

| **ID** | **Requisito Funcional** | **Descrição Técnica da Funcionalidade** | **Prioridade** |
| --- | --- | --- | --- |
| FR-001 | Curadoria de Tema | Permitir ao Curador selecionar um tema gótico e nível de complexidade (1 a 5 caveiras). | P0 |
| FR-002 | Geração Procedural | Acionar o motor de inferência IA para criar enunciados, trilhas e distratores coesos. | P0 |
| FR-003 | Validação Simbólica | Garantir por testes determinísticos que o enigma possui solução única e inequívoca. | P0 |
| FR-004 | Geração de Distratores | Gerar exatamente 3 alternativas incorretas semanticamente plausíveis e 1 correta. | P0 |
| FR-005 | Geração de Convites | Criar cards visuais dinâmicos (9:16 e 1:1) com deep links encriptados de desafio. | P0 |
| FR-006 | Trilha de Dedução | Exibir passos lógicos sequenciais (2 a 4 nós) desbloqueados conforme raciocínio. | P0 |
| FR-007 | Pistas Progressivas | Disponibilizar até 3 pistas por enigma, aplicando penalidade progressiva na pontuação. | P0 |
| FR-008 | Temporizador Decrescente | Executar cronômetro local com validação no backend via timestamp de sessão inviolável. | P0 |
| FR-009 | Mecanismo de Revanche | Permitir que o Herói derrotado inverta o papel instantaneamente e desafie o Vilão. | P1 |
| FR-010 | Ranking por Coorte | Agrupar 30 jogadores simultâneos por safra temporal para comparação justa de score. | P1 |
| FR-011 | Pipeline de Telemetria | Registrar eventos de tempo de resolução, abandono, uso de pistas e compartilhamento. | P1 |
| FR-012 | Pool Rotativo Diário | Atualizar automaticamente o banco de desafios diários globais a cada 24 horas. | P1 |
| FR-013 | Cálculo de Bônus de Gênio | Multiplicar por 1.5x o score se resolvido em menos de 30% do tempo sem pistas. | P1 |
| FR-014 | Monetização e Passes | Processar compras in-app de temas cosméticos e assinaturas do Clube do Vilão. | P2 |
| FR-015 | Modo Investigativo Detetive | Desbloquear campanhas lineares com múltiplos nós de dedução narrativa interligados. | P2 |
| FR-016 | Tier Filosófico Curado | Disponibilizar acervo premium de debates éticos e dilemas clássicos de pensadores. | P2 |

### 2.5. Requisitos Não-Funcionais (NFR)

- **NFR-001 (Latência):** O tempo de resposta para validação de respostas e entrega de pistas deve apresentar P95 < 250ms sob carga nominal.

- **NFR-002 (Eficiência de Custos de IA):** O custo computacional de inferência por enigma gerado não pode exceder R$ 0,001, utilizando modelos SLM locais otimizados em INT4.

- **NFR-003 (Soberania de Dados):** Arquitetura 100% hospedada em instâncias dedicadas de PostgreSQL 16 nativo, rejeitando dependências proprietárias de BaaS como Supabase ou Firebase.

- **NFR-004 (Privacidade e LGPD):** Dados pessoais sensíveis e registros de endereço IP devem ser isolados em esquema segregado (pii_data) com encriptação AES-256 em repouso.

- **NFR-005 (Capacidade e Throughput):** O sistema deve sustentar vazão estável de 1.500 requisições simultâneas por segundo sem degradação do tempo de entrega de conteúdo.

### 2.6. Métricas Norte e Gates de Sucesso

- **Métrica North Star:***Desafios Aceitos por Dia (Accepted Challenges per Day — ACD)*.

- **Retenção:** D1 ≥ 25%, D7 ≥ 9%, D30 ≥ 3%.

- **Taxa de Conclusão de Enigmas:** ≥ 60% dos desafios iniciados levados até o veredito final.

- **Coeficiente Viral (K-Factor):** ≥ 15% dos jogadores que concluem um enigma geram ao menos 1 novo convite externo aceito.

- **Taxa de Bônus de Gênio:** Balanceada entre 15% e 25% do volume total de vitórias para preservar a sensação de conquista intelectual.

## PARTE 3 — GDD (GAME DESIGN DOCUMENT)

### 3.1. Visão Geral e Elevator Pitch

*"**Wordle encontra Sherlock Holmes na corte de um lorde gótico-futurista.**"* Em *O Vilão*, o jogador assume alternadamente os papéis de Arquiteto da Trapaça e Mestre da Fuga. Criar um enigma não é preencher um formulário; é forjar uma armadilha intelectual calculada para expor as falhas de raciocínio de seus amigos.

### 3.2. Core Loop de 6 Etapas

[1. ESCOLHER TEMA] ──> [2. IA GERA ENIGMA] ──> [3. PROVOCAR & DESAFIAR]
         ▲                                                │
         │                                                ▼
[6. VINGAR / REVANCHE] <── [5. RESULTADO & RANKING] <── [4. DECIFRAR TRAJETÓRIA]

- **Escolha de Tema:** O Curador seleciona o arquétipo do dilema (Alquimia, Criptografia, Paradoxos ou Crimes da Abadia).

- **Geração ****&**** Calibração IA:** O motor sintetiza o mistério garantindo consistência lógica estrita.

- **Provocação ****&**** Desafio:** O card personalizado é gerado com a assinatura do Vilão e despachado via redes sociais.

- **Decifração sob Pressão:** O Herói recebe o chamado, analisa a trilha dedutiva e enfrenta o relógio.

- **Resultado ****&**** Coorte:** O score é calculado, atualizando a posição relativa dos rivais no ranking semanal.

- **Revanche Imediata:** A derrota fomenta a necessidade psicológica de superação, reiniciando o ciclo com papéis invertidos.

### 3.3. Anatomia do Enigma (As 5 Camadas)

Todo desafio produzido pelo motor de jogo é estruturado em cinco componentes obrigatórios:

- **Camada 1 — Cenário Atmosférico:** Introdução narrativa de 2 a 3 frases imersivas situando o contexto espacial e histórico.

- **Camada 2 — Charada Central:** O problema lógico formal apresentado de forma poética e enigmática.

- **Camada 3 — Trilha de Dedução:** Estrutura encadeada de 2 a 4 premissas que devem ser validadas sequencialmente.

- **Camada 4 — Pistas Progressivas (Três Níveis):***Pista 1 (Sutil):* Reorienta o foco do jogador sem entregar variáveis (-10% pontuação).

- *Pista 2 (Direcional):* Elimina 1 distrator e detalha uma premissa (-25% pontuação).

- *Pista 3 (Reveladora):* Expõe a mecânica central de resolução (-50% pontuação).

- **Camada 5 — Resposta e Distratores:** Exatamente 1 alternativa matematicamente/logicamente comprovada e 3 distratores construídos sobre falácias cognitivas comuns.

### 3.4. Sistema de Pontuação e Bônus de Gênio

A pontuação final de uma tentativa é expressa pela seguinte formulação matemática:

$$Pontuacao = \left( PontosBase \times \frac{TempoRestante}{TempoTotal} \right) \times (1 - PenalidadePistas) \times MultiplicadorGenio$$

Onde:

- $$PontosBase = 1.000 \times DificuldadeCaveiras$$ (variando de 1.000 a 5.000 pontos).

- $$TempoTotal = 180 \text{ segundos}$$.

- $$PenalidadePistas = \sum (\text{Penalidades das pistas utilizadas})$$.

- $$MultiplicadorGenio = 1.5$$ caso $$TempoRestante \ge 0.70 \times TempoTotal$$ e $$PenalidadePistas = 0$$; caso contrário, $$MultiplicadorGenio = 1.0$$.

### 3.5. Tipologia dos Enigmas (Fase 1)

- **Charada Clássica Gótica:** Troilismos poéticos, metáforas ontológicas e identificação de elementos personificados.

- **Lógico-Dedutivo:** Problemas de ordenação temporal, silogismos formais e eliminação de suspeitos com álibis conflitantes.

- **Numérico-Sequencial:** Relações matemáticas embutidas em símbolos alquímicos, proporções áureas e séries geométricas.

- **Criptografia Rúnica:** Cifras de substituição monoalfabética com pistas contextuais baseadas nas runas do Herói.

### 3.6. Pipeline de IA em 5 Estágios

A sintetização dos desafios opera em uma esteira de execução serial inviolável:

- **Estágio 1 (Prompt Assembly):** Montagem dinâmica do prompt injetando diretrizes temáticas, grau de dificuldade e sementes aleatórias.

- **Estágio 2 (SLM Generation):** Execução do modelo de linguagem estruturado para produzir payloads estritos em conformidade com o JSON Schema.

- **Estágio 3 (Verificação Simbólica Determinística):** Algoritmo solver em Python valida se há apenas uma resposta possível e se os distratores violam as premissas.

- **Estágio 4 (Auditoria de Pistas):** Confirmação de que as pistas fornecidas seguem a hierarquia de revelação progressiva sem redundâncias.

- **Estágio 5 (Batch Ingestion ****&**** Cache):** Enigmas aprovados são gravados na tabela riddle_templates e pré-aquecidos no Redis para entrega instantânea.

### 3.7. Estratégia de Monetização Premium-First

O jogo opera sob uma ética estrita de **justiça competitiva** (Zero Pay-to-Win). Todas as transações financeiras são restritas a valor cosmético, conveniência e conteúdo intelectual expandido:

- **Acesso Gratuito:** 1 desafio diário curado global, 3 criações de enigmas por dia e acesso irrestrito ao ranking de coorte.

- **Passe de Temporada (Compra Única):** Desbloqueio de temas visuais exclusivos para o Vilão (skins de armadura gótica, trilha rúnica esmeralda para o Herói e molduras de perfil).

- **Assinatura ****"****Clube do Vilão****"**** (Mensal/Anual):** Criação ilimitada de enigmas, telemetria detalhada de erros dos desafiados, acesso antecipado a novas categorias lógicas e ingresso integral ao Tier Filosófico.

- **Rewarded Ads (Voluntário):** Possibilidade de assistir a 1 vídeo promocional curto para recuperar uma vida exclusivamente em modos não-ranqueados.

### 3.8. O Tier Filosófico

O Tier Filosófico é a divisão de maior prestígio do ecossistema. Seus enigmas são fundamentados exclusivamente em obras e pensadores em domínio público (Platão, Aristóteles, Santo Agostinho, Maquiavel, Spinoza, Kant, Schopenhauer e Nietzsche). O design de cada desafio segue a estrutura de **Dilema Dialético**: Tese, Antítese e Resolução Sintética. A curadoria é submetida a um filtro duplo de validação: conformidade semântica por IA especializada e revisão humana final.

### 3.9. Design e Especificação das 7 Telas do Sistema

TELAS MOBILE (9:16)<br/>
[TELA 1: CURADOR]       [TELA 2: DECIFRAÇÃO]    [TELA 3: CARD CONVITE]  [TELA 4: RANKING]
┌─────────────────┐     ┌──────────────────┐    ┌─────────────────┐     ┌─────────────────┐
│ [VILÃO] Perfil  │     │ 02:45  ♥♥♥  [?]  │    │ ╔═════════════╗ │     │ TOP 1 - COROA   │
│ Seletor de Tema │     │ ──────────────── │    │ ║ O VILÃO     ║ │     │ 1. LordV  9450p │
│ Dificuldade: 💀 │     │ CENÁRIO GÓTICO   │    │ ║ Desafio #84 ║ │     │ 2. Raven  8900p │
│ Preview Enigma  │     │ Charada Central  │    │ ║ "Aceitas?"  ║ │     │ ─────────────── │
│ [FORJAR DESAFIO]│     │ [1] [2] [3] [4]  │    │ ╚═════════════╝ │     │ 12. VOCÊ  7200p │
└─────────────────┘     └──────────────────┘    └─────────────────┘     └─────────────────┘

TELAS DESKTOP / PC (16:9)<br/>
[TELA 5: CONSTRUTOR AVANÇADO]  [TELA 6: TELEMETRIA]        [TELA 7: TIER FILOSÓFICO]
┌───────────────────────────┐  ┌─────────────────────────┐ ┌───────────────────────────┐
│ Biblioteca | Canvas Grid  │  │ KPIs: ACD | D1/D7 | K-F │ │ Galeria Bustos | Dialética│
│ Params IA  | Validação S. │  │ Curvas de Resolução / h │ │ Citação Matriz | Distrator│
│ [EXPORTAR / ATIVAR POOL]  │  │ Matriz Erros por Tópico │ │ [HOMOLOGAR DESAFIO ELITE] │
└───────────────────────────┘  └─────────────────────────┘ └───────────────────────────┘

- **Tela 1: O Curador (Mobile 9:16 — Criação):** Topo com avatar do Vilão, carrossel horizontal de temas góticos, seletor de dificuldade em caveiras, caixa de pré-visualização da charada e botão inferior full-width "FORJAR DESAFIO & PROVOCAR" em gradiente Roxo Real com glow Roxo Neon. (Mapeamento: FR-001, FR-002).

- **Tela 2: Tela de Decifração (Mobile 9:16 — Gameplay):** HUD superior minimalista com cronômetro centralizado em Roboto Mono, indicador de 3 vidas em formato de broches celtas verdes e botão "PISTA". Área central com texto da charada em tipografia Inter sobre fundo Carvão Escuro. Grade inferior 2x2 com as 4 opções de resposta. (Mapeamento: FR-006, FR-007, FR-008).

- **Tela 3: Card de Convite Compartilhável (Mobile 9:16 / 1:1):** Composição artística com moldura ornamental dourada gótica, retrato em chiaroscuro do Vilão desafiante, texto de provocação personalizada ("Consegues decifrar o Enigma da Cripta das Sombras ou temes o fracasso?"), QR Code e botão de ação primária "ACEITAR DESAFIO". (Mapeamento: FR-005).

- **Tela 4: Ranking por Coorte (Mobile 9:16 — Social):** Seletor de período (Semanal / Temporada), pódio superior com o líder da coorte em destaque com coroa dourada, listagem dos 30 integrantes do grupo com avatar, score e botão de desafio direto. Linha do usuário fixada na base com iluminação Verde Neon. (Mapeamento: FR-010, FR-013).

- **Tela 5: Construtor Avançado de Enigmas (PC 16:9 — Engenharia):** Painel de três colunas: biblioteca de módulos lógicos à esquerda, canvas central de encadeamento de premissas com grid milimétrico roxo e inspetor de parâmetros de inferência IA à direita com status de validação simbólica determinística. (Mapeamento: FR-002, FR-003, FR-004).

- **Tela 6: Dashboard de Telemetria e Balanceamento (PC 16:9 — Analytics):** Grid com 4 cards executivos superiores (ACD, Retenção D1/D7/D30, K-Factor e Taxa de Bônus de Gênio), seguidos por gráficos de densidade de resolução por tempo e matriz de calor de erros por distrator. (Mapeamento: FR-011).

- **Tela 7: Painel do Tier Filosófico (PC 16:9 — Curadoria Erudita):** Galeria visual com bustos renderizados dos pensadores clássicos em chiaroscuro dourado, editor dialético de premissas e selo formal de homologação em duas etapas (IA + Curadoria Humana). (Mapeamento: FR-016).

## PARTE 4 — TDD (TECHNICAL DESIGN DOCUMENT)

### 4.1. Arquitetura de Software e Fluxo de Dados

┌┐
│                        CLIENT LAYER (FRONTEND)                         │
│   Next.js 14 App Router (Desktop Web)  /  React Native Expo (Mobile)   │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ HTTPS / WSS (TLS 1.3 + HMAC-SHA256)
                                   ▼
┌┐
│                       GATEWAY & APPLICATION API                        │
│                 FastAPI (Python 3.11 / AsyncIO / Uvicorn)              │
│       Rate Limiting (1.500 req/s) ── JWT Auth ── Input Sanitizer       │
└──────────────┬───────────────────┬───────────────────┬─────────────────┘
               │                   │                   │
               ▼                   ▼                   ▼
┌──────────────────────┐ ┌───────────────────┐ ┌─────────────────────────┐
│   DATABASE LAYER     │ │   CACHE & QUEUE   │ │  INFERENCE ENGINE (IA)  │
│  PostgreSQL 16 Nativo│ │  Redis 7 Cluster  │ │  Ollama Worker Pool     │
│  Particionamento     │ │  Sessões / Cache  │ │  Mistral-7B-Instruct    │
│  Schema Segregado    │ │  Filas Celery     │ │  Quantização INT4 GGUF  │
└──────────────────────┘ └───────────────────┘ └─────────────────────────┘

### 4.2. Modelo de Dados Relacional (Schema PostgreSQL 16)

-- Extensões obrigatórias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Esquema de dados privados para conformidade com LGPD
CREATE SCHEMA IF NOT EXISTS pii_data;

-- 1. Temas dos Enigmas
CREATE TABLE riddle_themes (
    theme_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(128) NOT NULL,
    description TEXT NOT NULL,
    accent_color VARCHAR(7) DEFAULT '#8B5CF6',
    is_philosophical BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Templates e Enigmas Homologados
CREATE TABLE riddle_templates (
    riddle_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id UUID NOT NULL REFERENCES riddle_themes(theme_id),
    difficulty_level SMALLINT CHECK (difficulty_level BETWEEN 1 AND 5),
    scenario_context TEXT NOT NULL,
    riddle_text TEXT NOT NULL,
    correct_answer VARCHAR(255) NOT NULL,
    distractors JSONB NOT NULL, -- Array de exatamente 3 strings
    deduction_steps JSONB NOT NULL, -- Passos sequenciais de dedução
    symbolic_hash VARCHAR(64) NOT NULL, -- Hash de integridade lógica
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Pistas Estruturadas
CREATE TABLE clues (
    clue_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    riddle_id UUID NOT NULL REFERENCES riddle_templates(riddle_id) ON DELETE CASCADE,
    tier_level SMALLINT CHECK (tier_level BETWEEN 1 AND 3),
    clue_text TEXT NOT NULL,
    score_penalty_percent NUMERIC(4,2) NOT NULL, -- Ex: 0.10, 0.25, 0.50
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Desafios Criados pelos Usuários
CREATE TABLE challenges (
    challenge_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    creator_user_id UUID NOT NULL,
    riddle_id UUID NOT NULL REFERENCES riddle_templates(riddle_id),
    custom_provocation VARCHAR(280),
    share_token VARCHAR(64) UNIQUE NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Sessões de Tentativa (Particionamento por Data)
CREATE TABLE riddle_attempts (
    attempt_id UUID DEFAULT gen_random_uuid(),
    challenge_id UUID NOT NULL REFERENCES challenges(challenge_id),
    solver_user_id UUID NOT NULL,
    started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    finished_at TIMESTAMPTZ,
    time_spent_seconds NUMERIC(6,2),
    clues_used SMALLINT[] DEFAULT '{}',
    is_correct BOOLEAN DEFAULT FALSE,
    session_hmac VARCHAR(64) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (attempt_id, created_at)
) PARTITION BY RANGE (created_at);

-- 6. Resultados e Pontuação
CREATE TABLE results (
    result_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    attempt_id UUID NOT NULL,
    attempt_created_at TIMESTAMPTZ NOT NULL,
    base_points INTEGER NOT NULL,
    time_bonus NUMERIC(6,2) NOT NULL,
    penalties NUMERIC(6,2) NOT NULL,
    genius_multiplier NUMERIC(3,2) DEFAULT 1.0,
    final_score INTEGER NOT NULL,
    calculated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. Ranking de Coortes
CREATE TABLE ranking_entries (
    entry_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cohort_id UUID NOT NULL,
    user_id UUID NOT NULL,
    accumulated_score INTEGER DEFAULT 0,
    challenges_completed INTEGER DEFAULT 0,
    genius_awards_count INTEGER DEFAULT 0,
    rank_position INTEGER,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 8. Eventos de Telemetria (Anonimizada)
CREATE TABLE telemetry_events (
    event_id UUID DEFAULT gen_random_uuid(),
    session_hash VARCHAR(64) NOT NULL,
    event_type VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    client_timestamp TIMESTAMPTZ NOT NULL,
    server_timestamp TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (event_id, server_timestamp)
) PARTITION BY RANGE (server_timestamp);

### 4.3. Motor de Validação Simbólica (Python)

from typing import List, Dict, Any
import hashlib
import json

class SymbolicValidator:
    """
    Quality Gate determinístico para validação lógica e semântica de enigmas.
    Garante unicidade da resposta, plausibilidade e ausência de contradições.
    """
    @staticmethod
    def validate_riddle_payload(payload: Dict[str, Any]) -> bool:
        required_keys = ["scenario", "riddle", "correct_answer", "distractors", "deduction_steps"]
        if not all(k in payload for k in required_keys):
            return False
            
        distractors: List[str] = payload.get("distractors", [])<br/>
        correct_answer: str = payload.get("correct_answer", "").strip()
        
        # Regra 1: Exatamente 3 distratores<br/>
        if len(distractors) != 3:
            return False
            
        # Regra 2: Distratores devem ser distintos entre si e da resposta correta
        all_answers = set([d.strip().lower() for d in distractors] + [correct_answer.lower()])
        if len(all_answers) != 4:
            return False
            
        # Regra 3: Trilha de dedução deve conter entre 2 e 4 passos encadeados<br/>
        steps: List[str] = payload.get("deduction_steps", [])<br/>
        if not (2 <= len(steps) <= 4):
            return False
            
        return True

    @staticmethod
    def generate_integrity_hash(payload: Dict[str, Any]) -> str:
        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(serialized.encode('utf-8')).hexdigest()

### 4.4. Pipeline de Inferência e JSON Schema Estrito

{
  "$schema": "http://json-schema.org/draft-07/schema#",<br/>
  "title": "RiddleGenerationSchema",<br/>
  "type": "object",<br/>
  "properties": {<br/>
    "scenario": {<br/>
      "type": "string",<br/>
      "minLength": 40,<br/>
      "maxLength": 300
    },
    "riddle": {<br/>
      "type": "string",<br/>
      "minLength": 30,<br/>
      "maxLength": 250
    },
    "correct_answer": {<br/>
      "type": "string",<br/>
      "minLength": 1,<br/>
      "maxLength": 60
    },
    "distractors": {<br/>
      "type": "array",<br/>
      "items": { "type": "string", "minLength": 1, "maxLength": 60 },<br/>
      "minItems": 3,<br/>
      "maxItems": 3
    },
    "deduction_steps": {<br/>
      "type": "array",<br/>
      "items": { "type": "string", "minLength": 10, "maxLength": 150 },<br/>
      "minItems": 2,<br/>
      "maxItems": 4
    },
    "clues": {<br/>
      "type": "array",<br/>
      "items": {<br/>
        "type": "object",<br/>
        "properties": {<br/>
          "tier": { "type": "integer", "minimum": 1, "maximum": 3 },<br/>
          "text": { "type": "string", "minLength": 10, "maxLength": 150 }
        },
        "required": ["tier", "text"]
      },
      "minItems": 3,<br/>
      "maxItems": 3
    }
  },
  "required": ["scenario", "riddle", "correct_answer", "distractors", "deduction_steps", "clues"],<br/>
  "additionalProperties": false
}

### 4.5. Implementação do Motor de Pontuação

from decimal import Decimal

def calculate_final_score(
    difficulty: int,<br/>
    time_spent: float,<br/>
    total_time: float,<br/>
    clues_penalties: list[float]<br/>
) -> dict:
    base_points = difficulty * 1000
    time_ratio = max(0.0, (total_time - time_spent) / total_time)
    penalty_sum = sum(clues_penalties)
    
    score_raw = (base_points

time_ratio)

(1.0 - penalty_sum)
    
    # Critério do Bônus de Gênio: resolução em <= 30% do tempo sem pistas
    is_genius = (time_spent <= 0.30 * total_time) and (len(clues_penalties) == 0)
    genius_multiplier = 1.5 if is_genius else 1.0
    
    final_score = int(round(score_raw * genius_multiplier))
    
    return {
        "base_points": base_points,<br/>
        "final_score": max(0, final_score),<br/>
        "is_genius": is_genius,<br/>
        "genius_multiplier": genius_multiplier
    }

### 4.6. Especificações Técnicas de Renderização dos Personagens

- **Shaders PBR ****&**** Emissão:** Material com Roughness entre 0.35 e 0.60 para armaduras metálicas e tecidos góticos. Mapas de Emissive calibrados em 8.0 nits em canais isolados (Roxo Neon #8B5CF6 e Verde Neon #39FF14) com pós-processamento de *Bloom* ativado.

- **Rim Lighting Chiaroscuro:** Aplicação de luz rasante lateral/dorsal em ângulo de 135° em relação à câmera principal para descolar os personagens dos cenários escuros.

- **Estrutura de Rigging ****&**** Blend Shapes:** O Vilão conta com 12 blend shapes faciais dedicados a microexpressões de desdém e cálculo analítico, além de bones independentes de IK para manipulação do Cajado-Tridente. O Herói possui rig esquelético de 72 ossos, malha com simulação física de capa (*Cloth Simulation*) em 30 FPS e controladores para tensionamento da corda de plasma do arco.

- **Otimização de Assets:** Renderização em WebGL2 / Metal com compressão de texturas KTX2 / ASTC, mapas normais em 2K para desktop e 1K para dispositivos mobile.

### 4.7. Protocolos de Segurança e Anti-Cheat

- **Ocultação Absoluta do Gabarito:** As opções de resposta são enviadas ao cliente acompanhadas apenas de um nonce aleatório. O ID da resposta correta jamais trafega no payload do frontend.

- **Assinatura Criptográfica de Sessão (HMAC-SHA256):** Toda ação de abertura de tela, consumo de pista e envio de resposta é assinada com chave efêmera vinculada ao timestamp do servidor.

- **Detecção de Fraude Temporal:** Resoluções submetidas em tempo inferior a 3.5 segundos são flagradas como anomalia por telemetria e direcionadas para quarentena de pontuação.

### 4.8. Telemetria e Conformidade LGPD

O identificador dos jogadores é pseudonimizado por meio de funções criptográficas de via única (`SHA-256(user_id + salt_rotativo)`). Nenhum dado que permita a correlação direta de identidade é persistido nos logs analíticos. A exclusão de conta via solicitação do usuário aciona uma rotina em cascata de expurgo na tabela `pii_data.user_identities` preservando apenas os registros puramente estatísticos e desprovidos de identificadores.

### 4.9. Estratégia de Testes e Homologação Técnica

- **Testes Unitários:** Cobertura mínima obrigatória de 85% do código Python no backend (pytest).

- **Testes de Estresse de Carga:** Simulação contínua com Locust para sustentar 1.500 usuários virtuais concorrentes executando o core loop completo sem ultrapassar latência de 250ms em endpoints críticos.

## PARTE 5 — REGRAS DE CONSISTÊNCIA PARA GERAÇÃO (CHECKLIST PARA A IA)

Antes de apresentar qualquer resultado, entrega de código, prompt de geração de arte ou mockups de tela, a IA atuante DEVE validar se a saída cumpre integralmente os 8 itens deste checklist:

- **Paleta Estrita:** As cores geradas pertencem exclusivamente à paleta oficial (Carvão, Roxo, Verde, Dourado)? Não há presença de ciano ou magenta genéricos?

- **Hierarquia Tipográfica:** A tipografia segue a tríade Cinzel (títulos góticos), Inter (corpo/UI) e Roboto Mono (dados e cronômetros)?

- **Identidade dos Personagens:** O Vilão mantém a silhueta aristocrática em roxo com máscara/cajado e o Herói mantém o design de arqueiro jovem em verde com arco rúnico?

- **Iluminação Chiaroscuro:** A iluminação é orientada a luz rasante, com sombras densas e rim lights de alto contraste entre o sujeito e o cenário?

- **Acessibilidade e Ergonomia:** O contraste tipográfico respeita a norma WCAG AA (mínimo de 4.5:1) e os alvos de clique mobile possuem área mínima de 44x44 pixels?

- **Matriz de Estados de Componentes:** Foram especificados todos os estados de interação visual dos botões e cards (default, hover, active, disabled, loading e error)?

- **Conformidade Funcional:** O fluxo respeita os requisitos funcionais FR-001 a FR-016 sem inventar mecânicas divergentes do GDD?

- **Regra 60-30-10:** A distribuição espacial de cor reserva 60% para superfícies escuras, 30% para sombras estruturais e apenas 10% para pontos luminescentes?

## PARTE 6 — PRÓXIMOS PASSOS E PLANO DE SPRINT

Para a materialização executiva da Revisão 3.0 de *O Vilão*, fica estabelecido o seguinte cronograma de execução técnica prioritária:

- **Sprint P0 (Dias 1 a 5):** Conclusão e congelamento das 4 telas mobile do core loop no repositório frontend, com vinculação imediata aos endpoints FastAPI.

- **Sprint P1 (Dias 6 a 10):** Implantação e validação do pipeline de telemetria (FR-011) e motor de particionamento no PostgreSQL 16.

- **Sprint P2 (Dias 11 a 15):** Execução de teste de estresse fechado com coorte alfa de 30 jogadores simultâneos para calibração final do Bônus de Gênio e estabilidade de latência.

**Tales**

Curador e Líder de Produto — Hack Tech Farm

Documento homologado em 29 de agosto de 2026. Proibida a alteração sem autorização formal da liderança de produto.