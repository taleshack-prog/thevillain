# assets — Pipeline de Arte (SSoT Pipeline 2.1, Rev. 3.0)

Estrutura oficial de pastas para key art, personagens, props, emblemas e mockups.
Nomenclatura: `tipo_sujeito_descricao_ratio_versao.ext` (ex.:
`char_vilao_solo_portrait_9x16_v3.webp`).

Politicas: fontes brutas (PSD/BLEND/FIG) em 16 bits/canal; exportacao raster via
`cwebp` (lossless em UI transparente, q=92 em pinturas); vetores via `svgo`.
Arquivos fonte pesados devem ir para **Git LFS** (ver `.gitignore`).
