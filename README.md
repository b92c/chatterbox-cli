# ChatterBox-CLI 🤖💬

Um chat bot interativo para terminal usando LangChain e Google Gemini, com funcionalidades avançadas de conversa, histórico e comandos especiais. **Totalmente em Português Brasileiro** com suporte a comandos em inglês para compatibilidade.

## ✨ Funcionalidades

### 🎯 Chat Básico

- Conversa em tempo real com Google Gemini
- Interface limpa e intuitiva no terminal em **Português Brasileiro**
- **Streaming real ativado por padrão** com fallback automático
- Histórico de conversa mantido durante a sessão
- **Comandos em português e inglês** para máxima usabilidade

### 💾 Gerenciamento de Conversas

- **Salvar conversas** em arquivos JSON com timestamps
- **Carregar conversas** anteriores para continuar onde parou
- **Histórico completo** visualizável a qualquer momento
- **Estatísticas** de mensagens trocadas

### 🚀 Otimizações de Performance

- **Streaming em tempo real**: Respostas aparecem conforme são geradas
- **Fallback inteligente**: Se streaming falhar, usa modo normal automaticamente
- **Interface responsiva**: Feedback visual claro do status de processamento
- **Configurações otimizadas**: Modelo Google Gemini 2.5 Flash

### 🇧🇷 Localização Brasileira

- **Interface 100% em português brasileiro**
- **Comandos nativos em português**: `/resumir`, `/traduzir`, `/salvar`, `/carregar`, `/comandos`
- **Comandos básicos em português**: `sair`, `limpar`, `ajuda`, `historico`, `contar`
- **Compatibilidade total**: Todos os comandos em inglês continuam funcionando
- **Experiência nativa**: Mensagens, prompts e interface adaptados ao português brasileiro

### 🔧 Comandos Especiais
- **`/resumir`** ou **`/summarize`** - Gera resumo da conversa atual
- **`/traduzir <idioma> <texto>`** ou **`/translate <idioma> <texto>`** - Traduz texto para qualquer idioma
- **`/salvar [arquivo]`** ou **`/save [arquivo]`** - Salva a conversa atual
- **`/carregar <arquivo>`** ou **`/load <arquivo>`** - Carrega uma conversa salva
- **`/comandos`** ou **`/commands`** - Lista todos os comandos disponíveis
- **`/stream`** - Liga/desliga modo streaming (respostas em tempo real)

### 🎮 Comandos Básicos
- `sair`, `quit`, `exit` - Encerra o chat
- `limpar`, `clear` - Limpa o histórico atual
- `ajuda`, `help` - Mostra o menu de ajuda
- `historico`, `histórico`, `history` - Exibe toda a conversa
- `contar`, `count` - Mostra estatísticas de mensagens

## 🚀 Instalação

### Pré-requisitos
- Python 3.8+
- Chave de API do Google Gemini

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd ChatterBox-CLI
```

### 2. Instale as dependências
```bash
pip install langchain-google-genai python-dotenv
```

### 3. Configure a API Key
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua chave
GOOGLE_API_KEY=sua_chave_api_aqui
```

### 4. Execute o chat
```bash
python main.py
```

## 🔑 Obtendo a API Key do Google Gemini

1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no arquivo `.env`

## 📖 Como Usar

### Conversação Normal
```
🙋 Você: Olá, como você está?
🤖 AI: Olá! Estou bem, obrigado por perguntar...
```

### Comandos Especiais
```bash
# Traduzir texto (português ou inglês)
🙋 Você: /traduzir inglês Bom dia
🙋 Você: /translate inglês Bom dia

# Resumir conversa (português ou inglês)
🙋 Você: /resumir
🙋 Você: /summarize

# Salvar conversa (português ou inglês)
🙋 Você: /salvar minha_conversa.json
🙋 Você: /save minha_conversa.json

# Carregar conversa salva (português ou inglês)
🙋 Você: /carregar minha_conversa.json
🙋 Você: /load minha_conversa.json

# Ver lista de comandos (português ou inglês)
🙋 Você: /comandos
🙋 Você: /commands

# Liga/desliga streaming
🙋 Você: /stream
```

### Comandos de Utilitário
```bash
# Ver histórico completo (português ou inglês)
🙋 Você: historico
🙋 Você: history

# Contar mensagens (português ou inglês)
🙋 Você: contar
🙋 Você: count

# Limpar histórico (português ou inglês)
🙋 Você: limpar
🙋 Você: clear

# Mostrar ajuda (português ou inglês)
🙋 Você: ajuda
🙋 Você: help

# Sair do chat (português ou inglês)
🙋 Você: sair
🙋 Você: quit
```

## 📁 Estrutura do Projeto

```
ChatterBox-CLI/
├── main.py              # Arquivo principal do chat
├── test_model.py        # Ferramenta de diagnóstico e validação
├── simple_chat.py       # Chat simplificado para testes
├── .env.example         # Exemplo de configuração
├── .env                 # Suas configurações (não versionado)
├── README.md            # Este arquivo
├── DEBUG.md             # Log de debugging e troubleshooting
├── PERFORMANCE.md       # Análise de performance e otimizações
└── chat_history_*.json  # Conversas salvas (criadas automaticamente)
```

## 🔧 Configurações Avançadas

O arquivo `.env` suporta configurações:

```bash
# Chave da API do Google Gemini (obrigatório)
GOOGLE_API_KEY=sua_chave_api_aqui
```

**Nota:** O ChatterBox-CLI foi otimizado para funcionar perfeitamente com as configurações padrão do Google Gemini 2.5 Flash, não sendo necessárias configurações adicionais.

## 📝 Formato das Conversas Salvas

As conversas são salvas em formato JSON estruturado:

```json
[
  {
    "type": "human",
    "content": "Olá!",
    "timestamp": "2025-08-02T10:30:00"
  },
  {
    "type": "ai",
    "content": "Olá! Como posso ajudar?",
    "timestamp": "2025-08-02T10:30:05"
  }
]
```

## 🐛 Solução de Problemas

### Erro de API Key
```
❌ Erro ao carregar modelo: Invalid API key
```
**Solução:** Verifique se a `GOOGLE_API_KEY` está correta no arquivo `.env`

### Erro de Dependências
```
ModuleNotFoundError: No module named 'langchain'
```
**Solução:** Instale as dependências:
```bash
pip install langchain-google-genai python-dotenv
```

### Erro de Arquivo não Encontrado
```
❌ Arquivo não encontrado: conversa.json
```
**Solução:** Verifique se o arquivo existe no diretório atual

## 🔍 Validação e Testes

### Ferramenta de Diagnóstico: `test_model.py`

Se você estiver enfrentando problemas com respostas vazias ou funcionamento inconsistente do chat, use nossa ferramenta de diagnóstico integrada:

```bash
python test_model.py
```

**O que esta ferramenta faz:**
- ✅ Testa a conexão direta com o modelo Google Gemini
- ✅ Valida se a API Key está funcionando corretamente
- ✅ Verifica se o modelo está retornando respostas válidas
- ✅ Isola problemas de configuração vs. problemas de lógica do chat
- ✅ Fornece debug detalhado do tipo e conteúdo das respostas

**Exemplo de saída esperada:**
```
🚀 Iniciando teste direto do modelo...
🔍 Testando modelo diretamente...
✅ Modelo inicializado com sucesso
📤 Enviando mensagem simples...
✅ Resposta recebida: content='Olá!' response_metadata={...}
✅ Conteúdo: 'Olá!'
✅ Tipo: <class 'langchain_core.messages.ai.AIMessage'>
✅ Tem conteúdo: True
✅ Conteúdo não vazio: True

🔍 Teste com pergunta mais complexa...
✅ Resposta 2: 'Estou funcionando bem, obrigado por perguntar!'

✅ TESTE DIRETO PASSOU! O modelo funciona.
```

**Interpretação dos resultados:**

| Resultado | Significado | Ação |
|-----------|-------------|------|
| ✅ **TESTE DIRETO PASSOU!** | Modelo e API funcionando corretamente | Se o chat principal não funciona, é problema de lógica no código |
| ❌ **TESTE DIRETO FALHOU!** | Problema de configuração ou API | Verifique API Key, conexão internet, dependências |
| 🔄 **Timeout/Travamento** | Problema de rede ou quota da API | Verifique conexão e limites da API |

**Quando usar:**
- 🔧 Antes de reportar bugs
- 🚨 Quando o chat retorna respostas vazias
- 🔍 Para isolar problemas de configuração
- 📊 Para validar nova instalação

### Outras Ferramentas de Debug

```bash
# Verificar versões das dependências
pip list | grep -E "(langchain|google)"

# Testar conectividade
python -c "import langchain_google_genai; print('✅ LangChain Google GenAI disponível')"

# Verificar variáveis de ambiente
python -c "import os; print('API Key:', '✅ Configurada' if os.getenv('GOOGLE_API_KEY') else '❌ Não encontrada')"
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- [LangChain](https://langchain.com/) - Framework para aplicações de IA
- [Google Gemini](https://deepmind.google/technologies/gemini/) - Modelo de linguagem
- [Python](https://python.org/) - Linguagem de programação

---

**ChatterBox-CLI** - Sua caixa de conversa inteligente no terminal! 🚀
