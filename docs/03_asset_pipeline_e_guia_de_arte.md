HACK TECH FARM

**O VILÃO — ASSET PIPELINE ****&**** GUIA DE ARTE ATUALIZADO (REVISÃO 3.0)**

*Personagens Finais, Pacote de Assets e Technical Design Document (TDD)*

29 de agosto de 2026

## 1. Visão Geral do Pacote de Assets

O presente documento estabelece a especificação técnica e artística definitiva para a produção, homologação e integração dos assets do projeto **O Vilão**. Consolidando a transição do produto para o modelo de enigmas e duelos dedutivos assíncronos (PRD/GDD 3.0), este pipeline unifica a direção de arte *Dark Fantasy Chiaroscuro* com o rigor da arquitetura computacional do jogo. Cada asset catalogado na matriz abaixo possui parâmetros estritos de resolução nativa, proporção de tela, formato de compressão e superfície de destino, garantindo paridade visual entre interfaces móveis, plataformas de mesa e materiais de conversão orgânica.

| **Identificador do Asset** | **Proporção** | **Resolução Nativa** | **Formato de Entrega** | **Superfície de Aplicação** |
| --- | --- | --- | --- | --- |
| Key Art Final (Vilão vs Herói) | 16:9 | 3840 × 2160 (4K Master) | PSD Master / WebP Lossless | Capa, Landing Page, App Store / Google Play |
| Turnaround — O Vilão Roxo | 16:9 | 3840 × 2160 px | PSD 16-bit / PNG Raw | Modelagem 3D, Rigging, Lookdev |
| Turnaround — O Herói Verde | 16:9 | 3840 × 2160 px | PSD 16-bit / PNG Raw | Modelagem 3D, Rigging, Lookdev |
| Pose Sheet — O Vilão Roxo | 16:9 | 3840 × 2160 px | PSD / PNG com Alpha | Animação, Cutscenes, Keyframes |
| Pose Sheet — O Herói Verde | 16:9 | 3840 × 2160 px | PSD / PNG com Alpha | Animação, HUD Interativo, Feedback |
| Solo — O Vilão Roxo | 16:9 e 9:16 | 3840 × 2160 / 2160 × 3840 | WebP / PNG com Alpha | Splash Screen, Tela do Curador, Loading |
| Solo — O Herói Verde | 16:9 e 9:16 | 3840 × 2160 / 2160 × 3840 | WebP / PNG com Alpha | Tela de Decifração, Vitória, Loading |
| Emblema Vetorial — O Vilão | 1:1 | 1024 × 1024 px (Vetorial) | SVG Otimizado / PNG 512px | Avatar HUD, Card de Convite, Favicon |
| Emblema Vetorial — O Herói | 1:1 | 1024 × 1024 px (Vetorial) | SVG Otimizado / PNG 512px | Avatar HUD, Ranking, Insígnia de Perfil |
| Mockups Mobile (4 Telas) | 9:16 | 1440 × 3200 px | Figma Tokenizado / PNG | Curador, Decifração, Convite, Coorte |
| Mockups PC (3 Telas) | 16:9 | 3840 × 2160 px | Figma Tokenizado / PNG | Construtor Avançado, Telemetria, Tier Filosófico |
| Prop — Cajado Tridente do Vilão | 1:1 / Livre | 2048 × 2048 px | FBX / Texture Pack 4K | Asset 3D Independente, Socket de Mão |
| Cenário — Trono Tecnológico | 16:9 | 3840 × 2160 px | FBX / Texturas PBR 4K | Background 3D, Cutscenes, Tier Filosófico |

## 2. Nomenclatura e Hierarquia de Pastas

A integridade do pipeline de desenvolvimento contínuo exige uma convenção determinística para nomeação de arquivos. Fica estritamente proibida a utilização de sufixos vagos como *final_v2* ou *ajustado*. Todos os colaboradores e ferramentas automatizadas de build devem seguir a fórmula estrutural:

[categoria]_[sujeito]_[variacao]_[aspecto]_[versao].[extensao]

Os parâmetros aceitos incluem categorias fixas (*keyart*, *char*, *prop*, *env*, *ui*, *mockup*, *token*), identificadores de sujeito (*vilao*, *heroi*, *curador*, *decifrador*, *sistema*), variações técnicas (*turnaround*, *poses*, *solo*, *emblem*, *diffuse*, *normal*, *emissive*), aspectos de proporção (*16x9*, *9x16*, *1x1*) e versões sequenciais semânticas (*v1*, *v2*, *v3*).

### 2.1 Árvore de Diretórios do Repositório de Assets

assets/
├── 00_source_files/
│   ├── figma/
│   │   ├── o_vilao_ui_kit_v3.fig
│   │   └── o_vilao_tokens.json
│   ├── 3d_raw_scenes/
│   │   ├── vilao_master_rig.blend
│   │   ├── heroi_master_rig.blend
│   │   └── throne_room_set.blend
│   └── raw_illustrations/
│       ├── keyart_master_comp_v3.psd
│       └── splash_portraits_v3.psd
├── 01_keyart/
│   ├── master/
│   │   └── keyart_vilao_vs_heroi_master_16x9_v3.psd
│   └── exports/
│       ├── keyart_vilao_vs_heroi_4k_16x9_v3.webp
│       ├── keyart_vilao_vs_heroi_fhd_16x9_v3.webp
│       └── keyart_vilao_vs_heroi_thumb_120x67_v3.webp
├── 02_characters/
│   ├── vilao/
│   │   ├── turnaround/
│   │   │   └── char_vilao_turnaround_16x9_v3.png
│   │   ├── poses_expressions/
│   │   │   └── char_vilao_pose_sheet_16x9_v3.png
│   │   ├── solo/
│   │   │   ├── char_vilao_solo_landscape_16x9_v3.webp
│   │   │   └── char_vilao_solo_portrait_9x16_v3.webp
│   │   └── textures/
│   │       ├── char_vilao_diffuse_4k_v3.png
│   │       ├── char_vilao_normal_4k_v3.png
│   │       ├── char_vilao_roughness_4k_v3.png
│   │       └── char_vilao_emissive_4k_v3.png
│   └── heroi/
│       ├── turnaround/
│       │   └── char_heroi_turnaround_16x9_v3.png
│       ├── poses_expressions/
│       │   └── char_heroi_pose_sheet_16x9_v3.png
│       ├── solo/
│       │   ├── char_heroi_solo_landscape_16x9_v3.webp
│       │   └── char_heroi_solo_portrait_9x16_v3.webp
│       └── textures/
│           ├── char_heroi_diffuse_4k_v3.png
│           ├── char_heroi_normal_4k_v3.png
│           ├── char_heroi_roughness_4k_v3.png
│           └── char_heroi_emissive_4k_v3.png
├── 03_props/
│   ├── throne/
│   │   ├── env_throne_model_v3.fbx
│   │   └── textures/
│   └── tridente/
│       ├── prop_vilao_cajado_tridente_v3.fbx
│       └── textures/
├── 04_ui_elements/
│   ├── emblems/
│   │   ├── ui_emblem_vilao_vector_1x1_v3.svg
│   │   └── ui_emblem_heroi_vector_1x1_v3.svg
│   ├── icons/
│   └── tokens/
│       └── tailwind_theme_tokens.json
└── 05_mockups/
    ├── mobile_9x16/
    │   ├── mockup_mobile_01_curador_9x16_v3.png
    │   ├── mockup_mobile_02_decifracao_9x16_v3.png
    │   ├── mockup_mobile_03_card_convite_9x16_v3.png
    │   └── mockup_mobile_04_ranking_coorte_9x16_v3.png
    └── pc_16x9/
        ├── mockup_pc_01_construtor_avancado_16x9_v3.png
        ├── mockup_pc_02_dashboard_telemetria_16x9_v3.png
        └── mockup_pc_03_tier_filosofico_16x9_v3.png

### 2.2 Políticas de Versionamento e Exportação

Todos os arquivos fonte brutos (PSD, Blend, Figma) mantêm-se em profundidade de cor de 16 bits por canal para preservação de gradientes no chiaroscuro. As exportações raster para produção utilizam a biblioteca cwebp configurada com compressão sem perdas (*lossless*) em assets de interface com transparência e fator de qualidade q=92 para pinturas contextuais. Os vetores de emblemas passam obrigatoriamente pelo utilitário svgo para eliminação de metadados redundantes, mantendo os IDs de camadas correspondentes aos nós de iluminação dinâmica da engine gráfica.

## 3. Especificações Técnicas por Tipo de Asset

### 3.1 Key Art Final 16:9

A Key Art constitui o ponto focal da narrativa visual. Em formato 16:9 nativo **3840 × 2160 px**, a composição retrata o duelo intelectual entre as duas forças em um cenário de cidadela gótico-futurista. O **Vilão Roxo** domina o terço esquerdo, elevado sobre degraus de basalto, irradiando luz volumétrica através de seu cajado e fendas de vestimenta. O **Herói Verde** posiciona-se no terço direito em semi-perfil dinâmico, com o arco tensionado e partículas de energia verde esmeralda dispersando a neblina.

O centro da imagem abriga o ponto de fuga chiaroscuro, onde as frequências de cor roxa (**#8B5CF6**) e verde neon (**#39FF14**) colidem em um gradiente sombrio que preserva o contraste de 4.5:1 exigido para sobreposição de tipografia do título. A legibilidade visual foi calibrada para manter o reconhecimento da silhueta dos personagens e o contraste dramático mesmo em miniaturas de **120 × 67 px** em canais de distribuição móvel.

### 3.2 Turnarounds dos Personagens

Os turnarounds estabelecem a base ortográfica para a modelagem tridimensional, contendo vistas frontal, lateral e dorsal em fundo neutro de estúdio (**#131318**) com linhas de alinhamento milimétricas para articulações e proporções anatômicas:

- **O Vilão Roxo (****"****O Mestre da Armadilha****"****):** Proporção canônica de **8,5 cabeças**. Silhueta esguia e imponente, postura ereta de comando aristocrático. Traje estruturado composto por sobretudo longo de gola alta reforçada com filamentos cibernéticos internos, colete formal com abotoamento duplo e meia-máscara geométrica integrada à estrutura óssea facial. O cajado de três pontas possui altura exata de 1,15x a estatura do personagem.

- **O Herói Verde (****"****O Fugitivo****"****):** Proporção ágil de **7,5 cabeças**. Silhueta aerodinâmica, musculatura atlética funcional sem exageros hipertróficos. Traje composto por manto com capuz assimétrico em tecido balístico, braçadeiras articuladas de couro tratado contendo placas metálicas com ranhuras para condução de energia, peitoral com broche circular esmeralda e coldre de arco rebaixado nas costas para evitar conflito com o volume do capuz.

### 3.3 Pose Sheets e Expressões Faciais

Os manuais de pose fornecem a ancoragem visual para as etapas de rigging, blend shapes e geração de quadros de vitória ou derrota:

- **Pose Sheet do Vilão:** Contém 3 poses ortopédicas de corpo inteiro em pé (Comando com Cajado apoiado, Mãos em Prece calculista, Casual de observação) e 1 pose de corpo inteiro sentado no Trono Tecnológico com pernas cruzadas. A fileira inferior detalha 4 expressões com chaveamento facial: Máscara Neutra (visor ativo uniforme), Máscara Desgastada (glitch luminoso e fissura estrutural), Rosto Humano Sério (maxilar cerrado, iluminação chiaroscuro rasante) e Rosto Humano Sorridente (expressão de escárnio refinado após vitória do enigma).

- **Pose Sheet do Herói:** Contém 4 poses de ação corporal completa (Ação em salto evasivo, Corrida de avanço rápido, Agachamento tático de observação com arco apoiado, Mira frontal de precisão com arco totalmente tensionado). A fileira de expressões mapeia 4 estados emocionais do decifrador: Foco Neutro, Surpresa Tática, Sorriso Confiante e Triunfo Amplo de Decifração.

### 3.4 Especificações Técnicas de Renderização e Shaders (TDD Visual)

**Diretriz de Shading:** Todos os personagens operam sob pipeline PBR (Physically Based Rendering) metálico/rugosidade com extensões para sub-superfície e canais de emissão controlados por código em tempo de execução.

A implementação dos materiais na engine gráfica obedece rigorosamente aos seguintes módulos de sombreamento:

- **Emissive Maps Dinâmicos:** Mapeamento de textura dedicado (RGBA 4K) onde os canais RGB controlam a cor base do brilho e o canal Alpha modula a intensidade do pulso elétrico através de funções senoidais computadas via script ($$I = I_{base} + A \cdot \sin(\omega t)$$). Circuitos do Vilão utilizam Roxo Elétrico (**#8B5CF6**, intensidade base 3.5 nits) e o Herói utiliza Verde Neon (**#39FF14**, intensidade base 4.2 nits).

- **Rim Lighting Chiaroscuro (Fresnel Customizado):** Shader de borda baseado no modelo de Fresnel modificado com expoente 3.2, garantindo que a luz de recorte destaque a silhueta contra fundos escuros sem lavar a saturação das texturas centrais:

$$F = \text{clamp}\left(1.0 - \max(0.0, \vec{N} \cdot \vec{V}), 0.0, 1.0\right)^{3.2}$$

- **Sistema de Blend Shapes:** A malha facial de ambos os personagens conta com 4 controladores primários de interpolação não-linear para transição entre expressões em 60 FPS, garantindo sincronização labial e resposta emocional aos feedbacks da IA.

- **Cinemática Inversa e Sockets:** O esqueleto base possui IK Handles nos pulsos e tornozelos. As mãos contêm sockets nomeados (Socket_Weapon_R e Socket_Bow_L) com restrições de orientação para acoplamento do Cajado Tridente e do Arco Composto.

- **Física de Tecidos (Cloth Simulation):** O capuz do Herói e as abas do sobretudo do Vilão utilizam malhas simplificadas de colisão acopladas a solucionadores de física Verlet com rigidez de flexão calibrada para responder realisticamente à aceleração das poses de ação.

### 3.5 Emblemas Vetoriais (1:1)

Projetados para escalabilidade extrema entre **32 × 32 px** (ícone de status no HUD) e **1024 × 1024 px** (insígnia de compartilhamento em alta resolução), os emblemas são gerados em formato vetorial puro (SVG):

- **Emblema do Vilão:** Geometria angular agressiva baseada na sobreposição de triângulos invertidos, representando a máscara aristocrática encimada por uma coroa de três pontas estilizada, com detalhes vazados que revelam o circuito interno roxo.

- **Emblema do Herói:** Curvas dinâmicas e arcos elípticos entrelaçados formando a meia-máscara do patrulheiro cibernético, integrada ao broche circular de folha esmeralda, simbolizando a agilidade e a busca pela quebra do enigma.

### 3.6 Assets de Cenário e Props Independentes

O **Cajado Tridente** é tratado como entidade 3D independente, exportado com malha fechada, ponto de pivô centralizado na empunhadura e material emissivo configurado para o cristal radiante superior. O **Trono Tecnológico** possui malha estática de 12.000 polígonos, contendo colisores primitivos pré-alinhados para recepção do nó de pose do Vilão (*Pose Snapping Socket*), facilitando o enquadramento de cutscenes do Construtor Avançado e do Tier Filosófico.

## 4. TDD (Technical Design Document) — Implementação Técnica

### 4.1 Arquitetura Geral do Sistema

O ecossistema computacional de **O Vilão** é fundamentado em uma arquitetura de serviços distribuídos de baixa latência e alta concorrência. A camada de apresentação (clientes Mobile em React Native e Web/Desktop em Next.js 14) comunica-se através de protocolos HTTP/2 (REST seguro) e WebSockets autenticados via JWT com o cluster de back-end implementado em **FastAPI (Python 3.11+)**.

O núcleo de serviços é particionado em quatro motores especializados: *Enigma Generation Engine* (integrado a SLMs locais via Ollama), *Symbolic Validator* (validação lógica determinística), *Realtime Duel Hub* (gerenciador de estados de partida sobre Redis 7) e *Telemetry Pipeline* (ingestão de eventos particionada). A persistência relacional é centralizada no **PostgreSQL 16** com suporte nativo a operações criptográficas através da extensão pgcrypto.

++
|                            CLIENTES (Next.js 14 / React Native)                   |
++
                                         │  ▲
              HTTPS / REST (JWT)         │  │        WSS (State Sync)
                                         ▼  │
++
|                        API GATEWAY & LOAD BALANCER (NGINX)                        |
++
                                         │
                                         ▼
++
|                     BACKEND SERVICES CLUSTER (FastAPI / Python)                   |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|  | Auth & Session Mgr |  | Enigma Orchestrator|  | Scoring & Anti-Cheat Engine |  |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|  +--------------------+  +--------------------+  +-----------------------------+  |
|  | WebSocket Duel Hub |  | Symbolic Validator |  | LGPD Telemetry Ingestion    |  |
|  +--------------------+  +--------------------+  +-----------------------------+  |
++
             │                         │                            │
             ▼                         ▼                            ▼
+--------------------------+  +--------------------------+  +-----------------------+
|  REDIS 7 (Cache & PubSub)|  | OLLAMA / SLM CLUSTER     |  | CELERY WORKERS (Queue)|
|  - Active Rooms          |  | - Mistral-7B Instruct    |  | - Batch Generation    |
|  - Rate Limiting Tokens  |  | - JSON Schema Strict Srv |  | - Telemetry Crunching |
+--------------------------+  +--------------------------+  +-----------------------+
                                       │
                                       ▼
++
|                     DATABASE CLUSTER (PostgreSQL 16 + pgcrypto)                   |
|  - Partitioned Telemetry    - Relational Schemas       - Cryptographic Vaults     |
++

### 4.2 Modelo de Dados Relacional (PostgreSQL 16)

O schema do banco de dados reflete o domínio assíncrono de enigmas, garantindo integridade referencial, indexação balanceada e isolamento estrito de dados sensíveis de usuários conforme exigências da LGPD.

-- Habilitação das extensões de segurança e UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- 1. Tabela de Temas Curados
CREATE TABLE riddle_themes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    slug VARCHAR(64) UNIQUE NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT NOT NULL,
    aesthetic_tag VARCHAR(32) NOT NULL DEFAULT 'GOTHIC_FUTURISTIC',
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Matriz de Templates de Enigmas
CREATE TABLE riddle_templates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    theme_id UUID NOT NULL REFERENCES riddle_themes(id) ON DELETE RESTRICT,
    title VARCHAR(255) NOT NULL,
    difficulty_tier SMALLINT NOT NULL CHECK (difficulty_tier BETWEEN 1 AND 10),
    scenario_prompt TEXT NOT NULL,
    riddle_text TEXT NOT NULL,
    deduction_steps_json JSONB NOT NULL,
    encrypted_solution_hash TEXT NOT NULL,
    validation_signature VARCHAR(64) NOT NULL,
    created_by_user_id UUID NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Pistas Progressivas com Custo de Dedução
CREATE TABLE clues (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    template_id UUID NOT NULL REFERENCES riddle_templates(id) ON DELETE CASCADE,
    sequence_order SMALLINT NOT NULL CHECK (sequence_order BETWEEN 1 AND 3),
    clue_text TEXT NOT NULL,
    penalty_deduction INTEGER NOT NULL DEFAULT 150,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_template_clue_seq UNIQUE (template_id, sequence_order)
);

-- 4. Instâncias de Desafios Disparados (O Convite)
CREATE TABLE challenges (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id UUID NOT NULL,
    riddle_template_id UUID NOT NULL REFERENCES riddle_templates(id),
    invite_code VARCHAR(16) UNIQUE NOT NULL,
    taunt_message TEXT,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Tentativas de Resolução do Herói
CREATE TABLE riddle_attempts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    challenge_id UUID NOT NULL REFERENCES challenges(id),
    solver_id UUID NOT NULL,
    started_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    submitted_at TIMESTAMP WITH TIME ZONE,
    time_elapsed_ms INTEGER,
    clues_unlocked_count SMALLINT NOT NULL DEFAULT 0,
    wrong_attempts_count SMALLINT NOT NULL DEFAULT 0,
    is_solved BOOLEAN NOT NULL DEFAULT false,
    session_hmac_signature VARCHAR(64) NOT NULL
);

-- 6. Tabela de Resultados e Pontuações
CREATE TABLE results (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    attempt_id UUID UNIQUE NOT NULL REFERENCES riddle_attempts(id),
    base_score INTEGER NOT NULL,
    time_penalty INTEGER NOT NULL,
    clue_penalty INTEGER NOT NULL,
    genius_bonus_applied BOOLEAN NOT NULL DEFAULT false,
    final_score INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Ranking por Coorte Dinâmica
CREATE TABLE ranking_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    cohort_id VARCHAR(32) NOT NULL,
    user_id UUID NOT NULL,
    accumulated_score BIGINT NOT NULL DEFAULT 0,
    solved_challenges_count INTEGER NOT NULL DEFAULT 0,
    genius_streak_count INTEGER NOT NULL DEFAULT 0,
    last_updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_cohort_user UNIQUE (cohort_id, user_id)
);

-- 8. Tabela de Telemetria Particionada (LGPD Safe)
CREATE TABLE telemetry_events (
    id UUID DEFAULT uuid_generate_v4(),
    event_name VARCHAR(64) NOT NULL,
    anonymous_user_hash VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    client_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
    server_timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id, server_timestamp)
) PARTITION BY RANGE (server_timestamp);

-- Índices de Otimização Operacional
CREATE INDEX idx_challenges_invite_code ON challenges(invite_code);
CREATE INDEX idx_attempts_challenge_solver ON riddle_attempts(challenge_id, solver_id);
CREATE INDEX idx_ranking_cohort_score ON ranking_entries(cohort_id, accumulated_score DESC);
CREATE INDEX idx_telemetry_event_time ON telemetry_events(event_name, server_timestamp);

### 4.3 Motor de Validação Simbólica

O validador simbólico é um módulo determinístico encarregado de certificar que nenhum enigma gerado pela IA contenha ambiguidade lógica, vazamento textual da solução ou múltiplos caminhos de dedução conflitantes antes da publicação.

import hashlib
import json
import re
from typing import Dict, List, Tuple

class SymbolicEnigmaValidator:<br/>
    def __init__(self, theme_vocabulary: set):
        self.vocabulary = theme_vocabulary

    def evaluate_uniqueness(self, options: List[str], correct_solution: str) -> bool:
        """Garante que a solucao seja estritamente unica entre as alternativas."""
        normalized_options = [opt.strip().lower() for opt in options]
        normalized_sol = correct_solution.strip().lower()
        
        if len(set(normalized_options)) != len(normalized_options):
            return False  # Distratores duplicados
        
        return normalized_options.count(normalized_sol) == 1

    def detect_clue_leakage(self, riddle_text: str, clues: List[str], solution: str) -> bool:
        """Verifica se a solucao literal vazou no corpo do enigma ou pistas."""
        sol_clean = solution.strip().lower()
        corpus = (riddle_text + " " + " ".join(clues)).lower()
        
        # Procura correspondencia de palavra inteira
        pattern = rf"\b{re.escape(sol_clean)}\b"
        return bool(re.search(pattern, corpus))

    def validate_deduction_graph(self, steps: List[Dict[str, str]]) -> bool:
        """Valida se a cadeia de inferencia logica possui conectividade estrita."""
        if len(steps) < 2:
            return False
        
        visited_nodes = set()
        for i, step in enumerate(steps):
            step_id = step.get("step_id")
            requires = step.get("requires_step")
            
            if not step_id or (i > 0 and requires not in visited_nodes):
                return False  # Quebra na cadeia de causalidade
            visited_nodes.add(step_id)
            
        return True

    def run_full_validation(self, enigma_payload: dict) -> Tuple[bool, str]:<br/>
        if not self.evaluate_uniqueness(enigma_payload["options"], enigma_payload["solution"]):<br/>
            return False, "FALHA: Opcoes duplicadas ou solucao ausente no conjunto."
            
        if self.detect_clue_leakage(enigma_payload["riddle_text"], enigma_payload["clues"], enigma_payload["solution"]):<br/>
            return False, "FALHA: Vazamento direto da solucao no texto do enigma."
            
        if not self.validate_deduction_graph(enigma_payload["deduction_steps"]):<br/>
            return False, "FALHA: Grafo de deducao apresenta descontinuidade causal."
            
        return True, "APROVADO: Enigma matematicamente integro."

### 4.4 Pipeline de Inteligência Artificial e Schema JSON

O motor generativo emprega instâncias de SLM (*Mistral-7B-Instruct* / *Llama-3-8B*) configuradas sob *Structured Outputs* via JSON Schema. O processo envolve a execução de 30 a 50 testes automatizados por lote com temperatura 

$$\tau = 0.7$$

 para calcular a taxa média de resolução por agentes de IA e calibrar o tier de dificuldade (1 a 10 caveiras). O agendador Celery executa tarefas noturnas em lote para reabastecer o pool com 200 a 500 novos enigmas diários por tema.

{
  "$schema": "http://json-schema.org/draft-07/schema#",<br/>
  "title": "EnigmaPayloadSchema",<br/>
  "type": "object",<br/>
  "properties": {<br/>
    "title": { "type": "string", "maxLength": 100 },<br/>
    "difficulty_tier": { "type": "integer", "minimum": 1, "maximum": 10 },<br/>
    "scenario_context": { "type": "string", "maxLength": 500 },<br/>
    "riddle_text": { "type": "string", "maxLength": 800 },<br/>
    "options": {<br/>
      "type": "array",<br/>
      "items": { "type": "string" },<br/>
      "minItems": 4,<br/>
      "maxItems": 4
    },
    "solution": { "type": "string" },<br/>
    "clues": {<br/>
      "type": "array",<br/>
      "items": { "type": "string" },<br/>
      "minItems": 3,<br/>
      "maxItems": 3
    },
    "deduction_steps": {<br/>
      "type": "array",<br/>
      "items": {<br/>
        "type": "object",<br/>
        "properties": {<br/>
          "step_id": { "type": "string" },<br/>
          "premise": { "type": "string" },<br/>
          "requires_step": { "type": ["string", "null"] }
        },
        "required": ["step_id", "premise"]
      },
      "minItems": 2
    },
    "villain_taunt": { "type": "string", "maxLength": 160 }
  },
  "required": [
    "title",
    "difficulty_tier",
    "scenario_context",
    "riddle_text",
    "options",
    "solution",
    "clues",
    "deduction_steps",
    "villain_taunt"
  ],
  "additionalProperties": false
}

### 4.5 Motor de Pontuação e Bônus de Gênio

O cálculo da pontuação final da partida pondera precisão, agilidade e autonomia analítica. A fórmula matemática canônica é descrita por:

$$S = \max\left(0, \left(B - (T_{ms} \cdot \lambda) - (C \cdot P_c) - (W \cdot P_w)\right)\right) \times G$$

Onde 

$$B = 1000$$

 representa os pontos base, 

$$T_{ms}$$

 é o tempo decorrido em milissegundos, 

$$\lambda = 0.002$$

 é o coeficiente de decaimento temporal, 

$$C$$

 é a quantidade de pistas consultadas (

$$P_c = 150$$

 pts cada), 

$$W$$

 é o número de tentativas erradas (

$$P_w = 200$$

 pts cada) e 

$$G$$

 representa o **Bônus de Gênio** (

$$G = 1.5$$

 se resolvido em 

$$T \le 45\text{s}$$

 com 

$$C = 0$$

 e 

$$W = 0$$

; caso contrário, 

$$G = 1.0$$

).

def calculate_enigma_score(time_elapsed_ms: int, clues_used: int, wrong_attempts: int, is_correct: bool) -> dict:<br/>
    if not is_correct:<br/>
        return {"base_score": 0, "final_score": 0, "genius_bonus": False}

    BASE_SCORE = 1000
    LAMBDA_TIME = 0.002
    CLUE_PENALTY_RATE = 150
    WRONG_PENALTY_RATE = 200

    time_penalty = int(time_elapsed_ms * LAMBDA_TIME)
    clue_penalty = clues_used * CLUE_PENALTY_RATE
    wrong_penalty = wrong_attempts * WRONG_PENALTY_RATE

    raw_score = BASE_SCORE - time_penalty - clue_penalty - wrong_penalty
    normalized_base = max(0, raw_score)

    # Condicao estrita para o Bonus de Genio (1.5x)
    is_genius = (time_elapsed_ms <= 45000) and (clues_used == 0) and (wrong_attempts == 0)
    multiplier = 1.5 if is_genius else 1.0
    final_score = int(normalized_base * multiplier)

    return {
        "base_score": normalized_base,<br/>
        "time_penalty": time_penalty,<br/>
        "clue_penalty": clue_penalty,<br/>
        "wrong_penalty": wrong_penalty,<br/>
        "genius_bonus": is_genius,<br/>
        "final_score": final_score
    }

### 4.6 Segurança Criptográfica e Anti-Cheat

**Regra de Ouro da Segurança:** O gabarito de um enigma JAMAIS trafega para o dispositivo cliente antes da submissão final do palpite.

- **Ocultação da Solução:** O cliente recebe apenas o identificador da alternativa encriptado por um hash salgado não-reversível na sessão. A validação ocorre estritamente na API.

- **Validação de Assinatura de Sessão (HMAC-SHA-256):** Toda ação do cliente (abertura de pista, clique de dedução, palpite final) envia um payload assinado digitalmente com segredo temporário armazenado em Redis.

- **Anti-Tampering de Temporização:** O servidor confronta o timestamp registrado na inicialização do WebSocket com o instante da requisição final. Resoluções com discrepância superior a 1500 ms em relação ao relógio atômico do servidor são sumariamente invalidadas para auditoria.

### 4.7 Telemetria Granular em Conformidade com a LGPD

O sistema realiza o desacoplamento total entre dados de identificação pessoal (PII) e o stream analítico de eventos. Os dados cadastrais residem no schema isolado pii_data sob encriptação simétrica via pgcrypto. Os eventos de produto operam exclusivamente com hashes unidirecionais não-rastreáveis.

| **Nome do Evento** | **Momento do Disparo** | **Parâmetros Registrados (JSON)** | **Finalidade Analítica** |
| --- | --- | --- | --- |
| enigma_created | Vilão conclui a curadoria | {theme_id, difficulty, length_chars} | Métricas de oferta e diversidade |
| challenge_shared | Disparo do link de convite | {challenge_id, channel: "WA"│"IG"} | Cálculo primário do K-factor |
| challenge_opened | Herói carrega a página do convite | {challenge_id, is_new_user: bool} | Funil de aquisição viral |
| clue_requested | Herói desbloqueia pista (1, 2 ou 3) | {attempt_id, clue_index, time_offset_ms} | Balanceamento de dificuldade |
| attempt_submitted | Herói envia resposta final | {attempt_id, is_solved, elapsed_ms, score} | Retenção, D1/D7 e Bônus de Gênio |

### 4.8 Estratégia de Testes Automatizados e Homologação de Carga

A integridade da aplicação é garantida por baterias de testes com cobertura mínima de **85%** nos módulos críticos de validação simbólica, segurança e pontuação. A infraestrutura é submetida periodicamente a testes de estresse com o framework *Locust*, simulando **1.500 requisições concorrentes por segundo** sob latência p95 inferior a 85 ms em instâncias de produção.

## 5. Critérios de Aceite (Definition of Done)

Nenhum asset visual ou componente de software será considerado pronto para implantação sem satisfazer integralmente os seguintes requisitos de qualidade:

- **Fidelidade Cromática Gótico-Futurista:** Aderência estrita à paleta aprovada (Vilão: Roxo **#8B5CF6** / **#6D28D9**; Herói: Verde **#39FF14** / **#22C55E**; Prestígio: Dourado **#F5C518**; Fundo: Carvão **#0B0B0F** / **#131318**). Ausência total de tons ciano ou magenta.

- **Harmonia Chiaroscuro e Iluminação:** Todos os personagens e elementos de cena devem compartilhar a mesma temperatura de luz rasante, com sombreamento volumétrico contrastante e rim light proporcional às intensidades nits especificadas.

- **Escalabilidade e Responsividade de Ícones:** Todos os emblemas e glifos devem ser homologados em formato SVG com testes de acuidade visual em 32 px, 64 px e 512 px sem perda de definição geométrica.

- **Conformidade de Acessibilidade (WCAG AA):** Taxa de contraste entre texto e plano de fundo igual ou superior a **4.5:1** para corpo de texto e **3:1** para elementos gráficos informativos e títulos de grande formato.

- **Ergonomia e Áreas de Toque:** Elementos clicáveis e botões em plataformas móveis devem possuir alvos mínimos de toque de **44 × 44 px** com espaçamento periférico isolado de 8 px.

- **Integridade de Estados de Componentes:** Cada elemento interativo deve conter implementações visuais explícitas para os estados: *Default*, *Hover*, *Active*, *Focus*, *Disabled*, *Loading* e *Error*.

- **Paridade com o Schema Técnico:** Os modelos 3D exportados devem conter a árvore de sockets e nomes de blend shapes em conformidade estrita com as chamadas de código documentadas na Seção 3.4.

## 6. Fluxo de Entrega e Pipeline de Produção

O ciclo de vida dos assets é gerenciado através de seis etapas sequenciais com portões de aprovação técnica e artística bem definidos:

[Etapa 1: Briefing & Requisitos] 
              │
              ▼
[Etapa 2: Aprovação de Conceito (Tales)] 
              │
              ▼
[Etapa 3: Modelagem / Renderização HD] 
              │
              ▼
[Etapa 4: Auditoria Técnica de QA (Shaders, Cores, WCAG)] 
              │
              ▼
[Etapa 5: Otimização & Exportação (SVGO, cwebp, LODs)] 
              │
              ▼
[Etapa 6: Integração no Repositório & CI/CD]

A matriz de responsabilidades distribui as atribuições entre as lideranças do projeto:

- **Diretoria de Arte ****&**** Produto (Tales):** Responsabilidade final sobre a aprovação estética, fidelidade do tom dos enigmas e validação dos portões de entrada e saída de versão.

- **Modelagem 3D ****&**** Shading:** Execução das malhas, abertura de mapas de UV sem distorção, configuração dos shaders PBR e exportação de LODs funcionais.

- **Rigging ****&**** Animação:** Implementação de esqueletos com restrições IK, mapeamento dos controladores de blend shapes faciais e física de tecido.

- **UI/UX Engineering:** Desenvolvimento dos componentes visuais em Figma, exportação de design tokens JSON e homologação de acessibilidade.

- **Engenharia de Back-end:** Manutenção da integridade dos esquemas SQL, algoritmos de validação simbólica e monitoramento dos testes de estresse.

## 7. Mapeamento de Assets para Telas e Superfícies

A tabela a seguir correlaciona formalmente cada asset catalogado às respectivas superfícies de aplicação e interfaces de usuário no ecossistema do jogo:

| **Asset Designado** | **Superfície de Apresentação** | **Contexto e Comportamento Visual** | **Objetivo de UX / Conversão** |
| --- | --- | --- | --- |
| Key Art Final (16:9) | Deck Executivo / Landing Page / Lojas | Hero section com overlay gradiente carvão e iluminação chiaroscuro nas bordas | Gancho visual instantâneo e ancoragem da proposta de valor |
| Solo — O Vilão Roxo | Tela do Curador / Splash Screen | Ilustração de destaque com pulso elétrico sutil no cristal do cajado | Reforçar a identidade de arquiteto do dilema e comando |
| Solo — O Herói Verde | Tela de Decifração / Tela de Vitória | Personagem em pose de observação tática com rim light esmeralda ativa | Sensação de agilidade e foco analítico sob pressão de tempo |
| Emblema do Vilão (SVG) | Card de Convite / Avatar HUD | Insígnia vetorial com gradiente roxo e coroa de três pontas vazada | Marca visual compartilhável em redes sociais (WhatsApp/Stories) |
| Emblema do Herói (SVG) | Tela de Ranking / Perfil do Decifrador | Broche esmeralda estilizado com bordas douradas para usuários Top 1 | Símbolo de prestígio competitivo e diferenciação por coorte |
| Cajado Tridente (Prop 3D) | Animações do Vilão / Tier Filosófico | Malha acoplada ao socket da mão com emissão dinâmica volumétrica | Elemento de autoridade nas cutscenes de forja de enigmas |
| Trono Tecnológico (Cenário) | Construtor Avançado / Tier Filosófico | Estrutura de fundo em perspectiva com iluminação roxa rasante | Atmosfera imersiva para curadoria profunda em telas desktop |
| Mockups Mobile (4 Telas) | Documentação Técnica / Guia Front-end | Especificação pixel-perfect com tokens integrados para React Native | Garantia de fidelidade de implementação na engenharia |
| Mockups PC (3 Telas) | Documentação Técnica / Aplicação Web | Layouts 16:9 com grids densos de telemetria e biblioteca de temas | Suporte a operações analíticas de curadores e administradores |

## 8. Próximos Passos e Priorização Técnica

O plano de execução está estruturado em quatro níveis de prioridade técnica condicionados ao cumprimento de métricas de engajamento (*Quality Gates*):

- **Prioridade P0 (Imediata — Sprint Core Mobile):**
Integração dos Emblemas Vetoriais SVG nos componentes de HUD e geração do Card de Convite dinâmico.

- Implementação das telas mobile (Curador, Decifração, Card de Convite, Ranking por Coorte) em React Native.

- Fechamento da pipeline de shaders emissivos dos personagens para telas de carregamento e avatar.

- **Prioridade P1 (Sprint Desktop ****&**** Telemetria):**
Implementação do Construtor Avançado e Dashboard de Telemetria no front-end Next.js 14.

- Integração do modelo 3D do Trono e Cajado nas telas de recompensa e curadoria estendida.

- **Prioridade P2 (Pós-Validação do Core Loop):**
Ativação do módulo do **Tier Filosófico** com galerias dialéticas e validação de enigma em duas etapas.

- Liberação condicionada ao atingimento do Gate de Retenção: **D1 ≥ 25%** e **D7 ≥ 9%** sustentados por 14 dias contínuos em coorte de testes.

- **Prioridade P3 (Expansão de Comunidade ****&**** Guildas):**
Desenvolvimento do sistema de Duelos de Guildas e temporadas competitivas.

- Liberação condicionada ao atingimento de Coeficiente Viral **K-factor ≥ 15%** e taxa de conclusão de desafios superior a 60%.

**Recomendação Operacional:** Executar rodada de testes de usabilidade com grupo focal de 20 a 30 jogadores para aferição dos limites de legibilidade da tipografia Cinzel e do tempo de percepção das pistas no cronômetro antes do envio da build final às lojas.

**Tales**
Curador e Líder de Produto — Hack Tech Farm

Local e data: Florianópolis/SC, 29 de agosto de 2026

*Documento elaborado em 29 de agosto de 2026. As informações contidas são de responsabilidade do solicitante.*