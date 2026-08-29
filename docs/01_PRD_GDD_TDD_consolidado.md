Hack Tech Farm

**O VILÃO — PACOTE COMPLETO DE DOCUMENTAÇÃO: PRD, GDD, DESIGN SYSTEM, TDD E BACKLOG CONSOLIDADO**

*Revisão 3.0 — Pivô para Orquestração de Enigmas e Duelos Dedutivos*

29 de agosto de 2026

## SUMÁRIO EXECUTIVO E DECLARAÇÃO DE PIVÔ

O presente documento estabelece a fonte única de verdade arquitetural, de produto, de design visual e de engenharia para o projeto **O Vilão**, desenvolvido pela **Hack Tech Farm**. Esta Revisão 3.0 consolida formalmente o pivô de game design: a transição definitiva do modelo anterior de construtor de armadilhas físicas em grade bidimensional para uma plataforma de **curadoria de enigmas e duelos dedutivos assíncronos**.

No modelo anterior, a fricção cognitiva na criação manual de fases espaciais gerava gargalos de retenção e assimetria de esforço entre criador e jogador. No novo paradigma, o jogador no papel de Vilão atua como um *Curador e Arquiteto do Dilema*: seleciona eixos temáticos e restrições conceituais, enquanto modelos de linguagem especializados (SLMs locais) e validadores determinísticos forjam charadas lógicas, trilhas de premissas dedutivas, pistas progressivas com custo de precisão e distratores de alta verossimilhança. O Herói, por sua vez, enfrenta o enigma sob intensa restrição temporal (1 a 3 minutos), decifrando premissas em um ambiente de Dark Fantasy Chiaroscuro.

A tese mestra do ecossistema permanece inalterada: *"**O convite é o jogo**"*. Cada enigma resolvido converte-se em um artefato social de provocação, impulsionando o coeficiente viral (

$$K\text{-factor} \geq 15%$$

) e alavancando a rivalidade assimétrica como motor primário de aquisição e retenção orgânica.

## PARTE 1 — PRODUCT REQUIREMENTS DOCUMENT (PRD) DEFINITIVO

### 1.1 Objetivo do Produto e Tese de Validação

O objetivo central do MVP de **O Vilão** é validar, com alocação mínima de capital e zero dependência de plataformas BaaS proprietárias, a hipótese comportamental de que usuários retornam com frequência diária para criar e decifrar desafios lógicos rápidos, comparam seus coeficientes intelectuais e tempos de resposta em círculos sociais fechados, e monetizam voluntariamente em um ecossistema estritamente cosmético e de prestígio intelectual, no qual a justiça competitiva é matematicamente inviolável.

O MVP não é estruturado como uma tentativa de captura de TAM massivo, mas como um teste de densidade de retenção (

$$D1 \geq 25%$$

, 

$$D7 \geq 9%$$

) e de coeficiente de propagação orgânica via cartas de convite gráficas com deep linking nativo.

### 1.2 Público-Alvo e Matriz de Personas

| **Persona** | **Papel Primário** | **Faixa Etária** | **Motivação Central** | **Comportamento na Plataforma** |
| --- | --- | --- | --- | --- |
| **O Curador** | Vilão (Fase 1) | 20 a 35 anos | Expressão de status intelectual e provocação social | Seleciona temas complexos, calibra pistas difíceis e compartilha cartas de desafio via redes e mensageiros. |
| **O Decifrador** | Herói (Fase 1) | 18 a 45 anos | Resolução rápida de problemas e senso de superação | Acessa via deep links recebidos, joga sessões de 90 a 150 segundos sob pressão e busca o Bônus de Gênio. |
| **O Detetive** | Modo Solo (Fase 2) | 25 a 50 anos | Hábito diário analítico e manutenção de sequências (streaks) | Consome o enigma procedural diário no deslocamento diário, focado em subir posições no ranking nacional de coortes. |
| **O Intelectual Erudito** | Tier Filosófico (Fase 2/3) | 22 a 55 anos | Dilemas éticos, rigor dialético e estética acadêmica | Assinante do Clube do Vilão, focado em resolver e forjar dilemas baseados em obras de pensadores históricos. |

### 1.3 Escopo do MVP (In/Out)

**Dentro do Escopo (IN):**

1. Interface de curadoria de desafios com seleção de temas góticos e lógicos.
2. Geração algorítmica de enigmas via SLM local (Llama 3.2 3B / Mistral NeMo 3B) com schema JSON rígido.
3. Validador simbólico determinístico em Python para garantia de unicidade de solução e ausência de vazamento de premissas.
4. Interface de decifração do Herói com trilha de passos, cronômetro regressivo (60-180s) e 3 pistas escalonadas.
5. Geração de cartas de convite gráficas dinâmicas com metadados Open Graph e deep linking (o_vilao://challenge/{token}).
6. Sistema de pontuação com penalidades estritas de tempo, erros e pistas, além do multiplicador de Bônus de Gênio (

$$1.5\times$$

).
7. Ranking normalizado por coortes semanais, país e plataforma com tempo de resposta sub-300ms.
8. Infraestrutura independente sem BaaS proprietário (PostgreSQL 16 com pgcrypto, Redis 7 e Celery).

**Fora do Escopo do MVP (OUT):**

1. Sistema de guildas, clãs ou facções comunitárias.
2. Editor manual de texto livre sem restrição semântica (evita alucinação de IA e conteúdo tóxico).
3. Modo Detetive diário procedural com narrativa ramificada de longa duração (reservado para Fase 2).
4. Qualquer mecânica transacional que confira vantagens competitivas ou compra de pistas com moeda real (pay-to-win categoricamente proibido).
5. Mecânicas baseadas em blockchain, tokens especulativos ou NFTs.

### 1.4 Matriz de Requisitos Funcionais (FR-001 a FR-016)

| **ID** | **Módulo** | **Prioridade** | **Descrição Técnica do Requisito** |
| --- | --- | --- | --- |
| **FR-001** | Curadoria | P0 | O sistema deve listar temas categorizados com metadados de dificuldade, renovados dinamicamente via job assíncrono. |
| **FR-002** | Geração IA | P0 | O motor de inferência deve gerar, via SLM local, cenário (2-3 frases), charada formal, trilha de dedução (2-4 passos) e 3 pistas progressivas em JSON estrito. |
| **FR-003** | Validação | P0 | O validador simbólico deve comprovar formalmente a existência de exatamente 1 resposta correta e assegurar que nenhuma pista contenha o gabarito literal. |
| **FR-004** | Distratores | P0 | O pipeline deve sintetizar entre 3 e 5 opções falsas verossímeis, pertencentes ao mesmo domínio semântico da resposta. |
| **FR-005** | Convites | P0 | O sistema deve renderizar o Card de Convite gráfico com deep link o_vilao://challenge/{token} e provocação personalizada. |
| **FR-006** | Trajetória | P0 | A interface do Herói deve processar a resolução passo a passo com feedback visual e bloqueio contra adulteração de estado local. |
| **FR-007** | Pistas | P0 | O sistema deve fornecer até 3 pistas progressivas sob demanda, aplicando penalidade imediata na pontuação e revogando o Bônus de Gênio. |
| **FR-008** | Temporizador | P0 | O cliente deve sincronizar cronômetro regressivo de 60 a 180s com validação no backend; o esgotamento do tempo aciona derrota automática. |
| **FR-009** | Revanche | P0 | A tela de desfecho deve permitir que o perdedor gere imediatamente um contra-desafio, invertendo os papéis de Herói e Vilão. |
| **FR-010** | Ranking | P0 | O serviço de ranking deve calcular e servir tabelas particionadas por coortes temporais semanais com latência P95 < 250ms. |
| **FR-011** | Telemetria | P0 | O coletor deve registrar eventos granulares de funil (abertura, clique de pista, submissão, share) com isolamento estrito de dados pessoais (LGPD). |
| **FR-012** | Pool Rotativo | P1 | Um worker Celery deve manter buffer de 200 a 500 enigmas pré-validados por categoria em cache Redis para entrega instantânea. |
| **FR-013** | Bônus Gênio | P1 | O motor de pontuação deve aplicar multiplicador de 1.5x na pontuação base quando a vitória ocorrer sem uso de pistas e sem submissões incorretas. |
| **FR-014** | Monetização | P1 | A plataforma deve processar compras in-app de pacotes de temas visuais e rewarded ads voluntários pós-partida sem impacto no gameplay. |
| **FR-015** | Modo Detetive | P2 | O sistema deve disponibilizar enigma procedural diário universal com ranking dedicado de manutenção de sequência (streaks). |
| **FR-016** | Tier Filosófico | P2 | O catálogo deve suportar temas eruditos fundamentados em obras de domínio público, validados por curadoria humana assistida. |

### 1.5 Requisitos Não-Funcionais (NFR)

**NFR-001 — Latência e Performance:** As requisições de consulta de ranking, carregamento de enigmas cacheados e validação de tokens devem responder em tempo 

$$P95 < 250\text{ms}$$

 e 

$$P99 < 500\text{ms}$$

 sob carga nominal.

**NFR-002 — Eficiência de Custo Marginal:** O custo de computação de inferência de IA não deve exceder R$ 0,001 por enigma forjado, viabilizado pela utilização de SLMs compactos (3B parâmetros) rodando localmente via Ollama em infraestrutura dedicada, com cache de premissas em Redis.

**NFR-003 — Arquitetura de Dados Zero-Supabase:** Persistência relacional estrita em PostgreSQL 16 nativo, orquestrado com SQLAlchemy 2.0 assíncrono e migrações versionadas via Alembic. Proibido o acoplamento a BaaS proprietários.

**NFR-004 — Conformidade e Segurança (LGPD):** Isolamento completo de dados identificáveis em schema pii_data criptografado com extensão pgcrypto (AES-256). Identificadores em telemetria devem ser tratados exclusivamente via hashes anônimos irreversíveis (HMAC-SHA-256 com salt rotativo).

**NFR-005 — Confiabilidade e Resiliência:** O backend deve suportar throughput contínuo de 1.500 requisições concorrentes por segundo, com taxa global de erro HTTP 5xx inferior a 

$$0,01%$$

.

### 1.6 Métricas de Sucesso e Gates de Validação

A métrica *North Star* do projeto é o volume de **Desafios Aceitos por Dia (ACD — Accepted Challenges per Day)**. O avanço entre as fases do ciclo de vida do produto é estritamente condicionado aos seguintes gates de validação comportamental:

| **Métrica / Indicador** | **Alvo Mínimo (Gate)** | **Frequência de Medição** | **Impacto no Produto** |
| --- | --- | --- | --- |
| **Retenção D1** | $$\geq 25\%$$ | Diária (Coortes de 24h) | Valida o apelo imediato do loop de decifração. |
| **Retenção D7** | $$\geq 9\%$$ | Semanal | Comprova formação de hábito e dinâmica de rivalidade. |
| **Retenção D30** | $$\geq 3\%$$ | Mensal | Sustenta a viabilidade do LTV sobre aquisição orgânica. |
| **Taxa de Conclusão** | $$\geq 60\%$$ | Por Enigma / Sessão | Evita frustração cognitiva excessiva no gameplay. |
| **K-Factor (Viralidade)** | $$\geq 15\%$$ | Semanal | Garante que 100 partidas gerem no mínimo 15 novos jogadores. |
| **Bônus de Gênio** | $$15\% \text{ a } 25\%$$ | Por Sessão Concluída | Equilibra a curva de dificuldade e recompensa por maestria. |

### 1.7 Critérios de Lançamento (Definition of Done — DoD)

O lançamento do MVP em ambiente de produção (Beta Fechado e Soft Launch) exige o cumprimento mandatório dos seguintes critérios de aceite:

1. Base inicial de 500 modelos de enigmas formalmente validados e indexados no pool rotativo.
2. Tempo médio de entrega de desafio pré-gerado ao cliente inferior a 800ms.
3. Cobertura de testes automatizados superior a 85% nos módulos críticos (motor de validação simbólica, cálculo de pontuação, sincronização de tempo e autenticação JWT).
4. Zero dependências ativas de serviços BaaS (Firebase, Supabase, Appwrite).
5. Pipeline de observabilidade e dashboard de telemetria operacional com atualização em tempo real.

## PARTE 2 — GAME DESIGN DOCUMENT (GDD) DEFINITIVO

### 2.1 Visão Geral e Atmosfera

**O Vilão** é um jogo social assíncrono de duelos intelectuais e dedução lógica, ambientado em uma estética *Dark Fantasy Chiaroscuro* que mescla a solenidade de catedrais góticas a elementos cibernéticos minimalistas. O Vilão atua como o arquiteto do dilema, enquanto o Herói é o decifrador ágil sob pressão temporal implacável.

### 2.2 Elevator Pitch

"Wordle encontra Sherlock Holmes sob o teatro de um vilão aristocrata refinado: desafie seus amigos com enigmas lógicos gerados por IA, onde cada pista custa seu orgulho intelectual e cada falha alimenta a glória do seu rival."

### 2.3 Core Loop Revisado (6 Etapas)

O ciclo de engajamento é estruturado em seis fases consecutivas, projetadas para durar entre 90 e 180 segundos por ciclo completo:

**1. Escolha do Tema:** O Vilão navega por um catálogo temático rotativo (ex.: *Alquimia **&** Venenos*, *Criptografia do Século XIX*, *Paradoxos do Tempo*) e define o nível de desafio almejado.
**2. Forja Algorítmica:** O motor de IA instancia uma charada lógica fechada, acompanhada de premissas formais, distratores semânticos e três pistas escalonadas.
**3. Provocação ****&**** Desafio:** O Vilão personaliza uma mensagem sarcástica gerada pela IA e despacha a carta de convite gráfica via link direto para seu oponente.
**4. Decifração Sob Pressão:** O Herói aceita o convite, visualiza a charada e avança na trilha dedutiva contra um cronômetro regressivo de 1 a 3 minutos.
**5. Veredito ****&**** Pontuação:** O sistema apura o resultado, calcula a pontuação com base em tempo, pistas e erros, e distribui as recompensas de coorte.
**6. Revanche Imediata:** A tela final estimula a inversão de papéis com um único toque, convertendo o Herói em Vilão para uma contraofensiva imediata.

### 2.4 Anatomia do Enigma e Sistema Matemático de Pontuação

Cada enigma é estruturado em cinco camadas lógicas independentes:

1. **Cenário Imersivo:** 2 a 3 frases que estabelecem o contexto narrativo e a atmosfera dramática.
2. **Charada Formal:** A proposição central que contém o problema lógico a ser resolvido.

3. **Trilha de Dedução:** Sequência de 2 a 4 passos intermediários verificáveis que conduzem à resposta.

4. **Pistas Progressivas:** 3 dicas graduais (Pista 1: Conceitual; Pista 2: Redução de Escopo; Pista 3: Quase Revelação).

5. **Matriz de Resposta:** Exatamente 1 resposta correta e 3 a 5 distratores com alto grau de coerência semântica.

A pontuação do jogador é determinada pela seguinte função determinística:

$$\text{Pontuação Base} = 1000 \times \mathbb{I}(\text{vitória})$$

$$\text{Bônus de Tempo} = \max\left(0, \frac{\text{TempoLimite} - \text{TempoGasto}}{\text{TempoLimite}}\right) \times 300$$

$$\text{Penalidade de Pistas} = \text{PistasUsadas} \times 150$$

$$\text{Penalidade de Erros} = \text{SubmissõesIncorretas} \times 200$$

$$\text{Pontuação Preliminar} = \max\left(0, \text{Pontuação Base} + \text{Bônus de Tempo} - \text{Penalidade de Pistas} - \text{Penalidade de Erros}\right)$$

$$\text{Pontuação Final} = \begin{cases} \text{Pontuação Preliminar} \times 1.5, & \text{se } \text{PistasUsadas} = 0 \land \text{SubmissõesIncorretas} = 0 \land \mathbb{I}(\text{vitória}) = 1 \ \text{Pontuação Preliminar}, & \text{caso contrário} \end{cases}$$

### 2.5 Pipeline de IA de Custo Marginal Zero (5 Estágios)

1. **Geração Estruturada (SLM):** Modelos compactos locais (Llama 3.2 3B / Mistral NeMo) recebem prompts em JSON restrito, especificando tema, nível de dificuldade e premissas lógicas necessárias.
2. **Validação Simbólica:** Parser determinístico em Python avalia as premissas e constrói a tabela verdade do enigma, rejeitando templates com zero ou mais de uma solução válida.

3. **Auditoria de Pistas:** Módulo de verificação semântica cruza os tokens das pistas contra a resposta final; se houver sobreposição léxica direta ou vazamento do gabarito, o enigma é descartado.

4. **Calibração de Dificuldade por Simulação:** O motor executa entre 30 e 50 simulações de resolução heurística com temperatura

$$\tau = 0.7$$

 para estimar a probabilidade de acerto empírica (

$$P_{\text{sucesso}}$$

) e atribuir o índice de caveiras (1 a 10).
5. **Buffer Rotativo (Celery + Redis):** Fila assíncrona mantém um buffer aquecido de 200 a 500 enigmas por categoria, eliminando a latência de inferência em tempo de jogo.

### 2.6 Modelo de Monetização Premium-First

| **Modalidade** | **Preço Sugerido** | **Conteúdo / Benefício** | **Impacto no Gameplay** |
| --- | --- | --- | --- |
| **Acesso Gratuito Pleno** | R$ 0,00 | Enigma diário universal, até 3 desafios criados/aceitos por dia e ranking de coorte. | Zero restrição no balanceamento; acesso integral ao core loop. |
| **Pacotes de Temas** | R$ 9,90 a R$ 19,90 | Temas visuais cosméticos (ex.: *Gótico Vitoriano*, *Cibernética Arcana*) e molduras de perfil. | Puramente cosmético; sem alteração em multiplicadores de pontos. |
| **Clube do Vilão (Assinatura)** | R$ 14,90 / mês | Criação ilimitada de enigmas, telemetria detalhada de oponentes, emblema de assinante e acesso ao Tier Filosófico. | Prestígio social e conveniência analítica; sem vantagens no ranking competitivo. |
| **Rewarded Ads** | Gratuito (Opção do Jogador) | Possibilidade de visualizar um anúncio voluntário de 15-30s pós-partida para desbloquear tentativa de revanche em modo casual. | Proibido em partidas ranqueadas oficiais. |

### 2.7 Metadados de Balanceamento e Métricas de Sessão

1. **Taxa de Conclusão por Nível de Dificuldade:**
- Fácil (1 a 3 caveiras):

$$75% \text{ a } 85%$$

de resolução com sucesso.
- Médio (4 a 6 caveiras):

$$50% \text{ a } 65%$$

de resolução com sucesso.
- Difícil (7 a 10 caveiras):

$$20% \text{ a } 35%$$

de resolução com sucesso.
2. **Tempo Médio de Sessão:** 90 a 150 segundos por duelo.

3. **Índice de Revanche Imediata:** Meta de

$$\geq 22%$$

de conversão na tela de desfecho.
4. **Taxa de Compartilhamento Social:** Meta de

$$\geq 35%$$

 dos desafios criados distribuídos via WhatsApp, Telegram ou Instagram Stories.

### 2.8 Plataforma e Entidades Relacionais

O frontend é implementado em Next.js 14 (App Router) e React Native (Expo), servido por backend FastAPI (Python 3.12). O modelo de dados gira em torno das seguintes entidades fundamentais:

- riddle_themes: Metadados, tags semânticas e status de rotação dos temas.
- riddle_templates: Estrutura lógica validada, charada, solução e metadados de dificuldade.

- clues: Pistas escalonadas vinculadas a cada template com ordem e peso de penalidade.

- challenges: Instâncias ativas de desafio, vinculando o criador (Vilão), o token público e a provocação personalizada.

- riddle_attempts: Registro temporal de cada tentativa do Herói, incluindo tempo gasto, passos executados e pistas abertas.

- results: Consolidação de vitória/derrota, pontuação matemática, Bônus de Gênio e timestamps.

- ranking_entries: Índices particionados por coorte temporal e região.

- telemetry_events: Trilhas anônimas de eventos comportamentais.

### 2.9 Roadmap Estratégico de Produto

| **Fase** | **Denominação** | **Marco Principal de Entrega** | **Condição de Saída (Exit Gate)** |
| --- | --- | --- | --- |
| **Fase 0** | Protótipo Dialético | Validação de 5 enigmas lógicos autorais em ambiente web fechado. | Taxa de engajamento manual > 70% em coorte de 30 usuários. |
| **Fase 1** | MVP de Enigmas IA | Core loop completo, pipeline SLM local, validadores determinísticos e ranking por coortes. | D1 ≥ 25%, D7 ≥ 9%, K-Factor ≥ 15% sustentados por 14 dias. |
| **Fase 2** | Modo Detetive & Social | Enigma procedural diário universal, sequências (streaks) e perfis públicos com vitrines de troféus. | D30 ≥ 3% e mais de 10.000 desafios aceitos por dia. |
| **Fase 3** | Escala & Guildas | Duelos intelectuais entre grupos, torneios sazonais e marketplace de temas cosméticos da comunidade. | Monetização mensal autossustentável e expansão internacional. |
| **Fase Filosófica** | Tier Filosófico | Catálogo de dilemas éticos e dialéticos com validação humana assistida e selo de prestígio. | Mais de 2.000 assinantes ativos no Clube do Vilão. |

### 2.10 Tier Filosófico (Escalão Premium)

O **Tier Filosófico** é o escalão intelectual de prestígio de **O Vilão**. Fundamenta-se em cinco vertentes clássicas do pensamento humano: *Estoicismo*, *Racionalismo*, *Empirismo*, *Iluminismo* e *Existencialismo*. Todo o conteúdo é ancorado estritamente em autores em domínio público, incluindo Platão, Aristóteles, Sêneca, Marco Aurélio, Baruch Espinosa, René Descartes, Immanuel Kant, Friedrich Nietzsche, Fiódor Dostoiévski e Victor Hugo.

A esteira de publicação do Tier Filosófico adota **curadoria em 2 camadas**: a IA sintetiza o dilema e a correlação lógica da tese do pensador com a charada, e a aprovação final é submetida à revisão e validação editorial de Tales (Curador e Líder de Produto), garantindo rigor conceitual e precisão histórica.

### 2.11 Identidade Visual — Dark Fantasy Chiaroscuro

A identidade visual adota a regra áurea de composição **60-30-10**: 60% de superfícies em Carvão Profundo e nuances de pedra escura (fundo e estrutura), 30% de elementos funcionais em Roxo Profundo ou Verde Escuro (painéis, cartões e superfícies elevadas), e 10% de acentos luminescentes em Roxo Neon, Verde Neon e Dourado de Prestígio.

| **Nome do Token** | **Valor HEX** | **Papel no Design System** | **Proporção de Aplicação** |
| --- | --- | --- | --- |
| --color-bg-primary | #121212 | Carvão Escuro (fundo principal de telas) | 60% (Base Estrutural) |
| --color-bg-surface | #1A1A1A | Carvão Profundo (cards, painéis e dialogs) | Superfície Elevada |
| --color-bg-subtle | #2A2A2A | Carvão Médio (bordas e divisórias) | Delimitação Estrutural |
| --color-villain-primary | #6A3FA0 | Roxo Real (identidade do Vilão e CTAs de forja) | 30% (Secundário/Identidade) |
| --color-villain-deep | #3D1F6E | Roxo Profundo (gradientes e estados ativos) | Profundidade do Vilão |
| --color-villain-neon | #8B5CF6 | Roxo Neon (rim light, glows e acentos de IA) | 10% (Acento Luminescente) |
| --color-hero-primary | #22C55E | Verde Esmeralda (identidade do Herói e resolução) | 30% (Secundário/Identidade) |
| --color-hero-neon | #39FF14 | Verde Neon (runas, feedback de sucesso e trilha) | 10% (Acento Luminescente) |
| --color-gold-primary | #D4AF37 | Dourado Prestígio (Top 1, Tier Filosófico e Bônus Gênio) | Acento de Prestígio |
| --color-gold-light | #F0D98C | Dourado Claro (destaques tipográficos em títulos) | Destaque Tipográfico |
| --color-text-primary | #F5F5F5 | Branco Puro Off-white (títulos e leitura prioritária) | Tipografia Primária |
| --color-text-secondary | #9E9E9E | Cinza Neutro (metadados, legendas e rótulos) | Tipografia Secundária |
| --color-state-success | #27AE60 | Verde Sucesso (confirmação e acertos) | Feedback Positivo |
| --color-state-error | #C0392B | Vermelho Dano (erros de dedução e timeout) | Feedback Negativo |

### 2.12 Especificação Narrativa e Visual dos Personagens

**O VILÃO — O Arquiteto do Dilema:**
Figura aristocrática e intimidadora. Enverga um sobretudo estruturado em tecido pesado de corte cerimonial, entremeado por filamentos e circuitos que emitem pulsação em Roxo Neon (#8B5CF6). O rosto é coberto por uma máscara geométrica angular em acabamento de obsidiana fosca, dotada de uma fenda vertical emissiva por onde escapa luz violeta de intensidade variável. Empunha um cajado tecnológico em liga escura encimado por um tridente estilizado que envolve um cristal de quartzo radiante. Possui 3 blend shapes faciais no rig: *Neutro Enigmático*, *Desprezo Calculado* e *Sorriso Sarcástico*.

**O HERÓI — O Decifrador Ágil:**
Arqueiro tecnomágico de feições jovens e afiadas. Veste capa e capuz de caçador em tom Verde Esmeralda (#22C55E) com forro em couro flexível. Suas braçadeiras metálicas exibem runas cibernéticas iluminadas em Verde Neon (#39FF14). No peito, ostenta um broche circular celta em latão envelhecido que ancora suas tiras de couro. Empunha um arco composto de geometria afiada com corda de plasma e aljava contendo flechas com penas energéticas. Possui 4 expressões faciais: *Foco Determinado*, *Surpresa Tática*, *Sorriso Confiante* e *Triunfo Amplo*.

### 2.13 Mapeamento de Telas do Novo Fluxo (7 Interfaces)

**1. Tela do Curador (Mobile 9:16 — Vilão):**
Cabeçalho com avatar do Vilão, contador de almas desafiadas e seletor de temas em carrossel horizontal com cards tridimensionais (ícone, título, dificuldade em caveiras). Painel central com pré-visualização da charada forjada pela IA, seletor de tom da provocação sarcástica e botão principal de largura total *"**FORJAR DESAFIO **&** PROVOCAR**"* com gradiente Roxo Real para Roxo Profundo e glow --shadow-glow-villain. Mapeamento: FR-001, FR-002, FR-004.

**2. Tela de Decifração (Mobile 9:16 — Herói):**
HUD superior compacto com cronômetro regressivo destacado (fonte Roboto Mono), vidas restantes representadas por broches celtas estilizados e botão de ação secundária *"**SOLICITAR PISTA (-150 pts)**"*. Área de cenário com texto narrativo em Cinzel, seguida pelo bloco da charada e pela trilha de dedução interativa com nós conectores. Na base, balão de fala translúcido com avatar do Vilão proferindo provocações contextuais e grade de 4 botões de alternativas com feedback de seleção instantâneo. Mapeamento: FR-006, FR-007, FR-008.

**3. Card de Convite Compartilhável (Mobile 9:16 / 1:1):**
Artefato visual concebido para captura de tela e compartilhamento em redes. Moldura gótica ornamentada com acentos dourados e roxos. No topo, ilustração chiaroscuro do Vilão em seu trono; no corpo central, a mensagem do desafiante com tipografia destacada: *"**[Nome do Jogador] forjou um enigma insolúvel para você**"*, seguida da dificuldade em caveiras, da citação provocativa gerada pela IA e do botão proeminente *"**ACEITAR DESAFIO**"* ancorado ao deep link. Rodapé com atalhos de compartilhamento para WhatsApp, Instagram e Telegram. Mapeamento: FR-005.

**4. Tela de Ranking e Coortes (Mobile 9:16):**
Seletor superior em abas segmentadas: *Coorte Semanal*, *Nacional* e *Hall da Infâmia*. Pódio visual destacando os três primeiros colocados com avatares emoldurados em ouro, prata e bronze, exibindo sua taxa de obtenção de Bônus de Gênio. Lista rolável com linhas alternadas em Carvão Profundo, destacando a posição do usuário logado em Verde Neon com rolagem automática para sua linha. Ao lado de cada rival, botão rápido *"**DESAFIAR**"*. Mapeamento: FR-010, FR-013.

**5. Construtor Avançado de Enigmas (PC 16:9):**
Ambiente de engenharia lógica em três colunas. Coluna esquerda: catálogo e taxonomia de temas, árvore de premissas e parâmetros de inferência (temperatura, modelo SLM, número de passos). Coluna central: editor de montagem lógica, visualização da árvore de derivação dedutiva e console de execução do validador simbólico com saída em tempo real (Status: Solução Única Confirmada ✓). Coluna direita: simulador de visualização mobile para teste imediato de gameplay. Mapeamento: FR-001, FR-002, FR-003.

**6. Dashboard de Telemetria e Balanceamento (PC 16:9):**
Painel operacional para acompanhamento em tempo real dos gates de produto. Quatro métricas de topo: Desafios Aceitos/Dia (North Star), Retenção D1/D7/D30, Coeficiente K-Factor e Taxa de Bônus de Gênio. Gráficos centrais de dispersão temporal de resolução por enigma e matriz de calor de erros por distrator. Tabela inferior de calibração automática com alertas de anomalia lógica. Mapeamento: FR-011, FR-012.

**7. Painel do Tier Filosófico (PC 16:9):**
Interface acadêmica com galeria de bustos dos pensadores clássicos em 3D Chiaroscuro. Seletor de correntes filosóficas (Estoicismo a Existencialismo), construtor dialético de teses e antíteses, módulo de cruzamento com textos de domínio público e área de revisão com selo de chancela editorial da Hack Tech Farm. Mapeamento: FR-016.

## PARTE 3 — DESIGN SYSTEM 2.0 (CONSOLIDADO)

### 3.1 Manifesto de Design

O **Design System 2.0** consolida a assinatura *Dark Fantasy Chiaroscuro*. Não projetamos interfaces puramente utilitárias; construímos uma catedral digital de sombras profundas onde a luz possui significado semântico: o Roxo evoca a astúcia e a estratégia do Vilão, o Verde representa a agilidade analítica e o triunfo do Herói, e o Dourado simboliza o prestígio intelectual supremo. A regra 60-30-10 é imperativa em todas as superfícies.

### 3.2 Tipografia Oficial

| **Família Tipográfica** | **Pesos Utilizados** | **Finalidade / Aplicação** | **Exemplo de Escala (Mobile / Desktop)** |
| --- | --- | --- | --- |
| **Cinzel** (Serifada Display) | Regular (400), Bold (700), Black (900) | Títulos de impacto, nomes de personagens, cabeçalhos de cartas e telas. | H1: 28px / 36pxH2: 22px / 28pxH3: 18px / 22px |
| **Inter** (Sem Serifa UI) | Regular (400), Medium (500), SemiBold (600) | Corpo de texto, descrições narrativas, premissas, botões e formulários. | Body: 14px / 16pxSmall: 12px / 14pxCaption: 10px / 12px |
| **Roboto Mono** (Monospaçada) | Regular (400), Bold (700) | Cronômetro, pontuação numérica, identificadores de tokens e telemetria. | Timer: 24px / 32pxData: 12px / 14px |

### 3.3 Matriz de Estados de Componentes de UI

| **Componente** | **Estado Padrão (Default)** | **Hover / Foco** | **Pressionado (Active)** | **Desabilitado (Disabled)** |
| --- | --- | --- | --- | --- |
| **Botão Primário Vilão** | Fundo #6A3FA0, borda #8B5CF6, texto #F5F5F5, glow suave. | Fundo #8B5CF6, glow 0 0 20px rgba(139,92,246,0.6), elevação -2px. | Fundo #3D1F6E, escala 0.98, redução de glow. | Fundo #2A2A2A, texto #9E9E9E, borda transparente, sem glow. |
| **Botão Primário Herói** | Fundo #22C55E, borda #39FF14, texto #121212, glow suave. | Fundo #39FF14, glow 0 0 20px rgba(57,255,20,0.6), elevação -2px. | Fundo #166534, escala 0.98, texto #F5F5F5. | Fundo #2A2A2A, texto #9E9E9E, sem glow. |
| **Card de Resposta (Alternativa)** | Fundo #1A1A1A, borda #2A2A2A (1px), texto #F5F5F5. | Borda #8B5CF6 (1px), fundo #22222E. | Borda #39FF14 (2px), fundo #1A2E1A (se correto). | Fundo #141414, opacidade 0.5. |
| **Chip de Pista** | Fundo #2A2A2A, ícone lâmpada dourada, texto #9E9E9E. | Borda #D4AF37, texto #F0D98C. | Fundo #3D3010, borda #D4AF37. | Fundo #121212, ícone apagado (pista esgotada). |

### 3.4 Bloco Oficial de Tokens CSS (variables.css)

:root {
  /

Cores Estruturais (60%)

/
  --bg-primary: #121212;<br/>
  --bg-surface: #1A1A1A;<br/>
  --bg-subtle: #2A2A2A;<br/>
  --bg-elevated: #242424;

  /

Identidade do Vilão (30% e 10%)

/
  --villain-primary: #6A3FA0;<br/>
  --villain-deep: #3D1F6E;<br/>
  --villain-neon: #8B5CF6;

  /

Identidade do Herói (30% e 10%)

/
  --hero-primary: #22C55E;<br/>
  --hero-deep: #166534;<br/>
  --hero-neon: #39FF14;

  /

Prestígio e Conquista

/
  --gold-primary: #D4AF37;<br/>
  --gold-light: #F0D98C;<br/>
  --gold-deep: #8A6D1C;

  /

Feedback e Estados

/
  --state-success: #27AE60;<br/>
  --state-error: #C0392B;<br/>
  --state-warning: #E67E22;

  /

Tipografia

/
  --text-primary: #F5F5F5;<br/>
  --text-secondary: #9E9E9E;<br/>
  --text-muted: #666666;<br/>
  --font-display: 'Cinzel', serif;<br/>
  --font-body: 'Inter', sans-serif;<br/>
  --font-mono: 'Roboto Mono', monospace;

  /

Espaçamentos e Geometria

/
  --space-xs: 4px;<br/>
  --space-sm: 8px;<br/>
  --space-md: 16px;<br/>
  --space-lg: 24px;<br/>
  --space-xl: 32px;<br/>
  --radius-sm: 4px;<br/>
  --radius-md: 8px;<br/>
  --radius-lg: 16px;<br/>
  --radius-full: 9999px;

  /

Sombras e Efeitos de Brilho (Glow)

/
  --shadow-surface: 0 4px 12px rgba(0, 0, 0, 0.7);<br/>
  --shadow-glow-villain: 0 0 20px rgba(139, 92, 246, 0.45);<br/>
  --shadow-glow-hero: 0 0 20px rgba(57, 255, 20, 0.45);<br/>
  --shadow-glow-gold: 0 0 24px rgba(212, 175, 55, 0.50);

  /

Transições e Curvas de Animação

/
  --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);<br/>
  --transition-normal: 250ms cubic-bezier(0.4, 0, 0.2, 1);<br/>
  --transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
}

### 3.5 Motion Design e Microinterações

1. **Glow Pulsante em Repouso:** Bordas e runas dos personagens emitem pulso de iluminação suave em loop senoidal com ciclo de 2.4 segundos (

$$0.3 \to 0.85$$

de opacidade).
2. **Seleção de Alternativa:** Ao toque, o card executa compressão elástica de 0.98x em 100ms, seguida de expansão para 1.0x com emissão radial de partículas luminosas em caso de acerto.

3. **Transição de Pistas:** Ao solicitar pista, o painel expande suavemente com transição de altura em 250ms e transição de opacidade, acompanhado de som de papel envelhecido sendo desdobrado.

4. **Feedback de Erro de Dedução:** A tela executa tremor lateral rápido (shake de 8px com atenuação em 300ms) e vinheta periférica em Vermelho Dano (#C0392B).

### 3.6 Acessibilidade e Parâmetros WCAG AA

1. **Contraste Mínimo de Cores:** Todos os textos sobre fundos escuros cumprem a razão mínima de 4.5:1 para texto normal e 3.0:1 para títulos em escala ampliada.
2. **Áreas Mínimas de Toque:** Todos os alvos interativos (botões, chips de pista, cartas de alternativa) possuem dimensão física mínima de

$$44 \times 44\text{ px}$$

.
3. **Independência de Cor para Feedback:** Estados de acerto e erro não dependem unicamente de verde ou vermelho; são acompanhados por ícones distintos (✓ para correto, ✗ para incorreto) e vibração háptica tátil diferenciada.

### 3.7 Grid Responsivo e Breakpoints

| **Breakpoint** | **Faixa de Resolução** | **Colunas de Grid** | **Margens Laterais** | **Calha (Gutter)** |
| --- | --- | --- | --- | --- |
| **Mobile Compacto** | 360px a 479px | 4 colunas | 16px | 12px |
| **Mobile Expandido** | 480px a 767px | 4 ou 6 colunas | 20px | 16px |
| **Tablet / Web Compacta** | 768px a 1023px | 8 colunas | 32px | 20px |
| **Desktop / PC Dashboard** | 1024px a 1440px+ | 12 colunas | 48px | 24px |

### 3.8 Checklist de Homologação para Pull Requests de UI

- [ ] Fidelidade estrita à regra 60-30-10 em todas as visualizações.
- [ ] Remoção completa e verificada de quaisquer gradientes de ciano ou magenta.
- [ ] Respeito aos tokens tipográficos (Cinzel nos títulos, Inter no corpo, Roboto Mono nos dados).
- [ ] Teste de contraste WCAG AA validado com taxa superior a 4.5:1.
- [ ] Áreas de toque em conformidade com o padrão

$$44 \times 44\text{ px}$$

.
- [ ] Implementação de estados de foco visíveis para navegação por teclado na web.
- [ ] Resposta háptica e sonora vinculada aos eventos de acerto, erro e esgotamento de tempo.

## PARTE 4 — TECHNICAL DESIGN DOCUMENT (TDD) — NOVO

### 4.1 Arquitetura de Software e Diagrama de Componentes

O ecossistema é desacoplado em camadas especializadas, garantindo independência de serviços terceirizados e permitindo escalabilidade horizontal:

[ FRONTEND CLIENTS ]
├── Next.js 14 Web App (App Router + Tailwind + React Query)
└── React Native Mobile Client (Expo + Zustand + Skia)
        │
        ▼ (HTTPS / WSS com JWT Seguro)
[ BACKEND API GATEWAY - FastAPI (Python 3.12) ]
├── Authentication & Session Guard (JWT + Role Validation)
├── Enigma Routing Engine (Orquestrador de Duelos)
├── WebSocket Hub (Sincronização de Partida em Tempo Real)
└── Services Layer:
    ├── ValidatorService (Verificação Simbólica e Grafo Lógico)
    ├── ScoringService (Cálculo Determinístico de Pontuação)
    ├── InvitationService (Geração de Deep Links e Tokens Criptográficos)
    └── TelemetryCollector (Ingestão Assíncrona de Eventos)
        │
        ├── (Consultas / Transações ACID) ──► [ PostgreSQL 16 ] (pgcrypto, JSONB, Particionamento)
        ├── (Cache / Lock Distribuído)   ──► [ Redis 7 Cluster ] (Pool de Enigmas, Sessões, PubSub)
        ├── (Processamento em Fila)      ──► [ Celery Workers ] (Geração Batch, Auditoria e Purga)
        └── (Inferência Local Privada)   ──► [ Ollama Service ] (Llama 3.2 3B / Mistral NeMo 3B)

### 4.2 Modelo de Dados Relacional Detalhado (PostgreSQL 16)

O schema relacional é projetado para alto desempenho em leituras, integrando tipos nativos UUIDv4, JSONB indexado com GIN e particionamento temporal nas tabelas de telemetria e histórico de tentativas.

-- Extensões Obrigatórias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 1. Temas de Enigmas
CREATE TABLE riddle_themes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug VARCHAR(64) UNIQUE NOT NULL,
    title VARCHAR(128) NOT NULL,
    category VARCHAR(64) NOT NULL,
    description TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    tier VARCHAR(32) DEFAULT 'standard', -- standard, philosophical, event
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Templates de Enigmas Validados (Pool de Produção)
CREATE TABLE riddle_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id UUID NOT NULL REFERENCES riddle_themes(id) ON DELETE CASCADE,
    scenario TEXT NOT NULL,
    riddle_text TEXT NOT NULL,
    deduction_steps JSONB NOT NULL, -- Array estruturado de passos lógicos
    correct_answer VARCHAR(255) NOT NULL,
    distractors JSONB NOT NULL, -- Array de 3 a 5 strings verossímeis
    difficulty_skulls INT NOT NULL CHECK (difficulty_skulls BETWEEN 1 AND 10),
    is_validated BOOLEAN DEFAULT FALSE,
    validation_hash VARCHAR(64) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_riddle_templates_theme_diff ON riddle_templates(theme_id, difficulty_skulls);

-- 3. Pistas Progressivas
CREATE TABLE clues (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    template_id UUID NOT NULL REFERENCES riddle_templates(id) ON DELETE CASCADE,
    clue_order INT NOT NULL CHECK (clue_order BETWEEN 1 AND 3),
    clue_text TEXT NOT NULL,
    penalty_points INT NOT NULL DEFAULT 150,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(template_id, clue_order)
);

-- 4. Instâncias de Desafio (Convites Forjados)
CREATE TABLE challenges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    token VARCHAR(32) UNIQUE NOT NULL,
    creator_user_id UUID NOT NULL,
    template_id UUID NOT NULL REFERENCES riddle_templates(id),
    custom_taunt TEXT,
    time_limit_seconds INT NOT NULL DEFAULT 180,
    status VARCHAR(32) DEFAULT 'pending', -- pending, accepted, completed, expired
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
CREATE INDEX idx_challenges_token ON challenges(token);

-- 5. Tentativas do Herói
CREATE TABLE riddle_attempts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    challenge_id UUID NOT NULL REFERENCES challenges(id) ON DELETE CASCADE,
    player_user_id UUID NOT NULL,
    started_at TIMESTAMP WITH TIME ZONE NOT NULL,
    completed_at TIMESTAMP WITH TIME ZONE,
    time_spent_seconds NUMERIC(6, 2),
    clues_revealed INT DEFAULT 0,
    incorrect_submissions INT DEFAULT 0,
    is_successful BOOLEAN DEFAULT FALSE,
    steps_completed JSONB DEFAULT '[]'::jsonb
);

-- 6. Resultados e Consolidação de Pontuação
CREATE TABLE results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    attempt_id UUID UNIQUE NOT NULL REFERENCES riddle_attempts(id) ON DELETE CASCADE,
    base_score INT NOT NULL,
    time_bonus INT NOT NULL,
    clue_penalty INT NOT NULL,
    error_penalty INT NOT NULL,
    genius_bonus_applied BOOLEAN DEFAULT FALSE,
    final_score INT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 7. Ranking por Coortes (Particionado por Semana)
CREATE TABLE ranking_entries (
    id UUID DEFAULT gen_random_uuid(),
    cohort_id VARCHAR(32) NOT NULL, -- ex: '2026-W35-BR'
    user_id UUID NOT NULL,
    total_score INT NOT NULL DEFAULT 0,
    challenges_won INT NOT NULL DEFAULT 0,
    genius_count INT NOT NULL DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (cohort_id, id)
) PARTITION BY LIST (cohort_id);

-- 8. Telemetria de Eventos de Funil (Particionamento Temporal)
CREATE TABLE telemetry_events (
    id UUID DEFAULT gen_random_uuid(),
    event_name VARCHAR(64) NOT NULL,
    session_hash VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (created_at, id)
) PARTITION BY RANGE (created_at);

### 4.3 Motor de Validação Simbólica (TDD)

O ValidatorService executa a validação determinística formal em três fases de checagem antes de autorizar a inserção do enigma no pool de produção:

import hashlib
import json
from typing import Dict, Any, List

class SymbolicValidator:
    """Motor determinístico para auditoria e validação de consistência lógica de enigmas."""

    @staticmethod
    def compute_template_hash(template_data: Dict[str, Any]) -> str:<br/>
        payload = f"{template_data['riddle_text']}:{template_data['correct_answer']}:{sorted(template_data['distractors'])}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    @classmethod
    def validate_riddle_integrity(cls, data: Dict[str, Any]) -> bool:
        # 1. Checagem de Gabarito e Distratores
        correct = data.get("correct_answer", "").strip().lower()
        distractors = [d.strip().lower() for d in data.get("distractors", [])]
        
        if not correct or len(distractors) < 3:
            return False
        
        # O gabarito não pode coincidir com nenhum distrator
        if correct in distractors:
            return False
        
        # Não pode haver distratores duplicados
        if len(distractors) != len(set(distractors)):
            return False

        # 2. Verificação de Vazamento em Pistas (Leak Detection)
        clues: List[str] = data.get("clues", [])<br/>
        if len(clues) != 3:
            return False
        
        for clue in clues:
            clue_normalized = clue.lower()
            # O gabarito literal não pode estar contido na pista
            if correct in clue_normalized:
                return False
            
        # 3. Validação do Grafo de Dedução
        steps: List[Dict[str, Any]] = data.get("deduction_steps", [])<br/>
        if not (2 <= len(steps) <= 4):
            return False
        
        for step in steps:<br/>
            if not step.get("premise") or not step.get("deduction"):
                return False

        return True

### 4.4 Pipeline de Geração e Prompt Estruturado de IA

A inferência do SLM local é instruída com restrição de saída em JSON Schema estrito, eliminando marcadores conversacionais e prefixos:

{
  "$schema": "http://json-schema.org/draft-07/schema#",<br/>
  "title": "RiddleGenerationPayload",<br/>
  "type": "object",<br/>
  "properties": {<br/>
    "scenario": { "type": "string", "maxLength": 280 },<br/>
    "riddle_text": { "type": "string", "maxLength": 400 },<br/>
    "deduction_steps": {<br/>
      "type": "array",<br/>
      "minItems": 2,<br/>
      "maxItems": 4,<br/>
      "items": {<br/>
        "type": "object",<br/>
        "properties": {<br/>
          "step_number": { "type": "integer" },<br/>
          "premise": { "type": "string" },<br/>
          "deduction": { "type": "string" }
        },
        "required": ["step_number", "premise", "deduction"]
      }
    },
    "correct_answer": { "type": "string", "maxLength": 100 },<br/>
    "distractors": {<br/>
      "type": "array",<br/>
      "minItems": 3,<br/>
      "maxItems": 5,<br/>
      "items": { "type": "string", "maxLength": 100 }
    },
    "clues": {<br/>
      "type": "array",<br/>
      "minItems": 3,<br/>
      "maxItems": 3,<br/>
      "items": { "type": "string", "maxLength": 200 }
    },
    "estimated_difficulty": { "type": "integer", "minimum": 1, "maximum": 10 }
  },
  "required": [
    "scenario",
    "riddle_text",
    "deduction_steps",
    "correct_answer",
    "distractors",
    "clues",
    "estimated_difficulty"
  ],
  "additionalProperties": false
}

### 4.5 Implementação do Motor de Pontuação

def calculate_challenge_score(
    time_limit: int,<br/>
    time_spent: float,<br/>
    clues_revealed: int,<br/>
    incorrect_submissions: int,<br/>
    is_successful: bool<br/>
) -> Dict[str, Any]:<br/>
    if not is_successful or time_spent > time_limit:
        return {
            "base_score": 0,<br/>
            "time_bonus": 0,<br/>
            "clue_penalty": 0,<br/>
            "error_penalty": 0,<br/>
            "genius_bonus_applied": False,<br/>
            "final_score": 0
        }

    base_score = 1000
    time_ratio = max(0.0, (time_limit - time_spent) / float(time_limit))
    time_bonus = int(time_ratio * 300)
    clue_penalty = clues_revealed * 150
    error_penalty = incorrect_submissions * 200

    preliminary_score = max(0, base_score + time_bonus - clue_penalty - error_penalty)

    # Condição do Bônus de Gênio: Vitória sem pistas e sem erros
    is_genius = (clues_revealed == 0) and (incorrect_submissions == 0)
    final_score = int(preliminary_score * 1.5) if is_genius else preliminary_score

    return {
        "base_score": base_score,<br/>
        "time_bonus": time_bonus,<br/>
        "clue_penalty": clue_penalty,<br/>
        "error_penalty": error_penalty,<br/>
        "genius_bonus_applied": is_genius,<br/>
        "final_score": final_score
    }

### 4.6 Técnicas de Renderização dos Personagens (3D/2.5D)

1. **Shaders Emissivos PBR:** Os circuitos no sobretudo do Vilão e as runas das braçadeiras do Herói utilizam mapa de emissão dedicado (canal RGB para cor de brilho e canal Alpha para modulação da intensidade de pulsação).
2. **Rim Lighting Chiaroscuro:** Shader de iluminação de borda (Fresnel modificado com expoente 3.2) alimentado por duas luzes virtuais pontuais: Roxo Neon (#8B5CF6) na silhueta do Vilão e Verde Neon (#39FF14) na silhueta do Herói.

3. **Sistema de Blend Shapes (Morph Targets):** Malhas faciais estruturadas com 4 controladores de interpolação não linear para transição suave de expressões entre os turnos da partida.

4. **Rigging e Simulação de Tecido:** Configuração de IK com 3 nós para a empunhadura do cajado e do arco, combinada a física de malha simplificada (Verlet integration) para o caimento da capa verde e do sobretudo escuro.

### 4.7 Segurança, Integridade de Partida e Anti-Cheat

1. **Ocultação Criptográfica do Gabarito:** A resposta correta e as pistas bloqueadas jamais são enviadas no payload inicial do cliente. A validação ocorre estritamente no backend via hash criptográfico de comparação pontual.
2. **Anti-Tampering de Temporização:** O timestamp de início da partida é registrado atomicamente no Redis no momento em que o desafio é aceito. Na submissão, a diferença absoluta entre o tempo alegado pelo cliente e o delta do servidor não pode divergir em mais de 1.500ms (tolerância de jitter de rede).

3. **Assinatura de Transação de Partida:** Cada conclusão gera uma assinatura HMAC-SHA-256 vinculando attempt_id, final_score e session_token para evitar injeção de resultados artificiais no ranking.

### 4.8 Telemetria e Coleta de Eventos (LGPD)

| **Nome do Evento** | **Momento do Disparo** | **Atributos Coletados (Zero PII)** |
| --- | --- | --- |
| challenge_created | Vilão conclui a forja e gera o token | theme_id, difficulty_skulls, time_limit |
| invite_shared | Usuário aciona botão de compartilhamento | channel (WhatsApp, IG, Link), challenge_token_hash |
| challenge_accepted | Herói abre a interface e inicia o timer | challenge_token_hash, device_category |
| clue_requested | Herói desbloqueia uma das 3 pistas | clue_order, seconds_elapsed, attempt_id |
| submission_evaluated | Herói submete uma alternativa de resposta | is_correct, attempt_number, seconds_remaining |
| rematch_initiated | Perdedor aciona o botão de revanche | previous_attempt_id, new_theme_selected |

### 4.9 Estratégia de Testes Automatizados e Carga

- **Testes Unitários:** Cobertura mínima de 90% no motor de validação simbólica, verificando ausência de falsos positivos em detecção de vazamentos e integridade da fórmula de pontuação.
- **Testes de Integração:** Simulação completa do ciclo de vida do desafio via pytest-asyncio com banco PostgreSQL efêmero via Testcontainers.

- **Testes de Carga (Locust):** Simulação de 1.500 usuários concorrentes executando aceitação de desafio, consumo de pistas e submissão de respostas com limite de tolerância de erro de

$$0,01%$$

.

## PARTE 5 — BACKLOG EXECUTÁVEL E REGRAS DE GATES

### 5.1 Backlog Priorizado de Engenharia (P0 a P3)

| **ID** | **Prioridade** | **Épico** | **História de Usuário / Descrição Técnica** | **Estimativa** |
| --- | --- | --- | --- | --- |
| **ENG-001** | P0 | Infraestrutura | Provisionar PostgreSQL 16 com particionamento, Redis 7 e worker Celery via Docker Compose. | 3 dias |
| **ENG-002** | P0 | Motor de IA | Implementar serviço local Ollama com Llama 3.2 3B e parser de saída em JSON Schema estrito. | 5 dias |
| **ENG-003** | P0 | Validação | Desenvolver módulo SymbolicValidator para checagem de unicidade e vazamento de pistas. | 4 dias |
| **ENG-004** | P0 | Gameplay | Criar endpoints de aceitação, sincronização de tempo e submissão de respostas no FastAPI. | 4 dias |
| **ENG-005** | P0 | Frontend | Desenvolver as 4 telas mobile essenciais (Curador, Decifração, Card de Convite, Ranking). | 8 dias |
| **ENG-006** | P0 | Deep Linking | Implementar roteamento de convite universal o_vilao://challenge/{token} com Open Graph. | 3 dias |
| **ENG-007** | P1 | Pool Rotativo | Configurar job Celery periódico para manter buffer de 500 enigmas pré-validados no Redis. | 3 dias |
| **ENG-008** | P1 | Monetização | Integrar processamento de compras de temas cosméticos e rewarded ads voluntários. | 5 dias |
| **ENG-009** | P2 | Modo Detetive | Desenvolver gerador diário de enigma procedural com ranking global de sequências (streaks). | 6 dias |
| **ENG-010** | P2 | Tier Filosófico | Implementar construtor dialético e esteira de revisão com curadoria assistida em 2 camadas. | 7 dias |
| **ENG-011** | P3 | Guildas | Desenvolver sistema de duelos coletivos entre grupos e torneios sazonais. | 10 dias |

### 5.2 Regra de Bloqueio por Gates de Retenção

**Regra de Gate Inegociável:** O desenvolvimento dos itens classificados como **P2** (Modo Detetive e Tier Filosófico) e **P3** (Guildas e Torneios) permanece estritamente bloqueado até que o MVP (P0/P1) atinja e sustente, por no mínimo 14 dias consecutivos em ambiente de produção com coorte real, as métricas de **Retenção D1 ≥ 25%** e **Retenção D7 ≥ 9%**.

## PARTE 6 — PRÓXIMOS PASSOS E PLANO DE AÇÃO IMEDIATO

Com a homologação deste documento consolidado, o plano de execução imediata para os próximos 15 dias de sprint é estabelecido na seguinte sequência:

**1. Implementação das Telas Mobile P0:** Codificar os componentes de UI das 4 telas mobile essenciais (Curador, Decifração, Card de Convite e Ranking) em Next.js 14 e React Native, aplicando estritamente os tokens do Design System 2.0.
**2. Conexão do Coletor de Telemetria (FR-011):** Subir o serviço de ingestão assíncrona de eventos de funil com particionamento temporal no PostgreSQL 16 para monitoramento em tempo real do K-factor.
**3. Teste de Estresse da Curadoria com Coorte Beta:** Realizar teste operacional com 30 jogadores convidados para avaliar a latência de geração e a coerência lógica dos 500 primeiros enigmas forjados.
**4. Consolidação do Stack Tecnológico:** Congelar as versões do ambiente de execução (FastAPI 0.111, PostgreSQL 16.3, Redis 7.2, Ollama 0.3) sem dependências externas de BaaS.
**5. Assinatura Final de Ativos de Arte:** Homologar o pacote de renderizações 3D dos personagens para integração nos shaders e interfaces.

**TALES**

Curador, Arquiteto de Sistemas e Líder de Produto — Hack Tech Farm

Local e data: Florianópolis / São Paulo, 29 de agosto de 2026