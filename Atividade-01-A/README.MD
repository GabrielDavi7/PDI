# Atividade Prática 01 - Processamento Digital de Imagens

Este repositório contém as resoluções da Atividade Prática 01 da disciplina de Processamento Digital de Imagens. O objetivo principal do projeto é realizar manipulações complexas de matrizes e pixels utilizando exclusivamente a biblioteca **NumPy** (vetorização, fatiamento e indexação booleana), respeitando a regra de não utilizar laços de repetição (`for`/`while`).

## 🛠️ Tecnologias e Dependências

Para executar os scripts, você precisará do Python instalado e das seguintes bibliotecas:

- `numpy` (Processamento matemático matricial)
- `matplotlib` (Leitura, exibição e salvamento de imagens)
- `Pillow` (PIL - Suporte auxiliar de imagens)

Você pode instalar todas as dependências rodando o comando abaixo no terminal:

```bash
pip install numpy matplotlib pillow

📁 Estrutura dos Arquivos
O projeto está dividido em quatro scripts principais, cada um resolvendo uma etapa específica da atividade:

1. slicing.py (Recortes e Mesclas com Matrizes)
Cria uma máscara preta com um quadrado branco central usando fatiamento matricial.

Gera um degradê horizontal (escala de cinza) utilizando np.linspace e np.tile.

Mescla as duas imagens de forma condicional utilizando np.where, exibindo o degradê apenas onde a máscara original é branca.

2. rgb_space.py (Brincando com Canais de Cor)
Realiza a leitura de uma imagem colorida, removendo o canal Alpha (transparência) caso exista.

Aplica o efeito BGR (inversão de canais) trocando o Vermelho e o Azul de lugar via fatiamento da terceira dimensão.

Cria um filtro vermelho puro zerando matematicamente os canais Verde e Azul.

3. statistics_threshold.py (Cálculos Estatísticos e Limiarização)
Converte a imagem colorida para tons de cinza extraindo a média dos canais RGB com np.mean().

Calcula a média geral de intensidade de todos os pixels e plota um Histograma de 255 barras.

Realiza uma Limiarização Analítica Automática (Thresholding), usando o valor exato da média como ponto de corte para transformar a imagem em uma matriz puramente preta e branca.

4. chroma_key.py (Efeito Chroma Key)
Isola uma cor de fundo específica (céu azul) utilizando cálculos de distância absoluta (np.abs) e tolerância para criar uma máscara booleana rigorosa.

Gera matematicamente um novo fundo contendo um degradê noturno vertical (do preto para o azul escuro).

Aplica o efeito Chroma Key mesclando o novo fundo na imagem original exatamente na área delimitada pela máscara.

🚀 Como Executar
Clone este repositório ou baixe os arquivos.

Certifique-se de ter uma imagem base para as questões 2, 3 e 4 salva no caminho especificado (por padrão: img/q2_a_original.png).

Abra o terminal na raiz do projeto.

Execute os scripts individualmente usando o Python. Exemplo:

'''
python slicing.py
python rgb_space.py
python statistics_threshold.py
python chroma_key.py
'''
📂 Saída (Outputs)
Ao rodar qualquer um dos scripts, o código exibirá as etapas visuais em janelas do Matplotlib. Ao fechar as janelas, as imagens processadas serão automaticamente salvas dentro de uma pasta chamada save_replies_image gerada na raiz do projeto.
```
